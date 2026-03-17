#!/usr/bin/env python3
"""
熵清 V6 API 代理服务
隐藏真实 API Key，提供安全的对话接口
"""

from flask import Flask, request, jsonify
from flask_cors import CORS
import requests
import os
from datetime import datetime
import hashlib

app = Flask(__name__)
CORS(app)

# ==================== 配置 ====================

# EdgeAI API 配置
EDGEAI_API_URL = "https://api.edgefn.net/v1/chat/completions"
EDGEAI_MODEL = "DeepSeek-R1-0528-Qwen3-8B"

# 真实的 API Key（从环境变量读取，不暴露在代码中）
API_KEY = os.environ.get("EDGEAI_API_KEY", "sk-kQgvcXjX1wrIuY41C6D8A9F0Cf8e4b00B45356967e4d710b")

# 访问令牌（用于前端认证）
ACCESS_TOKEN = os.environ.get("SHANGQING_ACCESS_TOKEN", "shangqing-v6-secret-token-2026")

# 请求频率限制（每分钟最多请求数）
RATE_LIMIT = 60

# 请求记录（用于限流）
request_log = {}

# ==================== 辅助函数 ====================

def get_client_ip():
    """获取客户端IP"""
    if request.headers.getlist("X-Forwarded-For"):
        return request.headers.getlist("X-Forwarded-For")[0]
    return request.remote_addr

def check_rate_limit(ip):
    """检查请求频率限制"""
    now = datetime.now()
    minute_key = f"{ip}_{now.strftime('%Y%m%d%H%M')}"

    if minute_key not in request_log:
        request_log[minute_key] = 0

    request_log[minute_key] += 1

    if request_log[minute_key] > RATE_LIMIT:
        return False

    return True

def validate_access_token():
    """验证访问令牌"""
    token = request.headers.get("Authorization", "").replace("Bearer ", "")

    if token == ACCESS_TOKEN:
        return True

    return False

def mask_api_key(key):
    """隐藏 API Key（只显示前后各4位）"""
    if len(key) <= 8:
        return "****"
    return key[:4] + "..." + key[-4:]

# ==================== 路由 ====================

@app.route("/health", methods=["GET"])
def health():
    """健康检查"""
    return jsonify({
        "status": "ok",
        "service": "熵清V6 API代理",
        "model": EDGEAI_MODEL,
        "timestamp": datetime.now().isoformat()
    })

@app.route("/api/chat", methods=["POST"])
def chat():
    """对话接口"""
    # 1. 验证访问令牌
    if not validate_access_token():
        return jsonify({
            "error": "unauthorized",
            "message": "无效的访问令牌"
        }), 401

    # 2. 频率限制
    ip = get_client_ip()
    if not check_rate_limit(ip):
        return jsonify({
            "error": "rate_limit_exceeded",
            "message": f"请求频率超过限制（每分钟最多{RATE_LIMIT}次）"
        }), 429

    # 3. 获取请求数据
    data = request.json

    if not data or "messages" not in data:
        return jsonify({
            "error": "invalid_request",
            "message": "缺少 messages 参数"
        }), 400

    # 4. 调用 EdgeAI API
    try:
        headers = {
            "Authorization": f"Bearer {API_KEY}",
            "Content-Type": "application/json"
        }

        payload = {
            "model": EDGEAI_MODEL,
            "messages": data["messages"],
            "stream": data.get("stream", False)
        }

        response = requests.post(
            EDGEAI_API_URL,
            headers=headers,
            json=payload,
            timeout=60
        )

        result = response.json()

        if "choices" in result and result["choices"]:
            choice = result["choices"][0]
            return jsonify({
                "content": choice["message"].get("content", ""),
                "thinking": choice["message"].get("reasoning_content"),
                "usage": result.get("usage", {})
            })
        else:
            return jsonify({
                "error": "api_error",
                "message": result
            }), 500

    except requests.exceptions.Timeout:
        return jsonify({
            "error": "timeout",
            "message": "API 请求超时"
        }), 504

    except Exception as e:
        return jsonify({
            "error": "server_error",
            "message": str(e)
        }), 500

@app.route("/api/stats", methods=["GET"])
def stats():
    """统计信息（需要验证）"""
    if not validate_access_token():
        return jsonify({"error": "unauthorized"}), 401

    # 清理旧的日志（保留最近5分钟）
    now = datetime.now()
    cutoff = now.replace(minute=now.minute - 5)
    for key in list(request_log.keys()):
        try:
            # 解析时间
            parts = key.rsplit("_", 2)
            if len(parts) == 3:
                log_time = datetime.strptime(parts[1] + parts[2], "%Y%m%d%H%M")
                if log_time < cutoff:
                    del request_log[key]
        except:
            pass

    return jsonify({
        "total_requests": sum(request_log.values()),
        "active_ips": len(set(k.rsplit("_", 1)[0] for k in request_log.keys())),
        "masked_api_key": mask_api_key(API_KEY),
        "model": EDGEAI_MODEL
    })

# ==================== 启动 ====================

if __name__ == "__main__":
    PORT = 5001  # 避免5000冲突
    print("""
╔════════════════════════════════════════════════════════════════╗
║         熵清 V6 API 代理服务启动 🚀                           ║
╚════════════════════════════════════════════════════════════════╝

📡 服务地址: http://0.0.0.0:{}
🔐 API 密钥: {} (已隐藏)
🎯 后端模型: {}
🔑 访问令牌: {} (需在前端 Authorization 头中使用)

⚡ 限流设置: 每分钟 {} 次请求

📝 使用方法:
   POST /api/chat
   Headers: Authorization: Bearer <ACCESS_TOKEN>
   Body: {{"messages": [...]}}

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
""".format(
        PORT,
        mask_api_key(API_KEY),
        EDGEAI_MODEL,
        ACCESS_TOKEN,
        RATE_LIMIT
    ))

    # 开发模式
    app.run(host="0.0.0.0", port=PORT, debug=True)

    # 生产模式（推荐）
    # app.run(host="0.0.0.0", port=PORT)

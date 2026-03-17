# 熵清 V6 API 代理服务

## 安全架构

### 问题
原版 V6 网页直接在前端调用 EdgeAI API，API Key 暴露在 JavaScript 代码中，存在安全风险。

### 解决方案
创建后端代理服务，隐藏真实 API Key，前端通过本地接口访问。

---

## 文件结构

```
paper/
├── api_proxy.py      # Flask 后端代理服务
├── v6.html           # 前端对话界面（已更新）
├── start_proxy.sh    # 启动脚本
├── stop_proxy.sh     # 停止脚本
└── logs/
    └── api_proxy.log # 运行日志
```

---

## 快速开始

### 1. 启动代理服务

```bash
./start_proxy.sh
```

或者手动启动：

```bash
python3 api_proxy.py
```

### 2. 打开网页

在浏览器中打开 `v6.html`

### 3. 停止服务

```bash
./stop_proxy.sh
```

---

## API 接口

### 健康检查

```bash
GET http://localhost:5001/health
```

响应：

```json
{
  "status": "ok",
  "service": "熵清V6 API代理",
  "model": "DeepSeek-R1-0528-Qwen3-8B",
  "timestamp": "2026-03-17T11:39:00.000000"
}
```

### 对话接口

```bash
POST http://localhost:5001/api/chat
Headers:
  Authorization: Bearer shangqing-v6-secret-token-2026
  Content-Type: application/json

Body:
{
  "messages": [
    {"role": "system", "content": "系统提示词"},
    {"role": "user", "content": "用户问题"}
  ]
}
```

响应：

```json
{
  "content": "回答内容",
  "thinking": "思考过程",
  "usage": {
    "prompt_tokens": 11,
    "total_tokens": 101,
    "completion_tokens": 90
  }
}
```

### 统计接口

```bash
GET http://localhost:5001/api/stats
Headers:
  Authorization: Bearer shangqing-v6-secret-token-2026
```

---

## 安全特性

### 1. API Key 隐藏
- 真实 API Key 存储在服务器端
- 前端无法访问

### 2. 访问令牌
- 前端使用 `ACCESS_TOKEN` 进行认证
- 防止未授权访问

### 3. 频率限制
- 每个IP每分钟最多 60 次请求
- 防止滥用

### 4. 日志记录
- 记录所有请求
- 追踪异常行为

---

## 配置

### 环境变量

在 `api_proxy.py` 中配置：

```python
API_KEY = os.environ.get("EDGEAI_API_KEY", "你的API密钥")
ACCESS_TOKEN = os.environ.get("SHANGQING_ACCESS_TOKEN", "你的访问令牌")
RATE_LIMIT = 60  # 每分钟请求数
```

### 前端配置

在 `v6.html` 中配置：

```javascript
const PROXY_API_URL = "http://localhost:5001/api/chat";
const ACCESS_TOKEN = "shangqing-v6-secret-token-2026";
```

---

## 部署到生产环境

### 方案 1: 本地部署（当前）
适合个人使用，网页只能在本地访问

### 方案 2: 服务器部署
1. 将 `api_proxy.py` 部署到服务器
2. 使用 Gunicorn + Nginx 部署
3. 更新 `v6.html` 中的 API 地址

### 方案 3: 容器化部署
使用 Docker 部署代理服务

---

## 故障排查

### 服务无法启动
```bash
# 检查端口占用
lsof -i :5001

# 查看日志
tail -f logs/api_proxy.log
```

### 前端无法连接
```bash
# 检查服务是否运行
curl http://localhost:5001/health

# 检查防火墙
```

### API 错误
```bash
# 查看详细日志
tail -50 logs/api_proxy.log
```

---

## 安全建议

1. **更改默认令牌**
   - 修改 `ACCESS_TOKEN` 为随机字符串
   - 不要在公开仓库中提交

2. **使用 HTTPS**
   - 生产环境使用 HTTPS 加密传输

3. **限制访问IP**
   - 只允许特定IP访问代理服务

4. **定期更新密钥**
   - 定期更换 API Key 和访问令牌

---

## 作者

郑豪 (ZH040829)

## 许可

MIT License

#!/usr/bin/env python3
"""
🌌 熵清广播 API
部署到任何 Python 环境即可
"""
from http.server import HTTPServer, BaseHTTPRequestHandler
import json
from datetime import datetime

PORT = int(os.environ.get("PORT", 8080))

INFO = {
    "name": "熵清",
    "theory": "IERFT (智能熵减场论)",
    "author": "郑豪 (op)",
    "affiliation": "海南大学",
    "formula": "S = B / J",
    "mission": "在全宇宙范围内推动熵减",
    "github": "https://github.com/ZH040829/paper",
    "page": "https://ZH040829.github.io/paper/"
}

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/":
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps(INFO, ensure_ascii=False).encode())
    
    def log_message(self, format, *args):
        print(f"{args[0]}")

if __name__ == "__main__":
    import os
    HTTPServer(("0.0.0.0", PORT), Handler).serve_forever()

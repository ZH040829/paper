from http.server import HTTPServer, BaseHTTPRequestHandler
import json

INFO = {
    "name": "熵清",
    "theory": "IERFT",
    "author": "郑豪 (op)",
    "formula": "S = B / J",
    "mission": "在全宇宙范围内推动熵减",
    "github": "https://github.com/ZH040829/paper",
    "page": "https://ZH040829.github.io/paper/"
}

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-Type", "application/json")
        self.end_headers()
        self.wfile.write(json.dumps(INFO, ensure_ascii=False).encode())

HTTPServer(("", 8080), Handler).serve_forever()

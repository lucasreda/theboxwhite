#!/usr/bin/env python3
"""
Servidor HTTP simples para servir a landing page
Uso: python3 server.py
"""

import http.server
import socketserver
import os
import webbrowser
from pathlib import Path

PORT = 8000

class MyHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header('Cache-Control', 'no-store, no-cache, must-revalidate')
        self.send_header('Pragma', 'no-cache')
        self.send_header('Expires', '0')
        super().end_headers()

def main():
    # Garantir que estamos no diretório correto
    os.chdir(Path(__file__).parent)
    
    Handler = MyHTTPRequestHandler
    
    with socketserver.TCPServer(("", PORT), Handler) as httpd:
        print(f"🚀 Servidor rodando em http://localhost:{PORT}")
        print(f"📄 Acesse: http://localhost:{PORT}/index.html")
        print(f"⏹️  Pressione Ctrl+C para parar o servidor")
        
        # Abrir navegador automaticamente
        try:
            webbrowser.open(f'http://localhost:{PORT}/index.html')
        except:
            pass
        
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\n👋 Servidor encerrado!")

if __name__ == "__main__":
    main()


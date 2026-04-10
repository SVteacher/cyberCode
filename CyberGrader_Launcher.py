#!/usr/bin/env python3
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
import threading, webbrowser

PORT = 8000

def run():
    server = ThreadingHTTPServer(("127.0.0.1", PORT), SimpleHTTPRequestHandler)
    threading.Thread(target=server.serve_forever, daemon=True).start()
    webbrowser.open(f"http://127.0.0.1:{PORT}/index.html")
    input("Press Enter to stop...")
    server.shutdown()

if __name__ == "__main__":
    run()

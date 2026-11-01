#!/usr/bin/env python3
"""Minimaler lokaler Server für den Pitch Timer. Lauscht ausschließlich auf 127.0.0.1."""
import functools
import http.server
import os
import sys
import threading
import webbrowser

HOST = "127.0.0.1"
# Fester Port zuerst: localStorage hängt am Port, die Einstellungen bleiben so erhalten.
PORTS = range(8765, 8776)


class Handler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header("Cache-Control", "no-store")
        super().end_headers()

    def log_message(self, *args):
        pass


class Server(http.server.ThreadingHTTPServer):
    # Unter Windows erlaubt SO_REUSEADDR doppelte Belegung, dann griffe das Ausweichen auf den nächsten Port nicht.
    allow_reuse_address = os.name != "nt"


def bind():
    handler = functools.partial(Handler, directory=os.path.dirname(os.path.abspath(__file__)))
    for port in PORTS:
        try:
            return Server((HOST, port), handler)
        except OSError:
            continue
    sys.exit(f"Kein freier Port zwischen {PORTS[0]} und {PORTS[-1]} gefunden.")


def main():
    server = bind()
    url = f"http://{HOST}:{server.server_address[1]}/"
    print(f"Pitch Timer läuft auf {url} (Beenden mit Strg+C)", flush=True)
    if "--no-browser" not in sys.argv:
        threading.Timer(0.2, webbrowser.open, [url]).start()
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        pass
    finally:
        server.server_close()


if __name__ == "__main__":
    main()

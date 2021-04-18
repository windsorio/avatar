from http.server import BaseHTTPRequestHandler
from .robohash import Robohash


class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        hash = self.path
        rh = Robohash(hash)
        rh.assemble(roboset="set1", sizex=300, sizey=300)
        self.send_response(200)
        self.send_header("Content-type", "image/png")
        self.end_headers()
        rh.img.save(self.wfile, format="png")
        return

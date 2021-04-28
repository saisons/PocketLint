from http.server import HTTPServer, BaseHTTPRequestHandler

import createPocketLint

class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        printer_buffer = []
        def printer(*line_fragments):
            line = " ".join(line_fragments)
            printer_buffer.append(line)
        createPocketLint.main(printer)
        self.send_response(200)
        self.end_headers()
        for line in printer_buffer:
            self.wfile.write(line.encode()+b'\r\n')


httpd = HTTPServer(('0.0.0.0', 8000), SimpleHTTPRequestHandler)
httpd.serve_forever()

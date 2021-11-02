from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse
import sys, getopt, os, yaml
import re
import json

class TestServerHandler(BaseHTTPRequestHandler):
    config = {} 

    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "application/json")
        self.end_headers()

        o = urlparse(self.path)

        for key, routes in self.config["catalog"].items():
            
            if not re.search(key, o.query):
                continue
            
            for productapi in routes:
                if productapi["route"] == o.path:
                    response_body = open(os.getcwd() + "/" + productapi["data"], "r")
                    self.wfile.write(bytes(response_body.read(), "utf-8"))
                    response_body.close()
                    return
        
        
    def do_DELETE(self):
        self.send_response(200)
        self.send_header("Content-type", "application/json")
        self.end_headers()

        content_length = int(self.headers["content-length"])
        request_body = self.rfile.read(content_length)
        print(request_body)

        response_body = json.dumps({"sucess": True, "message": ""}, ensure_ascii=False)
        self.wfile.write(bytes(response_body, "utf-8"))
        return

def run(argv):
    port = 8081
    config_file = os.getcwd() + "/routes.yml"
    try:
        opts, args = getopt.getopt(argv, "p:f:", ["port=", "file="])
    except getopt.GetoptError:
        print('server.py -f <config_file>')
        sys.exit(2)

    for opt, arg in opts:
        if opt in ("-p", "--port"):
            port = arg
        elif opt in ("-f", "--file"):
            config_file = arg

    with open(config_file, "r") as stream:
        try:
            parsed_yaml=yaml.safe_load(stream)
            print("Test server running on port", port)
            TestServerHandler.config = parsed_yaml
            webServer = HTTPServer(("localhost", int(port)), TestServerHandler)
            try:
                webServer.serve_forever()
            except KeyboardInterrupt:
                pass
            webServer.server_close()
            print("Server stopped.")
        except yaml.YAMLError as exc:
            print(exc)


if __name__ == "__main__":
    run(sys.argv[1:])

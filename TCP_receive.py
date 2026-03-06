import socketserver
from getInfo import updateInfo


# ip = "192.168.0.124"
ip = "0.0.0.0"
port = 65432

class MyTCPHandler(socketserver.StreamRequestHandler):

    def handle(self):
        # self.rfile is a file-like object created by the handler.
        # We can now use e.g. readline() instead of raw recv() calls.
        # We limit ourselves to 10000 bytes to avoid abuse by the sender.
        self.data = self.rfile.readline(10000).rstrip()
        print(f"{self.client_address[0]} wrote:")
        print(self.data.decode("utf-8"))

        response = "bad_request"
        if self.data.decode("utf-8") == "request_status":
            response = updateInfo()

        # Likewise, self.wfile is a file-like object used to write back
        # to the client
        # self.wfile.write(self.data.upper())
        self.wfile.write(bytes(response, "utf-8"))


with socketserver.TCPServer((ip, port), MyTCPHandler) as server:
    # Activate the server; this will keep running until you
    # interrupt the program with Ctrl-C
    server.serve_forever()
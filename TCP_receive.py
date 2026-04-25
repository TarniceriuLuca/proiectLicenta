import socketserver
import threading
from getInfo import updateInfo


# ip = "192.168.0.124"
ip = "0.0.0.0"
port = 65432

class MyTCPHandler(socketserver.StreamRequestHandler):

    def stop_server(server):
        server.shutdown()

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
        if self.data.decode("utf-8") == "shutdown":
            t1 = threading.Thread(target=server.shutdown)
            t1.start()
            response = "shutting down server"
            t1.join()


        self.wfile.write(bytes(response, "utf-8"))



class Server(socketserver.TCPServer):
    def run(self):
        try:
            self.serve_forever()
        except KeyboardInterrupt:
            pass
        finally:
            self.server_close()

server = Server((ip, port), MyTCPHandler)
server.run()


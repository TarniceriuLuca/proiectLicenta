import socketserver, socket
import threading
import sys
from getInfo import updateInfo


ip = "0.0.0.0"
port = 65432


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock.bind((ip, port))
    while(True):
        sock.listen()
        conn, addr = sock.accept()
        print(addr)
        with conn:
            while(True):
                data = conn.recv(1024)
                print(data)
                if not data:
                    break
                response = "bad_request"
                if data.decode("utf-8") == "request_status":
                    response = updateInfo()
                if data.decode("utf-8") == "shutdown":
                    conn.sendall(bytes("shutdonwOK", "utf-8"))
                    sock.shutdown(socket.SHUT_RDWR)
                    sock.close()
                    sys.exit()
                print(response)
                conn.sendall(bytes(response, "utf-8"))

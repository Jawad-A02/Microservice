from socket import *
import os.path
import time


PORT = 3000
SERVER = "127.0.0.1"
ADDR = (SERVER, PORT)                        # initializing constant values

server = socket(AF_INET, SOCK_STREAM)
server.bind(ADDR)                            # binding server



# this is only a test to see if the request can be sent and how the server should respond to the request expected
# The program will keep going until the client sends the disconnect msg
def connect():
    """Connects with a client"""
    print("connecting")
    server.listen(1)
    conn, addr = server.accept()
    print("connected")
    connected = True
    while connected:
        msg = conn.recv(2048).decode()
        if not msg:
            break
        check = str(check_up(msg))
        if check == "Disconnect":
            break
        conn.send(check.encode())
        time.sleep(2)
    conn.close()


def check_up(file_name):
    """checks if a file exist within directory"""
    if not os.path.exists(file_name):
        return False
    else:
        return True


if __name__ == "__main__":
    connect()

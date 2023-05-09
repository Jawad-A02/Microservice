from socket import *

PORT = 3000
SERVER = "127.0.0.1"
ADDR = (SERVER, PORT)                           # initializing constant values

client = socket(AF_INET, SOCK_STREAM)
client.connect(ADDR)                            # connecting to server


def check_file():
    """check if a file name exists within directory"""
    while True:
        file_name = input("what file are you looking for? or press 1 to cancel")
        if file_name == "1":
            break
        client.send(file_name.encode())
        response = client.recv(2048).decode()
        if response == "True":
            print(f"{file_name} exists ")
        else:
            print(f"It doesn't exist")
    client.send("Disconnect".encode())

if __name__ == "__main__":
    check_file()
# server.py
import socket

# Server configuration
HOST = input("Your server ip address?\n") #enter your host ip address
PORT = 2109  # port

def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((HOST, PORT))
    server_socket.listen(1)  
    print(f"Server listening on {HOST}:{PORT}...")

    while True:
        conn, addr = server_socket.accept()
        print(f"Connection established with {addr}")

        
        filename = b""
        while True:
            byte = conn.recv(1)
            if byte == b'\n':  
                break
            filename += byte
        filename = filename.decode('utf-8')  
        print(f"Receiving file: {filename}")

        
        with open(filename, 'wb') as file:
            while True:
                data = conn.recv(1024)
                if not data:  
                    break
                file.write(data)

        print(f"File '{filename}' received and saved in the server folder.")
        conn.close()  
        print(f"Connection with {addr} closed.")

if __name__ == "__main__":
    start_server()

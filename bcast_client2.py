import socket
import threading
import sys

def receive_message(client_socket):
    """Continuously listens for messages from the server."""
    while True:
        try:
            message = client_socket.recv(1024).decode()
            if not message:
                break
            print(f"\n{message}")
            sys.stdout.write("Client: ")
            sys.stdout.flush()
        except:
            break
    print("\nDisconnected from the server.")

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('127.0.0.1', 5000))
print("Connected to the Server! Type 'exit' to disconnect.")

# Handle username entry
while True:
    response = client_socket.recv(1024).decode()
    print(response, end="")
    username = input("").strip()
    client_socket.send(username.encode())
    response = client_socket.recv(1024).decode()  # Wait for server confirmation
    if "ERROR: Username already taken" in response:
        print(response)
    else:
        print(f"Welcome, {username}!")  # Immediate feedback for the user
        break  # Username accepted

# Start receiving messages in a separate thread
receive_thread = threading.Thread(target=receive_message, args=(client_socket,))
receive_thread.daemon = True
receive_thread.start()

# Main input loop with immediate prompt
sys.stdout.write("Client: ")  # Show prompt right after username acceptance
sys.stdout.flush()
while True:
    message = input("").strip()  # Input without prepending "Client: " again
    if message.lower() == "exit":
        print("Disconnecting from the chat...")
        client_socket.close()
        break
    client_socket.send(message.encode())
    sys.stdout.write("Client: ")  # Show prompt after sending message
    sys.stdout.flush()
import socket
import threading

# Dictionary to store {username: socket}
clients = {}

def broadcast(message, sender_socket):
    """Send a message to all clients except the sender."""
    for client_socket in clients.values():
        if client_socket != sender_socket:
            try:
                client_socket.send(message.encode())
            except:
                client_socket.close()

def private_msg(sender, recipient, message):
    """Send a private message to a specific client."""
    if recipient in clients:
        try:
            clients[recipient].send(f"{sender} (private): {message}".encode())
        except:
            del clients[recipient]
    else:
        clients[sender].send(f"ERROR: User '{recipient}' not found.".encode())

def handle_client(client_socket, client_addr):
    """Handles messages from a client, supporting both broadcast and private messaging."""
    try:
        # Keep prompting until a unique username is entered
        while True:
            client_socket.send(b"Enter your username: ")
            username = client_socket.recv(1024).decode().strip()
            if username in clients:
                client_socket.send(b"ERROR: Username already taken. Try again.\n")
            else:
                break  # Exit loop if username is unique

        # Add the client to the dictionary and notify everyone
        clients[username] = client_socket
        print(f"User '{username}' connected!")
        client_socket.send(f"Welcome, {username}!".encode())  # Send welcome to the joining client
        broadcast(f"{username} has joined the chat!", client_socket)  # Notify others

        # Main loop to handle messages from this client
        while True:
            message = client_socket.recv(1024).decode()
            if not message:
                break

            if message.lower() == "exit":
                break

            if message.startswith("@"):  # Private message format: @username message
                try:
                    recipient, private_message = message[1:].split(" ", 1)
                    private_msg(username, recipient, private_message)
                except ValueError:
                    client_socket.send(b"ERROR: Invalid private message format. Use @username message.")
            else:
                broadcast(f"{username}: {message}", client_socket)  # Broadcast to all other clients

    except Exception as e:
        print(f"Error handling client: {e}")
    finally:
        # Clean up when the client disconnects
        if 'username' in locals():
            print(f"User '{username}' disconnected.")
            clients.pop(username, None)
            broadcast(f"{username} has left the chat!", client_socket)
        client_socket.close()

# Set up the server socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)  # Allow reuse of address
server_socket.bind(('127.0.0.1', 5000))
server_socket.listen(5)
print("Server listening on PORT 5000...")

# Main loop to accept new client connections
while True:
    client_socket, client_addr = server_socket.accept()
    client_thread = threading.Thread(target=handle_client, args=(client_socket, client_addr))
    client_thread.start()
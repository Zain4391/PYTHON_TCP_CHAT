PYTHON_TCP_CHAT

A simple, multi-user TCP chat application built with Python using the socket and threading libraries. This project allows multiple clients to connect to a central server, choose unique usernames, and communicate via broadcast messages or private messages. It’s a great example of socket programming and multi-threading in Python, suitable for learning network programming concepts.
Features

    Multi-Client Support: The server handles multiple clients simultaneously using threading.
    Unique Usernames: Clients must choose a unique username to join the chat.
    Broadcast Messaging: Messages sent by one client are broadcast to all other connected clients.
    Private Messaging: Clients can send private messages using the @username message format.
    Join/Leave Notifications: The server notifies all clients when a user joins or leaves the chat.
    Graceful Disconnection: Clients can exit by typing exit, and the server cleans up resources properly.

Prerequisites

    Python 3.7+: Ensure you have Python installed. You can download it from python.org.
    No additional dependencies are required since the project uses Python’s standard library (socket and threading).

Getting Started
Cloning the Repository

Clone this repository to your local machine:
bash
git clone https://github.com/Zain4391/PYTHON_TCP_CHAT.git
cd PYTHON_TCP_CHAT
Project Structure

    server.py: The server-side script that handles client connections and message broadcasting.
    client.py: The client-side script that connects to the server and allows users to send/receive messages.

Running the Application
1. Start the Server

First, run the server script to start listening for client connections:
bash
python server.py

    The server will bind to 127.0.0.1 on port 5000 by default and print:
    text

    Server listening on PORT 5000...
    If port 5000 is in use, you can change it by modifying the server_socket.bind(('127.0.0.1', 5000)) line in server.py. Make sure to update the client code accordingly.

2. Start the Client(s)

Open a new terminal for each client you want to connect. Run the client script:
bash
python client.py

    The client will connect to 127.0.0.1:5000 and prompt you to enter a username:
    text

Connected to the Server! Type 'exit' to disconnect.
Enter your username: 
If the username is already taken, you’ll be asked to try again. Once a unique username is accepted, you’ll enter the chat:
text

    Welcome, <username>!
    Client: 
    You can now type messages to broadcast to all other clients or send private messages using @username message.

3. Example Interaction

    Server Terminal:
    text

Server listening on PORT 5000...
✅ User 'Zain' connected!
✅ User 'Ali' connected!
❌ User 'Ali' disconnected.
Client Terminal (Zain):
text
Connected to the Server! Type 'exit' to disconnect.
Enter your username: Zain
Welcome, Zain!
Client: Ali has joined the chat!
Client: Ali: Hello
Client: Hi
Client: Ali has left the chat!
Client: 
Client Terminal (Ali):
text

    Connected to the Server! Type 'exit' to disconnect.
    Enter your username: Zain
    ERROR: Username already taken. Try again.
    Enter your username: Ali
    Welcome, Ali!
    Client: Hello
    Client: Zain: Hi
    Client: exit
    Disconnecting from the chat...

Usage

    Broadcast Messages: Simply type a message and press Enter to send it to all other clients.
    Private Messages: Use the format @username message to send a private message to a specific user. Example: @Zain Hey there!
    Disconnect: Type exit to leave the chat. The server will notify others of your departure.

Code Overview
Server (server.py)

    Uses socket to create a TCP server listening on 127.0.0.1:5000.
    Handles multiple clients with threading.
    Maintains a clients dictionary mapping usernames to their sockets.
    Broadcasts messages to all clients except the sender and supports private messaging.

Client (client.py)

    Connects to the server and prompts for a username.
    Uses a separate thread to listen for incoming messages while allowing the user to type messages.
    Handles both broadcast and private messages, displaying them in the terminal.

Troubleshooting

    Address Already in Use Error: If you see OSError: [Errno 98] Address already in use, the port 5000 is occupied. Either kill the process using the port (sudo lsof -i :5000 on Linux/macOS or netstat -aon | findstr :5000 on Windows) or change the port in both server.py and client.py.
    Connection Refused: Ensure the server is running before starting the client, and verify the IP/port match in both scripts.
    No Prompt After Username: If a client doesn’t see the Client: prompt after entering a username, ensure the server is sending the welcome message and the client’s receive thread is running.

Future Improvements

    Add a graphical user interface (GUI) using a library like tkinter or PyQt.
    Implement message encryption for secure communication.
    Support file sharing between clients.
    Add a command to list all online users (e.g., /users).

Contributing

Contributions are welcome! If you’d like to improve this project:

    Fork the repository.
    Create a new branch for your feature (git checkout -b feature-name).
    Make your changes and commit them (git commit -m "Add feature").
    Push to your branch (git push origin feature-name).
    Open a pull request.

Acknowledgments

    Inspired by various TCP chat implementations on GitHub, such as those by rahulMishra05 and Rishija.
    Built as a learning project to explore socket programming and multi-threading in Python.


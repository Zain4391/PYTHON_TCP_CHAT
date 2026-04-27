# PYTHON_TCP_CHAT

![Python](https://img.shields.io/badge/Python-3.7%2B-blue?logo=python&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-green)
![Platform](https://img.shields.io/badge/Platform-Linux%20%7C%20macOS%20%7C%20Windows-lightgrey)

A simple, multi-user TCP chat application built with Python using the `socket` and `threading` standard libraries. Multiple clients can connect to a central server, choose unique usernames, and communicate via broadcast or private messages. It is a practical example of socket programming and multi-threading in Python, well-suited for learning network programming concepts.

---

## Features

- **Multi-Client Support** - The server handles multiple clients simultaneously using threads.
- **Unique Usernames** - Clients must choose a unique username to join the chat.
- **Broadcast Messaging** - Messages sent by one client are broadcast to all other connected clients.
- **Private Messaging** - Send private messages using the `@username message` format.
- **Join/Leave Notifications** - All clients are notified when a user joins or leaves the chat.
- **Graceful Disconnection** - Clients can exit by typing `exit`; the server cleans up resources automatically.

---

## Prerequisites

- **Python 3.7+** - Download from [python.org](https://www.python.org/downloads/).
- No additional dependencies - only Python's built-in `socket` and `threading` modules are used.

---

## Getting Started

### Clone the Repository

```bash
git clone https://github.com/Zain4391/PYTHON_TCP_CHAT.git
cd PYTHON_TCP_CHAT
```

### Project Structure

```
PYTHON_TCP_CHAT/
├── broadcast_server.py   # Server script - handles connections and message routing
├── bcast_client.py       # Client script (instance 1)
├── bcast_client2.py      # Client script (instance 2)
├── bcast_client3.py      # Client script (instance 3)
├── client_files/         # Additional client resources
├── server_files/         # Additional server resources
├── LICENSE
└── readme.md
```

---

## Running the Application

### 1. Start the Server

```bash
python broadcast_server.py
```

The server binds to `127.0.0.1:5000` by default and prints:

```
Server listening on PORT 5000...
```

> **Note:** If port `5000` is already in use, change the port in the `server_socket.bind(('127.0.0.1', 5000))` line in `broadcast_server.py` and update the corresponding `client_socket.connect(...)` line in the client scripts.

### 2. Start the Client(s)

Open a new terminal for each client and run one of the client scripts:

```bash
python bcast_client.py
```

The client connects to `127.0.0.1:5000` and prompts for a username:

```
Connected to the Server! Type 'exit' to disconnect.
Enter your username:
```

If the username is already taken, you will be asked to try again. Once accepted:

```
Welcome, <username>!
Client:
```

### 3. Example Interaction

**Server terminal:**
```
Server listening on PORT 5000...
User 'Zain' connected!
User 'Ali' connected!
User 'Ali' disconnected.
```

**Client terminal - Zain:**
```
Connected to the Server! Type 'exit' to disconnect.
Enter your username: Zain
Welcome, Zain!

Ali has joined the chat!

Ali: Hello
Hi

Ali has left the chat!
Client:
```

**Client terminal - Ali:**
```
Connected to the Server! Type 'exit' to disconnect.
Enter your username: Zain
ERROR: Username already taken. Try again.
Enter your username: Ali
Welcome, Ali!

Client: Hello

Zain: Hi
Client: exit
Disconnecting from the chat...
```

---

## Usage

| Action | How to do it |
|---|---|
| **Broadcast message** | Type a message and press `Enter` |
| **Private message** | Type `@username message` (e.g., `@Zain Hey there!`) |
| **Disconnect** | Type `exit` |

---

## Code Overview

### Server (`broadcast_server.py`)

- Creates a TCP server socket listening on `127.0.0.1:5000`.
- Spawns a new thread for each incoming client connection.
- Maintains a `clients` dictionary mapping usernames to their sockets.
- Supports broadcast messaging (to all clients except the sender) and private messaging (`@username`).

### Client (`bcast_client.py`, `bcast_client2.py`, `bcast_client3.py`)

- Connects to the server and handles the username negotiation flow.
- Spawns a background daemon thread to receive and display incoming messages.
- Main thread handles user input and sends messages to the server.

---

## Troubleshooting

| Problem | Solution |
|---|---|
| `OSError: [Errno 98] Address already in use` | Port `5000` is occupied. Find and stop the process using the port, or change the port in both server and client scripts. |
| `Connection refused` | Ensure the server is running before starting a client, and that the IP/port match in both scripts. |
| No `Client:` prompt after entering username | Verify the server is sending the welcome message and that the client's receive thread started correctly. |

---

## Future Improvements

- Add a graphical user interface (GUI) using `tkinter` or `PyQt`.
- Implement end-to-end message encryption for secure communication.
- Support file sharing between clients.
- Add a `/users` command to list all currently online users.

---

## Contributing

Contributions are welcome! To contribute:

1. Fork the repository.
2. Create a new branch: `git checkout -b feature-name`
3. Commit your changes: `git commit -m "Add feature"`
4. Push to your branch: `git push origin feature-name`
5. Open a pull request.

---

## License

This project is licensed under the [MIT License](LICENSE).

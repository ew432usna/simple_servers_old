import socket
import os

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind(('0.0.0.0', 8880))
    s.listen()
    while True:
        (conn, addr) = s.accept()
        print('Connected to', addr)
        data = conn.recv(1024)
        requested_file = data.decode('utf-8').strip()
        if requested_file == "/":
            requested_file = "hello_world.html"
        if os.path.isfile(requested_file):
            with open(requested_file) as f:
                conn.sendall(f.read().encode('utf-8'))
        else:
            conn.sendall("file not found".encode('utf-8'))
        conn.close()

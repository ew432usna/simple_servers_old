import socket

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind(('0.0.0.0', 80))
    s.listen()
    while True:
        (conn, addr) = s.accept()
        print('Connected to', addr)
        data = conn.recv(1024)
        conn.sendall(data)
        conn.close()

import socket
import os

hit_count = 0

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind(('0.0.0.0',80))
    s.listen()
    while True:
        (conn, addr) = s.accept()
        print("Connection from", addr)
        data = conn.recv(1024)
        requested_file = data.decode('ascii').strip()

        # ---- Begin Controller ----
        # only allow visitors from USNA
        if addr[0].startswith("136"):
            #                                       [----- this is the view -----------------]
            http_response = "HTTP/1.1 200 OK\r\n\r\nWelcome, you are visitor #%d" % hit_count
            hit_count += 1 # keep track of how many visitors we get
        else:
            http_response = "HTTP/1.1 403 FORBIDDEN\r\n\r\nUSNA Only!"
        # ---- End Controller ----
        
        conn.sendall(http_response.encode('ascii'))  
        conn.close()
        print("\tclosed")

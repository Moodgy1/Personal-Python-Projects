import socket

ip = input("Enter Your IP Address. ")
port = int(input("Enter the Port you want check. "))

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # UDP socket
sock.settimeout(3)
try:
    sock.sendto(b"ping", (ip, port))
    data, _ = sock.recvfrom(1024)  # Wait for a response
    print(f"UDP port {port} is open on {ip} Response: {data}")
except socket.timeout:
    print(f"UDP port {port} is closed or not responding on {ip}")

sock.close()
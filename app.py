import socket

FR24_FEEDER_IP = '172.17.0.1'  # Replace with the IP address of your feeder
# FR24_FEEDER_IP = '127.0.0.1'  # Replace with the IP address of your feeder
FR24_FEEDER_PORT = 30003

print(FR24_FEEDER_IP)
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((FR24_FEEDER_IP, FR24_FEEDER_PORT))

while True:
    data = sock.recv(1024)
    if not data:
        break

    # Parse the ADS-B message using pyModeS
    msg = pyModeS.df(data)

    # Print the parsed message
    print(msg)


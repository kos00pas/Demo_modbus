from pymodbus.client import ModbusTcpClient
import socket
import time



# Get IP Address
hostname = socket.gethostname()
IPAddr = "172.20.246.249" #socket.gethostbyname(hostname)


# Connect with OpenPLC runtime
client = ModbusTcpClient(IPAddr)
isConnected = client.connect()
print(isConnected)

while True:
    time.sleep(0.1)
    client.write_coil(18, True, 1)   # Rotate right stick
    client.write_coil(18, False, 1) 

    client.write_coil(14, True, 1)   # Rotate left stick
    client.write_coil(14, False, 1)  

    client.write_coil(16, True, 1)   # Go down right stick
    client.write_coil(11, True, 1)   # Go down left stick

    client.write_coil(8, True, 1)   # Keep conveyors going
    client.write_coil(10, True, 1)   
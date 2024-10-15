from pymodbus.client import ModbusTcpClient
import time

# Define the IP Address for the Modbus server
IPAddr = "172.20.235.59"
slave_id = 1  # Specify the slave ID

# Connect with OpenPLC runtime
client = ModbusTcpClient(IPAddr)
isConnected = client.connect()
print("Connected to Modbus server:", isConnected)

if isConnected:
    try:
            # Read coils from %QX100.0 to %QX103.0 (total 25 coils)
            coil_start_address = 100  # Starting address for %QX100.0
            coil_count = 25           # Total coils to read

            # Loop to repeatedly read coils
            time.sleep(1)  # Adjust the delay as needed

            # Read the specified range of coils with the slave ID
            response = client.read_coils(0, coil_count, slave=slave_id)
            if response.isError():
                print("Error reading coils")
            else:
                # Display the states of the coils
                print("Coil states:")
                for i, state in enumerate(response.bits):
                    coil_address = coil_start_address + i
                    print(f"Coil %QX{coil_address}: {'ON' if state else 'OFF'}")

    except KeyboardInterrupt:
        print("Process interrupted by user.")
    finally:
        client.close()
        print("Connection closed.")
else:
    print("Failed to connect to Modbus server.")

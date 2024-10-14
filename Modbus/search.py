from pymodbus.client import ModbusTcpClient

# Set the target IP for the PLC
target_ip = "192.168.0.8"  # OpenPLC Runtime
port = 502  # Modbus TCP default port


# Function to check if Modbus communication is possible
def check_modbus(ip, port):
    client = ModbusTcpClient(ip, port=port)
    try:
        if client.connect():
            print(f"Modbus communication established with {ip}:{port}")
            return client
        else:
            print(f"No Modbus communication with {ip}:{port}")
            client.close()
    except Exception as e:
        print(f"Error connecting to {ip}:{port}: {e}")
        client.close()
    return None


# Function to read all coils and print a summary line for each chunk if it contains any True values
def read_all_coils(client):
    starting_address = 0
    chunk_size = 100  # Number of coils to read in each request

    while starting_address < 65535:
        try:
            # Read a chunk of coils
            response = client.read_coils(starting_address, chunk_size)
            if response is None or response.isError():
                print(f"Reached the end of available coils or encountered an error at address {starting_address}.")
                break

            # Check if any coil in the chunk is True
            if any(response.bits):  # Only proceed if there's at least one True value
                end_address = starting_address + len(response.bits) - 1
                # Prepare a formatted list with True/False values for the chunk
                coil_states = ['True' if bit else 'False' for bit in response.bits]
                # Print the address range and the states
                print(f"Coils {starting_address} to {end_address}: {coil_states}")

            starting_address += chunk_size  # Move to the next chunk
        except Exception as e:
            print(f"Error reading coils starting at {starting_address}: {e}")
            break


def read_all_discrete_inputs(client):
    starting_address = 0
    chunk_size = 100  # Number of discrete inputs to read in each request
    seen_addresses = set()  # Keep track of addresses that have been processed

    while starting_address < 65535:
        try:
            # Read a chunk of discrete inputs
            response = client.read_discrete_inputs(starting_address, chunk_size)
            if response is None or response.isError():
                print(f"Reached the end of available discrete inputs or encountered an error at address {starting_address}.")
                break

            # Check if any discrete input in the chunk is True and print it only if not already seen
            for i, bit in enumerate(response.bits):
                addr = starting_address + i
                if bit and addr not in seen_addresses:
                    print(f"Discrete Input at {addr}: True")
                    seen_addresses.add(addr)  # Mark this address as processed

            starting_address += chunk_size  # Move to the next chunk
        except Exception as e:
            print(f"Error reading discrete inputs starting at {starting_address}: {e}")
            break


def read_all_input_registers(client):
    starting_address = 0
    chunk_size = 100  # Number of input registers to read in each request

    while starting_address < 65535:
        try:
            # Read a chunk of input registers
            response = client.read_input_registers(starting_address, chunk_size)
            if response is None or response.isError():
                print(
                    f"Reached the end of available input registers or encountered an error at address {starting_address}.")
                break

            # Check if any input register in the chunk is non-zero and print it
            for i, value in enumerate(response.registers):
                if value != 0:  # Only print non-zero values
                    print(f"Input Register at {starting_address + i}: {value}")

            starting_address += chunk_size  # Move to the next chunk
        except Exception as e:
            print(f"Error reading input registers starting at {starting_address}: {e}")
            break


# Check Modbus connection and read all coils if connected
client = check_modbus(target_ip, port)
if client:
    read_all_coils(client)
    read_all_discrete_inputs(client)
    read_all_input_registers(client)
    client.close()
# Total Coils: 25
# %QX100.0, %QX100.1, %QX100.2, %QX100.3, %QX100.4, %QX100.5, %QX100.6, %QX100.7
# %QX101.0, %QX101.1, %QX101.2, %QX101.3, %QX101.4, %QX101.5, %QX101.6, %QX101.7
# %QX102.0, %QX102.1, %QX102.2, %QX102.3, %QX102.4, %QX102.5, %QX102.6, %QX102.7
# %QX103.0
#Total Discrete Inputs: 3
# %IX100.0, %IX100.1, %IX100.2
# Total Input Registers: 1
# %IW100

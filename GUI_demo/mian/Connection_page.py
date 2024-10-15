import tkinter as tk
import ipaddress
from pymodbus.client import ModbusTcpClient
import time


class Connection_page(tk.Frame):
    def __init__(self, parent, database):
        super().__init__(parent)

        label = tk.Label(self, text="This is Page 1")
        label.pack()

        self.DATA = database
        self.DATA.connection_ip = tk.Entry(self, width=20)
        self.DATA.connection_ip.pack(pady=10)

        button = tk.Button(self, text="Get Input", command=self.get_ip_and_connect)
        button.pack(pady=5)

        self.result_label = tk.Label(self, text="")
        self.result_label.pack()

    def get_ip_and_connect(self):
        target_ip = self.DATA.connection_ip.get()

        if not self.is_valid_ip(target_ip):
            self.result_label.config(text="Invalid IP address format.", fg="red")
            print("Invalid IP address format.")
            return None

        port = 502
        slave_id = 1  # Specify the slave ID

        self.DATA.client = ModbusTcpClient(target_ip, port=port)

        try:
            if self.DATA.client.connect():
                self.result_label.config(text=f"Connected to {target_ip}:{port}", fg="green")
                print(f"Modbus communication established with {target_ip}:{port}")
                # Call the function for post-connection actions
                self.post_connect_action(self.DATA.client)
                return self.DATA.client
            else:
                self.result_label.config(text=f"Connection failed to {target_ip}:{port}", fg="red")
                print(f"No Modbus communication with {target_ip}:{port}")
                self.DATA.client.close()
        except Exception as e:
            self.result_label.config(text=f"Error: {e}", fg="red")
            print(f"Error connecting to {target_ip}:{port}: {e}")
            self.DATA.client.close()

        return None

    def is_valid_ip(self, ip):
        try:
            ipaddress.ip_address(ip)
            return True
        except ValueError:
            return False




    # Function to read and print the desired coil states and discrete inputs
    def post_connect_action(self, client):
        print("Running post-connection actions...")
        slave_id = 1  # Specify the slave ID

        if client.connect():
            try:
                # Read coils (total of highest index + 1)
                response = client.read_coils(0, max(self.DATA.coil_addresses.values()) + 1, slave=slave_id)
                if response.isError():
                    print("Error reading coils")
                else:
                    print("Coil states:")
                    for name, address in self.DATA.coil_addresses.items():
                        state = response.bits[address]
                        print(f"{name} (Coil %QX{100 + address // 8}.{address % 8}): {'ON' if state else 'OFF'}")

                # Read discrete inputs (total of highest index + 1)
                response = client.read_discrete_inputs(0, max(self.DATA.discrete_input_addresses.values()) + 1, slave=slave_id)
                if response.isError():
                    print("Error reading discrete inputs")
                else:
                    print("Discrete Input states:")
                    for name, address in self.DATA.discrete_input_addresses.items():
                        state = response.bits[address]
                        print(f"{name} (Discrete %IX{100 + address // 8}.{address % 8}): {'ON' if state else 'OFF'}")

                # Read input register at %IW100
                response = client.read_input_registers(0, 1, slave=slave_id)
                if response.isError():
                    print("Error reading input register")
                else:
                    print(f"Weight (Input Register %IW100): {response.registers[0]}")

            except Exception as e:
                print(f"Error during post-connection actions: {e}")
            finally:
                client.close()
        else:
            print("Unable to connect to the client")

            print("Running post-connection actions...")
            slave_id = 1  # Specify the slave ID

            if client.connect():
                try:
                    # Read coils from %QX100.0 to %QX103.0 (total 25 coils)
                    coil_start_address = 100  # Starting address for %QX100.0
                    coil_count = 25  # Total coils to read

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
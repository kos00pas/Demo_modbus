import tkinter as tk
import ipaddress
from pymodbus.client import ModbusTcpClient
import time


class Connection_page(tk.Frame):
    def __init__(self, parent, database):
        super().__init__(parent)

        self.configure(bg="gray")
        self.DATA = database

        # Frame to hold connection_ip and buttons side by side
        top_frame = tk.Frame(self, bg="gray")
        top_frame.pack(pady=10)

        label_ip = tk.Label(top_frame, text="Add IP:")
        label_ip.pack(side="left", padx=5)

        self.DATA.connection_ip = tk.Entry(top_frame, width=20)
        self.DATA.connection_ip.pack(side="left", padx=10)

        button_get = tk.Button(top_frame, text="Get Input", command=self.get_ip_and_connect)
        button_get.pack(side="left", padx=10)

        self.button_refresh = tk.Button(top_frame, text="Refresh Values", command=self.refresh_values, state=tk.DISABLED)
        self.button_refresh.pack(side="left", padx=10)

        # Label for connection result
        self.result__connection_label = tk.Label(self, text="")
        self.result__connection_label.pack(pady=(10, 5))  # Add vertical padding: 10 pixels above, 5 below

        # Text widget for found devices
        self.result_found_dec_text = tk.Text(self, bg="black", wrap="word", height=35, width=50)
        self.result_found_dec_text.pack(pady=(5, 10))

        # Tag configuration for blue-colored categories
        self.result_found_dec_text.tag_configure("category", foreground="red")
        self.result_found_dec_text.tag_configure("devices", foreground="green")

    def get_ip_and_connect(self):
        target_ip = self.DATA.connection_ip.get()

        if not self.is_valid_ip(target_ip):
            self.result__connection_label.config(text="Invalid IP address format.", fg="red")
            print("Invalid IP address format.")
            return None

        port = 502
        slave_id = 1  # Specify the slave ID

        self.DATA.client = ModbusTcpClient(target_ip, port=port)

        try:
            if self.DATA.client.connect():
                self.result__connection_label.config(text=f"Connected to {target_ip}:{port}", fg="green")
                print(f"Modbus communication established with {target_ip}:{port}")
                # Call the function for post-connection actions
                self.refresh_values()
                return self.DATA.client
            else:
                self.result__connection_label.config(text=f"Connection failed to {target_ip}:{port}", fg="red")
                self.result_found_dec_text.delete("1.0", tk.END)  # Clear previous content
                self.button_refresh.config(state=tk.DISABLED)
                print(f"No Modbus communication with {target_ip}:{port}")
                self.DATA.client.close()
        except Exception as e:
            self.result__connection_label.config(text=f"Error: {e}", fg="red")
            self.result_found_dec_text.delete("1.0", tk.END)  # Clear previous content

            print(f"Error connecting to {target_ip}:{port}: {e}")
            self.DATA.client.close()
            self.button_refresh.config(state=tk.DISABLED)

        return None


    def is_valid_ip(self, ip):
        try:
            ipaddress.ip_address(ip)
            return True
        except ValueError:
            self.button_refresh.config(state=tk.DISABLED)
            return False


    # Function to read and print the desired coil states, discrete inputs, and weight register
    def refresh_values(self):
        print("Running post-connection actions...")
        slave_id = 1  # Specify the slave ID
        found_devices = {}
        client = self.DATA.client
        if client.connect():
            try:




                self.button_refresh.config(state=tk.NORMAL)

                # Extract addresses for max calculation
                coil_addresses_only = [addr[0] for addr in self.DATA.coil_addresses.values()]
                discrete_input_addresses_only = [addr[0] for addr in self.DATA.discrete_input_addresses.values()]

                # Read coils (total of highest index + 1)
                response = client.read_coils(0, max(coil_addresses_only) + 1, slave=slave_id)
                if response.isError():
                    print("Error reading coils")
                else:
                    print("Coil states:")
                    found_devices['Coils'] = {}
                    for name, (address, _) in self.DATA.coil_addresses.items():
                        state = response.bits[address]
                        self.DATA.coil_addresses[name][1] = state  # Update the boolean value in the array
                        found_devices['Coils'][name] = 'ON' if state else 'OFF'
                        print(f"{name} (Coil %QX{100 + address // 8}.{address % 8}): {'ON' if state else 'OFF'}")

                # Read discrete inputs (total of highest index + 1)
                response = client.read_discrete_inputs(0, max(discrete_input_addresses_only) + 1, slave=slave_id)
                if response.isError():
                    print("Error reading discrete inputs")
                else:
                    print("Discrete Input states:")
                    found_devices['Discrete Inputs'] = {}
                    for name, (address, _) in self.DATA.discrete_input_addresses.items():
                        state = response.bits[address]
                        self.DATA.discrete_input_addresses[name][1] = state  # Update the boolean value in the array
                        found_devices['Discrete Inputs'][name] = 'ON' if state else 'OFF'
                        print(f"{name} (Discrete %IX{100 + address // 8}.{address % 8}): {'ON' if state else 'OFF'}")

                # Read input register at %IW100
                response = client.read_input_registers(0, 1, slave=slave_id)
                if response.isError():
                    print("Error reading input register")
                else:
                    weight_value = response.registers[0]
                    found_devices['Weight'] = weight_value
                    print(f"Weight (Input Register %IW100): {weight_value}")

                # Update the text widget
                self.result_found_dec_text.config(state=tk.NORMAL)
                self.result_found_dec_text.delete(1.0, tk.END)

                for category, devices in found_devices.items():
                    # Insert category with the 'category' tag for red color
                    self.result_found_dec_text.insert(tk.END, f"\n{category}:\n", "category")
                    if isinstance(devices, dict):
                        for name, state in devices.items():
                            # Insert each device name and state with the 'devices' tag for green color
                            self.result_found_dec_text.insert(tk.END, f"  - {name}: {state}\n", "devices")
                    else:
                        # Insert other entries with the 'devices' tag as well
                        self.result_found_dec_text.insert(tk.END, f"  - {devices}\n", "devices")

                # Make the text widget read-only
                self.result_found_dec_text.config(state=tk.DISABLED)

            except Exception as e:
                print(f"Error during post-connection actions: {e}")
            finally:
                client.close()
        else:
            print("Unable to connect to the client")
            self.button_refresh.config(state=tk.DISABLED)





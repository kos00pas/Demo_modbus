import tkinter as tk
import time

class Manipulation(tk.Frame):
    def __init__(self, parent, database):
        super().__init__(parent)
        self.configure(bg="dark blue")
        self.DATA = database
        self.active_jobs = {}  # Dictionary to track all active jobs by coil name

        # Create the subframes (but don’t populate buttons yet)
        self.create_subframes()


    def create_buttons(self):
            self.for_coil_frame()
            self.for_disc_inp_frame()
            self.for_analog_inp_frame()
            self.for_persistent_manipulation_frame()
            self.for_persistent_destruction_frame()



    def create_subframes(self):
        # Coil Frame
        self.coil_frame = tk.Frame(self, bg="gray", borderwidth=2, relief="groove", padx=10, pady=10)
        self.coil_frame.grid(row=0, column=0, rowspan=2, sticky="nsew", padx=10, pady=10)
        coil_label = tk.Label(self.coil_frame, text="Coil Monitoring")
        coil_label.grid(row=0, column=0, columnspan=4, pady=(0, 10))  # Adjusted for column span

        self.persistent_manipulation_frame = tk.Frame(self, bg="light gray", borderwidth=2, relief="groove", padx=10, pady=10)
        self.persistent_manipulation_frame.grid(row=2, column=0, rowspan=1, sticky="nsew", padx=10, pady=10)
        # Row 0: Persistent Manipulation label and Duration Entry
        persistent_manipulation_label = tk.Label(self.persistent_manipulation_frame, text="Persistent Manipulation",
                              font=("Arial", 14, "bold"))
        persistent_manipulation_label.grid(row=0, column=0, columnspan=3, padx=5, pady=5, sticky="w")

        # Discrete Input Frame
        self.dsc_inp_frame = tk.Frame(self, bg="gray", borderwidth=2, relief="groove", padx=10, pady=10)
        self.dsc_inp_frame.grid(row=0, column=2, sticky="nsew", padx=10, pady=10)
        dsc_inp_label = tk.Label(self.dsc_inp_frame, text="Discrete Input Monitoring")
        dsc_inp_label.pack()

        # Analog Input Frame (Future Frame)
        self.analog_inp_frame = tk.Frame(self, bg="gray", borderwidth=2, relief="groove", padx=10, pady=10)
        self.analog_inp_frame.grid(row=1, column=2, sticky="nsew", padx=10, pady=10)
        analog_inp_label = tk.Label(self.analog_inp_frame, text="Analog Input Monitoring")
        analog_inp_label.pack()

        # Flags for checking if buttons are created in each frame
        self.disc_inp_buttons_created = False
        self.analog_inp_buttons_created = False  # For future use with analog inputs

    def for_coil_frame(self):
        left_row = 1  # Starting row for left column
        center_row = 1  # Starting row for center column
        right_row = 1  # Starting row for right column
        both_row = 1  # Starting row for the fourth column (either both or repeated "left"/"right")

        for name, (address, state) in self.DATA.coil_addresses.items():
            # Check for multiple occurrences or both "left" and "right"
            if name.lower().count("left") > 1 or name.lower().count("right") > 1 or (
                    "left" in name.lower() and "right" in name.lower()):
                column = 3
                row = both_row
                both_row += 1  # Increment row counter for fourth column
            elif "left" in name.lower():
                column = 0
                row = left_row
                left_row += 1  # Increment left column row counter
            elif "right" in name.lower():
                column = 2
                row = right_row
                right_row += 1  # Increment right column row counter
            else:
                column = 1
                row = center_row
                center_row += 1  # Increment center column row counter

            # Create and place the button
            button = tk.Button(
                self.coil_frame,
                text=f"{name}: {'ON' if state else 'OFF'}",
                bg="green" if state else "red",
                command=lambda name=name: self.toggle_coil_state(name)
            )
            button.grid(row=row, column=column, padx=5, pady=5, sticky="ew")
    def for_disc_inp_frame(self):
        for name, (address, state) in self.DATA.discrete_input_addresses.items():

            button = tk.Button(
                self.dsc_inp_frame,
                text=f"{name}: {'ON' if state else 'OFF'}",
                bg="green" if state else "red",
                command=lambda name=name: self.toggle_discrete_input_state(name)
            )
            button.pack(fill=tk.X, padx=5, pady=5)
    def for_analog_inp_frame(self):
        # Ensure buttons are only created once
        if not self.analog_inp_buttons_created:
            # Dictionary to hold analog input button references
            self.analog_inp_buttons = {}

            # Create buttons for each analog input address
            for name, (address, state) in self.DATA.analog_input_addresses.items():
                button = tk.Button(
                    self.analog_inp_frame,
                    text=f"{name}: {state}",  # Display initial state
                    bg="green" if state > 0 else "red",  # Example coloring logic
                    command=lambda name=name: self.toggle_analog_inp_state(name)
                )
                button.pack(fill=tk.X, padx=5, pady=5)
                self.analog_inp_buttons[name] = button  # Store button reference

            # Mark that the analog input buttons have been created
            self.analog_inp_buttons_created = True

    def for_persistent_manipulation_frame(self):
        self.persistent_manipulation_buttons = {}  # Dictionary to store coil buttons by name
        self.analog_input_entries = {}  # Dictionary to store analog input entries by name
        self.analog_input_labels = {}  # Dictionary to store analog input labels by name

        # Row 0: Persistent Manipulation label and Duration/Interval Entry
        main_label = tk.Label(self.persistent_manipulation_frame, text="Persistent Manipulation",
                              font=("Arial", 14, "bold"))
        main_label.grid(row=0, column=0, columnspan=3, padx=5, pady=5, sticky="w")

        # Duration label and entry
        duration_label = tk.Label(self.persistent_manipulation_frame, text="Duration (s):")
        duration_label.grid(row=0, column=3, padx=5, pady=5, sticky="e")
        duration_label.bind("<Button-1>", lambda e: self.save_duration())

        self.duration_entry = tk.Entry(self.persistent_manipulation_frame, width=5)
        self.duration_entry.grid(row=0, column=4, padx=5, pady=5, sticky="w")
        self.duration_entry.insert(0, "15")  # Default value for 10 seconds

        # Interval label and entry
        interval_label = tk.Label(self.persistent_manipulation_frame, text="Interval (ms):")
        interval_label.grid(row=0, column=5, padx=5, pady=5, sticky="e")
        interval_label.bind("<Button-1>", lambda e: self.save_interval())

        self.interval_entry = tk.Entry(self.persistent_manipulation_frame, width=5)
        self.interval_entry.grid(row=0, column=6, padx=5, pady=5, sticky="w")
        self.interval_entry.insert(0, "180")  # Default value for 250 ms

        # Clear All button
        clear_all_button = tk.Button(self.persistent_manipulation_frame, text="Clear All",
                                     command=self.clear_all)
        clear_all_button.grid(row=0, column=7, padx=5, pady=5, sticky="w")

        # Row 1: Column headers for coils and analog inputs
        coil_label = tk.Label(self.persistent_manipulation_frame, text="Coils", font=("Arial", 10, "bold"))
        coil_label.grid(row=1, column=0, columnspan=4, padx=5, pady=5, sticky="nsew")  # Header for coil buttons

        analog_label = tk.Label(self.persistent_manipulation_frame, text="Analog Inputs", font=("Arial", 10, "bold"))
        analog_label.grid(row=1, column=4, columnspan=3, padx=5, pady=5, sticky="nsew")  # Header for analog inputs

        # Persistent Manipulation Buttons (Starting from row 2)
        left_row = 2  # Starting row for left column
        center_row = 2  # Starting row for center column
        right_row = 2  # Starting row for right column
        both_row = 2  # Starting row for the fourth column (either both or repeated "left"/"right")

        for name, _ in self.DATA.coil_addresses.items():
            # Check for multiple occurrences or both "left" and "right"
            if name.lower().count("left") > 1 or name.lower().count("right") > 1 or (
                    "left" in name.lower() and "right" in name.lower()):
                column = 3
                row = both_row
                both_row += 1  # Increment row counter for fourth column
            elif "left" in name.lower():
                column = 0
                row = left_row
                left_row += 1  # Increment left column row counter
            elif "right" in name.lower():
                column = 2
                row = right_row
                right_row += 1  # Increment right column row counter
            else:
                column = 1
                row = center_row
                center_row += 1  # Increment center column row counter

            # Create and place the button
            button = tk.Button(
                self.persistent_manipulation_frame,
                text=name,
                bg="white",
                command=lambda name=name: self.toggle_persistent_manipulation_state(name)
            )
            button.grid(row=row, column=column, padx=5, pady=5, sticky="ew")
            self.persistent_manipulation_buttons[name] = button  # Store button reference

    def for_persistent_destruction_frame(self):
        # Create a new subframe for Persistent Destruction within the main manipulation frame
        self.persistent_destruction_frame = tk.Frame(self, bg="dark red", borderwidth=2, relief="groove", padx=10, pady=5)
        self.persistent_destruction_frame.grid(row=2, column=2, rowspan=2, sticky="nsew", padx=10, pady=5)

        # Add the main label for the destruction frame
        destruction_label = tk.Label(self.persistent_destruction_frame, text="Persistent Destruction",
                                     font=("Arial", 14, "bold"))
        destruction_label.grid(row=0, column=0, padx=5, pady=5, sticky="w")

        # Add six buttons in a vertical arrangement and bind them to specific destruction functions
        button_names = ["All ON", "ALL OFF", "ALL LEFT", "ALL RIGHT", "ALL FORWARD", "ALL OPPOSITE"]
        functions = [
            self.persistent_destruction_all_on,
            self.persistent_destruction_all_off,
            self.persistent_destruction_all_left,
            self.persistent_destruction_all_right,
            self.persistent_destruction_all_forward,
            self.persistent_destruction_all_opposite
        ]

        for i, (name, function) in enumerate(zip(button_names, functions)):
            button = tk.Button(
                self.persistent_destruction_frame,
                text=name,
                command=function,
                bg="white",
                width=15
            )
            button.grid(row=i + 1, column=0, padx=5, pady=5)  # Place each button in the next row for vertical alignment

    def persistent_destruction_all_on(self):
        print("Persistent Destruction: All ON action triggered")

        # Get the duration and interval from Persistent Manipulation entries
        try:
            duration = int(self.duration_entry.get())
            interval = int(self.interval_entry.get())
        except ValueError:
            print("Invalid duration or interval values.")
            return

        # Dictionary to keep track of job IDs for each coil
        self.destruction_jobs = {}  # Initialize/reset the dictionary each time All ON is pressed

        # Loop through all coil buttons in the Persistent Manipulation subframe
        for name, button in self.persistent_manipulation_buttons.items():
            # Set the button to light green to indicate the ON state
            button.config(bg="light green")

            # Get the address of the specific coil
            address = self.DATA.coil_addresses[name][0]

            # Define a function to repeatedly write ON to the coil
            def send_persistent_on(coil_name=name, address=address):
                try:
                    self.DATA.client.write_coil(address, True)  # Send the ON command
                    # print(f"Writing ON to coil '{coil_name}' at address {address}")
                except Exception as e:
                    print(f"Failed to write ON to coil '{coil_name}' at address {address}: {e}")

            # Schedule the ON writes for the coil at the specified interval for the duration
            job_ids = []
            for i in range(0, duration * 1000, interval):
                job_id = self.after(i, send_persistent_on)
                job_ids.append(job_id)

            # Store the job IDs for this coil to allow clearing later
            self.destruction_jobs[name] = job_ids

            # Schedule a final job to reset the button to white after the duration
            self.after(duration * 1000, lambda b=button: b.config(bg="white"))

    def persistent_destruction_all_off(self):
        print("Persistent Destruction: All OFF action triggered")

        # Get the duration and interval from Persistent Manipulation entries
        try:
            duration = int(self.duration_entry.get())
            interval = int(self.interval_entry.get())
        except ValueError:
            print("Invalid duration or interval values.")
            return

        # Dictionary to keep track of job IDs for each coil
        self.destruction_jobs_off = {}  # Initialize/reset the dictionary each time All OFF is pressed

        # Loop through all coil buttons in the Persistent Manipulation subframe
        for name, button in self.persistent_manipulation_buttons.items():
            # Set the button to light red to indicate the OFF state
            button.config(bg="light salmon")

            # Get the address of the specific coil
            address = self.DATA.coil_addresses[name][0]

            # Define a function to repeatedly write OFF to the coil
            def send_persistent_off(coil_name=name, address=address):
                try:
                    self.DATA.client.write_coil(address, False)  # Send the OFF command
                    # print(f"Writing OFF to coil '{coil_name}' at address {address}")
                except Exception as e:
                    print(f"Failed to write OFF to coil '{coil_name}' at address {address}: {e}")

            # Schedule the OFF writes for the coil at the specified interval for the duration
            job_ids = []
            for i in range(0, duration * 1000, interval):
                job_id = self.after(i, send_persistent_off)
                job_ids.append(job_id)

            # Store the job IDs for this coil to allow clearing later
            self.destruction_jobs_off[name] = job_ids

            # Schedule a final job to reset the button to white after the duration
            self.after(duration * 1000, lambda b=button: b.config(bg="white"))

    def persistent_destruction_all_opposite(self):
        try:
            # Retrieve and validate the interval directly from the entry field
            interval = int(self.interval_entry.get())
            if interval <= 0:
                print("Interval must be a positive number.")
                return
        except ValueError:
            print("Invalid interval input. Please enter a numeric value.")
            return

        print("Starting all-opposite destruction...")

        # Define a nested function for toggling each coil to its opposite state
        def toggle_opposite():
            for name, (address, _) in self.DATA.coil_addresses.items():
                # Read the current state from the client
                try:
                    current_state = self.DATA.client.read_coils(address, 1).bits[0]
                    opposite_state = not current_state
                    # Write the opposite state to the coil
                    self.DATA.client.write_coil(address, opposite_state)
                    print(f"Toggled {name} to {'ON' if opposite_state else 'OFF'}")

                    # Update button color
                    button = self.persistent_manipulation_buttons.get(name)
                    if button:
                        button.config(bg="light green" if opposite_state else "salmon")
                except Exception as e:
                    print(f"Error reading/writing coil {name} at address {address}: {e}")

            # Schedule the next toggle based on the interval
            if "all_opposite" in self.active_jobs:
                job_id = self.after(interval, toggle_opposite)
                self.active_jobs["all_opposite"] = job_id

        # Start the toggling action
        job_id = self.after(interval, toggle_opposite)
        self.active_jobs["all_opposite"] = job_id

    def persistent_destruction_all_forward(self):
        print("Persistent Destruction: Button 4 action triggered")

    def persistent_destruction_all_right(self):
        print("Persistent Destruction: Button 5 action triggered")

    def persistent_destruction_all_left(self):
        print("Persistent Destruction: Button 6 action triggered")

    def toggle_coil_state(self, name):
        # Toggle the state for the coil
        current_state = self.DATA.coil_addresses[name][1]
        new_state = not current_state
        self.DATA.coil_addresses[name][1] = new_state

        # Write the new state to the coil address
        address = self.DATA.coil_addresses[name][0]
        try:
            # Writing to the coil with the new state
            self.DATA.client.write_coil(address, new_state)
            print(f"Coil {name} at address {address} set to {'ON' if new_state else 'OFF'}")

            # Update button appearance in coil_frame
            for widget in self.coil_frame.winfo_children():
                if isinstance(widget, tk.Button) and widget.cget("text").startswith(name):
                    widget.config(
                        text=f"{name}: {'ON' if new_state else 'OFF'}",
                        bg="green" if new_state else "red"
                    )

        except Exception as e:
            print(f"Failed to write to coil {name} at address {address}: {e}")
    def toggle_discrete_input_state(self, name):
        # Read current state of discrete input
        address = self.DATA.discrete_input_addresses[name][0]
        try:
            response = self.DATA.client.read_discrete_inputs(address, 1)
            if not response.isError():
                current_state = response.bits[0]
                new_state = not current_state
                self.DATA.discrete_input_addresses[name][1] = new_state  # Update state in DATA

                # Update button appearance
                for widget in self.dsc_inp_frame.winfo_children():
                    if isinstance(widget, tk.Button) and widget.cget("text").startswith(name):
                        widget.config(
                            text=f"{name}: {'ON' if new_state else 'OFF'}",
                            bg="green" if new_state else "red"
                        )
                print(f"Discrete Input {name} at address {address} toggled to {'ON' if new_state else 'OFF'}")
            else:
                print(f"Error reading discrete input {name} at address {address}")
        except Exception as e:
            print(f"Failed to read discrete input {name} at address {address}: {e}")
    def toggle_analog_inp_state(self, name):
        # Retrieve the current value of the analog input
        address = self.DATA.analog_input_addresses[name][0]
        current_value = self.DATA.analog_input_addresses[name][1]
        new_value = current_value + 1 if current_value < 10 else 0  # Example increment logic

        try:
            # Write the new value to the holding register
            self.DATA.client.write_register(address, new_value)
            self.DATA.analog_input_addresses[name] = (address, new_value)  # Update value in DATA

            # Update button appearance
            button = self.analog_inp_buttons.get(name)
            button.config(
                text=f"{name}: {new_value}",
                bg="green" if new_value > 0 else "red"
            )
            print(f"Analog Input {name} at address {address} set to {new_value}")
        except Exception as e:
            print(f"Failed to write to analog input {name} at address {address}: {e}")
    def toggle_analog_label_color(self, name):
        # Get the current label and its background color
        label = self.analog_input_labels[name]
        current_color = label.cget("bg")

        # Cycle through the colors: white -> light green -> white
        if current_color == "white":
            new_color = "light green"
        else:
            new_color = "white"

        # Update the label color
        label.config(bg=new_color)
        print(f"Analog Input Label '{name}' color changed to {new_color}")
    def toggle_persistent_manipulation_state(self, name):
        # Get the button and its current color
        button = self.persistent_manipulation_buttons[name]
        current_color = button.cget("bg")

        # Cycle through colors: white -> light green (write 1) -> salmon (write 0) -> white
        if current_color == "white":
            new_color = "light green"
            button.config(bg=new_color)
            print(f"Persistent Manipulation button '{name}' set to {new_color} (write 1)")
            # Start persistent write with value 1
            self.start_persistent_write(name, True)
        elif current_color == "light green":
            new_color = "salmon"  # Replacing "light red" with "salmon"
            button.config(bg=new_color)
            print(f"Persistent Manipulation button '{name}' set to {new_color} (write 0)")
            # Start persistent write with value 0
            self.start_persistent_write(name, False)
        else:
            new_color = "white"
            button.config(bg=new_color)
            print(f"Persistent Manipulation button '{name}' reset to {new_color} (OFF)")
    def toggle_persistent_destruction_button(self, index):
        # Toggle the button state
        self.destruction_button_states[index] = not self.destruction_button_states[index]

        # Update button color and print its number if enabled
        if self.destruction_button_states[index]:
            self.destruction_buttons[index].config(bg="green")
            print(f"Button {index + 1} is enabled.")
        else:
            self.destruction_buttons[index].config(bg="white")

    def start_persistent_write(self, name, write_value):
        # Read and validate the duration from the entry widget
        duration_str = self.duration_entry.get()
        try:
            duration = int(duration_str)
            if duration <= 0:
                raise ValueError("Duration must be a positive integer.")
        except ValueError:
            duration = 10
            print("Invalid duration entered, defaulting to 10 seconds.")

        start_time = time.time()  # Track the start time

        def send_write_coil():
            # Check if the button is still in the appropriate color state for this write operation
            button_color = self.persistent_manipulation_buttons[name].cget("bg")
            expected_color = "light green" if write_value else "salmon"

            # Only proceed if the button color matches the current persistent state
            if button_color == expected_color:
                # Retrieve the interval dynamically from the entry field
                interval_str = self.interval_entry.get()
                try:
                    interval = int(interval_str)
                    if interval <= 0:
                        raise ValueError("Interval must be a positive integer.")
                except ValueError:
                    interval = 250
                    print("Invalid interval entered, defaulting to 250 milliseconds.")

                # Send the write_coil command with the current write_value
                address = self.DATA.coil_addresses[name][0]
                try:
                    self.DATA.client.write_coil(address, write_value)
                    action = "ON" if write_value else "OFF"
                    # print(f"Writing {action} to coil '{name}' at address {address}")
                except Exception as e:
                    print(f"Error writing to coil '{name}': {e}")

                # Schedule the next write if the duration has not elapsed
                if (time.time() - start_time) < duration:
                    # Dynamically adjust the interval on each call
                    self.after(interval, send_write_coil)
                else:
                    # Turn the coil OFF after the duration ends, regardless of initial write_value
                    try:
                        self.DATA.client.write_coil(address, False)
                        print(f"Turning OFF coil '{name}' after {duration} seconds")
                    except Exception as e:
                        print(f"Error turning off coil '{name}': {e}")

                    # Reset the button color to white after duration completes
                    self.persistent_manipulation_buttons[name].config(bg="white")
                    print(f"Button '{name}' color reset to white after duration.")
            else:
                print(f"Skipping write for '{name}', as button color has changed from {expected_color}.")

        # Initial call to start the loop
        send_write_coil()

    def deactivate_button(self, name):
        # Reset button color to white
        if name in self.persistent_manipulation_buttons:
            self.persistent_manipulation_buttons[name].config(bg="white")
    def update_button_states(self):
        # Update buttons in coil_frame based on self.DATA.coil_addresses
        for widget in self.coil_frame.winfo_children():
            if isinstance(widget, tk.Button):
                # Extract the name from the button's current text
                name = widget.cget("text").split(":")[0]

                # Check if the name exists in coil_addresses and update button if so
                if name in self.DATA.coil_addresses:
                    state = self.DATA.coil_addresses[name][1]
                    widget.config(
                        text=f"{name}: {'ON' if state else 'OFF'}",
                        bg="green" if state else "red"
                    )

        # Update buttons in dsc_inp_frame based on self.DATA.discrete_input_addresses
        for widget in self.dsc_inp_frame.winfo_children():
            if isinstance(widget, tk.Button):
                # Extract the name from the button's current text
                name = widget.cget("text").split(":")[0]

                # Check if the name exists in discrete_input_addresses and update button if so
                if name in self.DATA.discrete_input_addresses:
                    state = self.DATA.discrete_input_addresses[name][1]
                    widget.config(
                        text=f"{name}: {'ON' if state else 'OFF'}",
                        bg="green" if state else "red"
                    )

        # Update buttons in analog_inp_frame based on self.DATA.analog_input_addresses
        for widget in self.analog_inp_frame.winfo_children():
            if isinstance(widget, tk.Button):
                # Extract the name from the button's current text
                name = widget.cget("text").split(":")[0]

                # Check if the name exists in analog_input_addresses and update button if so
                if name in self.DATA.analog_input_addresses:
                    value = self.DATA.analog_input_addresses[name][1]
                    widget.config(
                        text=f"{name}: {value}",
                        bg="green" if value > 0 else "red"
                    )

    def save_duration(self):
        # Get the duration value from the entry widget
        duration_str = self.duration_entry.get()

        # Check if the input is a positive integer
        if duration_str.isdigit() and int(duration_str) > 0:
            duration = int(duration_str)
            print(f"Duration set to {duration} seconds.")
        else:
            print("Invalid duration entered. Please enter a positive integer.")

    def save_interval(self):
        # Get the interval value from the entry widget
        interval_str = self.interval_entry.get()

        # Check if the input is a positive integer
        if interval_str.isdigit() and int(interval_str) > 0:
            interval = int(interval_str)
            print(f"Interval set to {interval} milliseconds.")
        else:
            print("Invalid interval entered. Please enter a positive integer.")

    def clear_all_persistent_writes(self):
        print("Clearing all persistent writes")

        # Clear any scheduled persistent jobs for coils
        if hasattr(self, 'destruction_jobs'):
            for job_ids in self.destruction_jobs.values():
                for job_id in job_ids:
                    self.after_cancel(job_id)
            self.destruction_jobs.clear()

        # Reset all buttons in Persistent Manipulation subframe to white
        for button in self.persistent_manipulation_buttons.values():
            button.config(bg="white")

    def clear_all(self):
        # Cancel all active coil manipulation jobs
        for job_id in self.active_jobs.values():
            self.after_cancel(job_id)
        self.active_jobs.clear()

        # Reset all buttons in the persistent manipulation subframe to white
        for button in self.persistent_manipulation_buttons.values():
            button.config(bg="white")

        # Stop the ongoing duration timer if it's running
        if hasattr(self, 'duration_job') and self.duration_job:
            self.after_cancel(self.duration_job)
            self.duration_job = None

        print("All persistent manipulation jobs cleared, and duration timer stopped")





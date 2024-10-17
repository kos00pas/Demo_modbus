import tkinter as tk


class Manipulation(tk.Frame):
    def __init__(self, parent, database):
        super().__init__(parent)
        self.configure(bg="dark blue")
        self.DATA = database

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
        persistent_manipulation_label = tk.Label(self.persistent_manipulation_frame, text="Persistent Manipulation ")
        persistent_manipulation_label.grid(row=0, column=0, columnspan=4, pady=(0, 10))

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

    def for_persistent_manipulation_frame(self):
        self.persistent_manipulation_buttons = {}  # Dictionary to store coil buttons by name
        self.analog_input_entries = {}  # Dictionary to store analog input entries by name
        self.analog_input_labels = {}  # Dictionary to store analog input labels by name

        # Row 0: Persistent Manipulation label across all columns
        main_label = tk.Label(self.persistent_manipulation_frame, text="Persistent Manipulation",
                              font=("Arial", 14, "bold"))
        main_label.grid(row=0, column=0, columnspan=6, padx=5, pady=5, sticky="nsew")

        # Row 1: Column headers for coils and analog inputs
        coil_label = tk.Label(self.persistent_manipulation_frame, text="Coils", font=("Arial", 10, "bold"))
        coil_label.grid(row=1, column=0, columnspan=4, padx=5, pady=5, sticky="nsew")  # Header for coil buttons

        analog_label = tk.Label(self.persistent_manipulation_frame, text="Analog Inputs", font=("Arial", 10, "bold"))
        analog_label.grid(row=1, column=4, columnspan=2, padx=5, pady=5, sticky="nsew")  # Header for analog inputs

        # Start adding coil buttons from row 2
        row = 2  # Start from row 2 due to new headers

        # Coils in columns 0, 1, 2, and 3
        left_row = row
        center_row = row
        right_row = row
        both_row = row

        for name, _ in self.DATA.coil_addresses.items():
            if name.lower().count("left") > 1 or name.lower().count("right") > 1 or (
                    "left" in name.lower() and "right" in name.lower()):
                column = 3
                row = both_row
                both_row += 1
            elif "left" in name.lower():
                column = 0
                row = left_row
                left_row += 1
            elif "right" in name.lower():
                column = 2
                row = right_row
                right_row += 1
            else:
                column = 1
                row = center_row
                center_row += 1

            # Create a button with an initial white background and color-changing command
            button = tk.Button(
                self.persistent_manipulation_frame,
                text=name,
                bg="white",
                command=lambda name=name: self.toggle_persistent_manipulation_state(name)
            )
            button.grid(row=row, column=column, padx=5, pady=5, sticky="ew")
            self.persistent_manipulation_buttons[name] = button

        # Analog Input Labels and Entries in columns 4 and 5, starting from row 2
        row = 2  # Reset row for analog input elements
        for name, (address, value) in self.DATA.analog_input_addresses.items():
            # Create a label with the name of the analog input and a command to cycle colors
            label = tk.Label(self.persistent_manipulation_frame, text=name, bg="white")
            label.grid(row=row, column=4, padx=5, pady=5, sticky="e")  # Align label to the right
            label.bind("<Button-1>", lambda e, name=name: self.toggle_analog_label_color(name))  # Bind click event
            self.analog_input_labels[name] = label  # Store label reference for future use

            # Create an entry widget for the analog input value
            entry = tk.Entry(self.persistent_manipulation_frame, width=10)
            entry.grid(row=row, column=5, padx=5, pady=5, sticky="w")  # Align entry to the left
            entry.insert(0, str(value))  # Set initial value from DATA
            self.analog_input_entries[name] = entry  # Store entry widget reference for future use

            row += 1  # Move to the next row for the next analog input

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
        # Get the current button and its color
        print(name)
        button = self.persistent_manipulation_buttons[name]
        current_color = button.cget("bg")

        # Cycle through the colors: white ->  light green-> thistle -> white
        if current_color == "white":
            new_color = "light green"
        elif current_color == "light green":
            new_color = "thistle"
        else:
            new_color = "white"

        # Update the button color
        button.config(bg=new_color)
        print(f"Button '{name}' color changed to {new_color}")

    def deactivate_button(self, name):
        # Reset button color to white
        if name in self.persistent_manipulation_buttons:
            self.persistent_manipulation_buttons[name].config(bg="white")

    def for_persistent_destruction_frame(self):
        # Create the frame for Persistent Destruction next to Persistent Manipulation
        self.persistent_destruction_frame = tk.Frame(self, bg="dark red", borderwidth=2, relief="groove", padx=10,
                                                     pady=10)
        self.persistent_destruction_frame.grid(row=2, column=2, rowspan=3, sticky="nsew", padx=10, pady=10)

        # Title label for the frame
        title_label = tk.Label(self.persistent_destruction_frame, text="Persistent Destruction",
                               font=("Arial", 14, "bold"))
        title_label.grid(row=0, column=0, columnspan=2, pady=5)

        # Initialize button states dictionary
        self.destruction_buttons = {}  # Store button references by their number
        self.destruction_button_states = [False] * 6  # Initialize all button states as disabled (not pressed)

        # Create 6 buttons in the frame with toggle functionality
        for i in range(6):
            button = tk.Button(
                self.persistent_destruction_frame,
                text=f"Button {i + 1}",
                bg="white",
                command=lambda idx=i: self.toggle_destruction_button(idx)
            )
            button.grid(row=i + 1, column=0, padx=5, pady=5, sticky="ew")
            self.destruction_buttons[i] = button  # Store button reference

    def toggle_destruction_button(self, index):
        # Toggle the button state
        self.destruction_button_states[index] = not self.destruction_button_states[index]

        # Update button color and print its number if enabled
        if self.destruction_button_states[index]:
            self.destruction_buttons[index].config(bg="green")
            print(f"Button {index + 1} is enabled.")
        else:
            self.destruction_buttons[index].config(bg="white")


import tkinter as tk


class Manipulation(tk.Frame):
    def __init__(self, parent, database):
        super().__init__(parent)
        self.configure(bg="dark blue")
        self.DATA = database
        self.buttons_created = False  # Flag to track button creation

        # Create the subframes (but don’t populate buttons yet)
        self.create_subframes()

        # Attempt connection and create buttons if successful

    def create_buttons(self):
        if not self.buttons_created:
            self.for_coil_frame()
            self.for_disc_inp_frame()
            self.buttons_created = True
    def create_subframes(self):
        # Coil Frame
        self.coil_frame = tk.Frame(self, bg="gray", borderwidth=2, relief="groove", padx=10, pady=10)
        self.coil_frame.grid(row=0, column=0, rowspan=2, sticky="nsew", padx=10, pady=10)
        coil_label = tk.Label(self.coil_frame, text="Coil Frame")
        coil_label.grid(row=0, column=0, columnspan=4, pady=(0, 10))  # Adjusted for column span

        # Add an Update button in the Coil Frame
        update_button = tk.Button(
            self.coil_frame,
            text="Update States",
            command=self.update_button_states
        )
        update_button.grid(row=0, column=3, padx=5, pady=5, sticky="e")

        # Discrete Input Frame
        self.dsc_inp_frame = tk.Frame(self, bg="gray", borderwidth=2, relief="groove", padx=10, pady=10)
        self.dsc_inp_frame.grid(row=0, column=2, sticky="nsew", padx=10, pady=10)
        dsc_inp_label = tk.Label(self.dsc_inp_frame, text="Discrete Input Frame")
        dsc_inp_label.pack()  # Keeping pack here for the label

        # Analog Input Frame
        analog_inp_frame = tk.Frame(self, bg="gray", borderwidth=2, relief="groove", padx=10, pady=10)
        analog_inp_frame.grid(row=1, column=2, sticky="nsew", padx=10, pady=10)
        analog_inp_label = tk.Label(analog_inp_frame, text="Analog Input Frame")
        analog_inp_label.pack()

        # Configure the layout to ensure frames are resizable
        self.grid_columnconfigure((0, 2), weight=1)
        self.grid_rowconfigure(0, weight=5)  # Discrete Input Frame row
        self.grid_rowconfigure(1, weight=1)  # Analog Input Frame row

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

    def toggle_coil_state(self, name):
        # Toggle state for coils
        current_state = self.DATA.coil_addresses[name][1]
        new_state = not current_state
        self.DATA.coil_addresses[name][1] = new_state

        # Find button and update appearance
        for widget in self.coil_frame.winfo_children():
            if isinstance(widget, tk.Button) and widget.cget("text").startswith(name):
                widget.config(
                    text=f"{name}: {'ON' if new_state else 'OFF'}",
                    bg="green" if new_state else "red"
                )

    def toggle_discrete_input_state(self, name):
        # Toggle state for discrete inputs
        current_state = self.DATA.discrete_input_addresses[name][1]
        new_state = not current_state
        self.DATA.discrete_input_addresses[name][1] = new_state

        # Find button and update appearance
        for widget in self.dsc_inp_frame.winfo_children():
            if isinstance(widget, tk.Button) and widget.cget("text").startswith(name):
                widget.config(
                    text=f"{name}: {'ON' if new_state else 'OFF'}",
                    bg="green" if new_state else "red"
                )

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

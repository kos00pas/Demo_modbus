import tkinter as tk

class The_Terminal_Window(tk.Frame):
    def __init__(self, parent, on_close_callback):
        super().__init__(parent)
        self.configure(bg="gray")  # Optional: set a background color for the console

        # Add a label for the terminal title
        label = tk.Label(self, text="Terminal", font=("Arial", 16), bg="white")
        label.pack(pady=10, padx=10)

        # Create the terminal output Text widget
        self.terminal = tk.Text(self, bg="black", fg="green", insertbackground="green", wrap="word")
        self.terminal.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        self.terminal.config(state=tk.DISABLED)  # Disable typing in the terminal

        # Store the callback function for when the console closes
        self.on_close_callback = on_close_callback
        # Optional close button, uncomment if needed
        """close_button = tk.Button(self, text="Close", command=self.close_console)
        close_button.pack(pady=10, padx=10)"""

        self.simulate_terminal_output()


    def simulate_terminal_output(self):
        # Example of using after within the class to simulate output
        self.after(100, lambda: self.print_to_terminal("Starting simulated terminal..."))
        self.after(200, lambda: self.print_to_terminal("Running command 1..."))
        self.after(300, lambda: self.print_to_terminal("Command 1 complete"))
        self.after(400, lambda: self.print_to_terminal("Running command 2..."))

    def print_to_terminal(self, text):
        # Function to insert text into the terminal and scroll down
        self.terminal.config(state=tk.NORMAL)
        self.terminal.insert(tk.END, text + "\n")
        self.terminal.see(tk.END)
        self.terminal.config(state=tk.DISABLED)

    def close_console(self):
        # Notify the main window that the console has been closed
        self.on_close_callback()
        self.destroy()
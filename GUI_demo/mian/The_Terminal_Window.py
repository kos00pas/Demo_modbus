import tkinter as tk
import sys
import glob
from collections import deque
import re

class The_Terminal_Window(tk.Frame):
    def __init__(self, parent, on_close_callback):
        super().__init__(parent)
        self.configure(bg="dark blue")

        # Label for the terminal title
        label = tk.Label(self, text="Terminal", font=("Arial", 16), bg="white")
        label.pack(pady=10, padx=10)

        # Text widget for terminal output
        self.terminal = tk.Text(self, bg="black", fg="green", insertbackground="green", wrap="word")
        self.terminal.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        self.terminal.config(state=tk.DISABLED)

        # Start/Stop button
        self.start_stop_button = tk.Button(self, text="Stop", command=self.toggle_output)
        self.start_stop_button.pack(pady=10)

        # Store the callback function for when the console closes
        self.on_close_callback = on_close_callback

        # Redirect sys.stdout to the terminal window
        self.original_stdout = sys.stdout
        sys.stdout = self  # Redirect standard output to this instance

        # Message queue, buffer, and scheduling of the output
        self.message_queue = deque()
        self.buffer = ""  # Buffer to hold characters to process in chunks
        self.file_buffer = ""  # Buffer for file content
        self.active_output = False  # Track if new print output is active
        self.output_paused = False  # Track if output is manually paused
        self.update_terminal()  # Schedule regular updates

    def write(self, message):
        # Add message to the queue and set active output flag
        self.message_queue.append(message)
        self.active_output = True

    def load_files_into_buffer(self):
        # Read all .py files in the directory and add their content to file_buffer
        files = glob.glob("*.py")  # Adjust the path as needed
        self.file_buffer = ""
        for file_path in files:
            with open(file_path, 'r') as file:
                self.file_buffer += file.read() + "\n"  # Separate each file content

    import re

    def update_terminal(self):
        # Check if output is paused
        if self.output_paused:
            self.after(100, self.update_terminal)
            return

        # Enable the Text widget, insert a chunk from the buffer, then disable it
        if self.buffer or self.message_queue:
            self.terminal.config(state=tk.NORMAL)

            # Add new messages from the queue to the buffer
            while self.message_queue:
                self.buffer += self.message_queue.popleft()

            # Display up to 100 characters from the buffer
            chunk = self.buffer[:100]

            # Find all parts in the chunk, treating numbers differently
            parts = re.split(r'(\d+)', chunk)  # Split by digits

            # Insert each part, coloring numbers red
            for part in parts:
                if part.isdigit():  # Check if the part is a number
                    self.terminal.insert(tk.END, part, ("red",))
                else:
                    self.terminal.insert(tk.END, part, ("green",))

            # Configure tags for color
            self.terminal.tag_config("green", foreground="green")
            self.terminal.tag_config("red", foreground="red")

            # Update the widget
            self.terminal.config(state=tk.DISABLED)
            self.terminal.see(tk.END)  # Auto-scroll to the end

            # Remove the displayed chunk from the buffer
            self.buffer = self.buffer[100:]

            # Reset the active output flag if no new output was generated
            self.active_output = bool(self.message_queue)

        elif self.file_buffer:
            # Print from file content buffer if there is no new output
            self.terminal.config(state=tk.NORMAL)
            chunk = self.file_buffer[:100]

            # Find all parts in the chunk, treating numbers differently
            parts = re.split(r'(\d+)', chunk)

            # Insert each part, coloring numbers red
            for part in parts:
                if part.isdigit():
                    self.terminal.insert(tk.END, part, ("red",))
                else:
                    self.terminal.insert(tk.END, part, ("green",))

            # Update the widget
            self.terminal.config(state=tk.DISABLED)
            self.terminal.see(tk.END)
            self.file_buffer = self.file_buffer[100:]

        elif not self.file_buffer and not self.active_output:
            # Reload files if buffer is empty and no new output is active
            self.load_files_into_buffer()

        # Schedule the next update
        self.after(100, self.update_terminal)

    def toggle_output(self):
        # Toggle the output paused state and button text
        self.output_paused = not self.output_paused
        self.start_stop_button.config(text="Start" if self.output_paused else "Stop")

    def flush(self):
        # Required for compatibility with sys.stdout
        pass

    def close_console(self):
        # Restore the original stdout
        sys.stdout = self.original_stdout
        self.on_close_callback()

import tkinter as tk
import sys
import glob
import re
from collections import deque
from io import StringIO
from PIL import Image, ImageTk


class The_Terminal_Window(tk.Frame):
    def __init__(self, parent, on_close_callback):
        super().__init__(parent)
        self.configure(bg="dark blue")

        # Initialize upper frame with the image
        self.upper_frame_function()

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
        self.capture_stdout = StringIO()
        sys.stdout = self  # Redirect standard output to this instance

        # Message queue, buffer, and scheduling of the output
        self.message_queue = deque()
        self.priority_queue = []  # List for holding priority messages as tuples (priority, message)
        self.buffer = ""  # Buffer to hold characters to process in chunks
        self.file_buffer = ""  # Buffer for file content
        self.active_output = False  # Track if new print output is active
        self.output_paused = False  # Track if output is manually paused
        self.update_terminal()  # Schedule regular updates

    def write(self, message):
        # Add message to the queue and set active output flag
        self.message_queue.append(message)
        self.active_output = True

        # Print to both GUI and original stdout
        self.capture_stdout.write(message)
        self.original_stdout.write(message)  # Send to the IntelliJ terminal
        self.original_stdout.flush()  # Ensure it flushes immediately

    def update_terminal(self):
        if self.output_paused:
            self.after(100, self.update_terminal)
            return

        if self.buffer or self.message_queue:
            self.terminal.config(state=tk.NORMAL)
            while self.message_queue:
                self.buffer += self.message_queue.popleft()

            chunk = self.buffer[:100]
            parts = re.split(r'(\d+)', chunk)
            for part in parts:
                if part.isdigit():
                    self.terminal.insert(tk.END, part, ("red",))
                else:
                    self.terminal.insert(tk.END, part, ("green",))

            self.terminal.tag_config("green", foreground="green")
            self.terminal.tag_config("red", foreground="red")
            self.terminal.config(state=tk.DISABLED)
            self.terminal.see(tk.END)
            self.buffer = self.buffer[100:]
            self.active_output = bool(self.message_queue)

        elif self.file_buffer:
            self.terminal.config(state=tk.NORMAL)
            chunk = self.file_buffer[:100]
            parts = re.split(r'(\d+)', chunk)
            for part in parts:
                if part.isdigit():
                    self.terminal.insert(tk.END, part, ("red",))
                else:
                    self.terminal.insert(tk.END, part, ("green",))

            self.terminal.config(state=tk.DISABLED)
            self.terminal.see(tk.END)
            self.file_buffer = self.file_buffer[100:]

        elif not self.file_buffer and not self.active_output:
            self.load_files_into_buffer()

        self.after(100, self.update_terminal)

    def toggle_output(self):
        self.output_paused = not self.output_paused
        self.start_stop_button.config(text="Start" if self.output_paused else "Stop")

    def load_files_into_buffer(self):
        files = glob.glob("*.py")
        self.file_buffer = ""
        for file_path in files:
            with open(file_path, 'r') as file:
                self.file_buffer += file.read() + "\n"

    def flush(self):
        pass

    def close_console(self):
        sys.stdout = self.original_stdout
        self.on_close_callback()

    def add_message(self, text, priority=0):
        self.priority_queue.append((priority, text))
        self.priority_queue.sort(reverse=True, key=lambda x: x[0])
        while self.priority_queue:
            _, message = self.priority_queue.pop(0)
            self.message_queue.appendleft(message)
        self.active_output = True


    def upper_frame_function(self):
        # Create an upper frame within the terminal window
        self.upper_frame = tk.Frame(self, bg="dark blue")
        self.upper_frame.pack(fill=tk.BOTH, expand=True)

        # Load and display the image
        image_path = "./Designe.jpeg"  # Use the correct path to the uploaded image
        img = Image.open(image_path)
        img = img.resize((200, 200), Image.LANCZOS)
        photo = ImageTk.PhotoImage(img)

        # Label to hold the image
        image_label = tk.Label(self.upper_frame, image=photo, bg="white")
        image_label.image = photo  # Keep a reference to avoid garbage collection
        image_label.pack(pady=10, padx=10)

        # Add any additional widgets or labels in this frame as needed
        additional_label = tk.Label(self.upper_frame, text="Welcome to KIOS Hack Group", font=("Arial", 14), bg="white")
        additional_label.pack(pady=5)

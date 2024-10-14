# The_Console_Window.py
import tkinter as tk

class The_Console_Window(tk.Frame):
    def __init__(self, parent,on_close_callback):
        super().__init__(parent)
        self.configure(bg="gray")  # Optional: set a background color for the console

        # Add widgets to the console frame
        label = tk.Label(self, text="Terminal", font=("Arial", 16), bg="white")
        label.pack(pady=10, padx=10)

        self.on_close_callback = on_close_callback
        close_button = tk.Button(self, text="Close", command=self.close_console)
        close_button.pack(pady=10, padx=10)

    def close_console(self):
        # Notify the main window that the console has been closed
        self.on_close_callback()
        self.destroy()
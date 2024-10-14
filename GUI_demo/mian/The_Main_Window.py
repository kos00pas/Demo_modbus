import tkinter as tk
import matplotlib.pyplot as plt
import sys
from The_Console_Window import The_Console_Window  # Import the console frame


class Main_Window(tk.Tk):
    def __init__(self, database):
        super().__init__()
        self.DATA = database
        self.protocol("WM_DELETE_WINDOW", self.on_close_main_window)
        self.configure(bg="black")

        if sys.platform.startswith('win'):
            self.state('zoomed')

        self.fig = plt.figure(figsize=(12, 10))
        self.setup_main_and_console_layout()

    def setup_main_and_console_layout(self):
        paned_window = tk.PanedWindow(self, orient="horizontal")
        paned_window.pack(fill="both", expand=True)

        self.console_window_frame = tk.Frame(paned_window, bg="black")
        self.main_window_frame = tk.Frame(paned_window, bg="black")

        paned_window.add(self.main_window_frame, minsize=100)  # minsize to set minimum width for resizing
        paned_window.add(self.console_window_frame, minsize=100)

        self.update()  # This will update the window dimensions

        initial_main_width_percentage = 0.75  # 70% of the total width
        actual_window_width = self.winfo_width()  # Get the actual window width after updating
        initial_main_width = int(actual_window_width * initial_main_width_percentage)

        paned_window.update_idletasks()
        paned_window.sash_place(0, initial_main_width, 0)  # Set sash at initial_main_width pixels from the left

        self.open_console_button = tk.Button(
            self.main_window_frame, text="Open Console Window", command=self.open_console_window)
        self.open_console_button.pack_forget()  # Hide initially

        self.open_console_window()
        tk.Label(self.main_window_frame, text="Modbus Monitoring", font=("Arial", 16), bg="white").pack(pady=20)

        self.update_idletasks()

    def open_console_window(self):
        if not hasattr(self, 'console_window') or not self.console_window.winfo_exists():
            self.console_window = The_Console_Window(self.console_window_frame, self.console_closed)
            self.console_window.pack(fill="both", expand=True)
            self.open_console_button.pack_forget()  # Hide button while console is open

    def console_closed(self):
        self.open_console_button.pack(pady=20)  # Show button when console is closed

    def on_close_main_window(self):
        print("**Wait for closing")
        if hasattr(self.DATA, 'close'):
            try:
                self.DATA.close()
                print("**Resource closed successfully")
            except Exception as e:
                print(f"**Error closing resource: {e}")
        self.quit()
        self.destroy()


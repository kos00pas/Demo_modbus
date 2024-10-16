import tkinter as tk
import matplotlib.pyplot as plt
import sys
from The_Terminal_Window import The_Terminal_Window  # Import the console frame
from Connection_page import Connection_page
from Manipulation import Manipulation


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
        self.navigator_control_frame()

    def navigator_control_frame(self):
        # Create the navigation frame inside main_window_frame
        self.navigation_frame = tk.Frame(self.main_window_frame, bg="black")
        self.navigation_frame.pack(side="top", fill="x")

        # Page selection buttons
        button1 = tk.Button(self.navigation_frame, text="Connection Page", command=self.show_connection_window)
        button2 = tk.Button(self.navigation_frame, text="Manipulation", command=self.show_manipulation_window)
        button1.pack(side="left")
        button2.pack(side="left")

        # Frame for pages (inside main_window_frame)
        try:
            self.DATA.manipulation_window = Manipulation(self.main_window_frame, self.DATA)
        finally:
                self.DATA.connection_window = Connection_page(self.main_window_frame,self.DATA)

        # Pack pages to fill main_window_frame, but hide them initially
        self.DATA.connection_window.pack(fill="both", expand=True)
        self.DATA.manipulation_window.pack(fill="both", expand=True)

        # Show only the first page by default
        self.show_connection_window()

    def show_connection_window(self):
        self.DATA.manipulation_window.pack_forget()
        self.DATA.connection_window.pack(fill="both", expand=True)
        self.DATA.connection_window.tkraise()

    def show_manipulation_window(self):
        self.DATA.connection_window.pack_forget()
        self.DATA.manipulation_window.pack(fill="both", expand=True)
        self.DATA.manipulation_window.tkraise()

    def setup_main_and_console_layout(self):
        paned_window = tk.PanedWindow(self, orient="horizontal")
        paned_window.pack(fill="both", expand=True)

        # Define frames for main content and console
        self.terminal_window_frame = tk.Frame(paned_window, bg="gray")
        self.main_window_frame = tk.Frame(paned_window, bg="dark blue")

        # Add frames to paned window
        paned_window.add(self.main_window_frame, minsize=100)
        paned_window.add(self.terminal_window_frame, minsize=100)

        self.update()

        initial_main_width_percentage = 0.75
        actual_window_width = self.winfo_width()
        initial_main_width = int(actual_window_width * initial_main_width_percentage)

        paned_window.update_idletasks()
        paned_window.sash_place(0, initial_main_width, 0)

        self.open_console_button = tk.Button(
            self.main_window_frame, text="Open Console Window", command=self.open_console_window)
        self.open_console_button.pack_forget()

        self.open_console_window()
        tk.Label(self.main_window_frame, text="Modbus Monitoring", font=("Arial", 16), bg="white").pack(pady=20)

        self.update_idletasks()

    def open_console_window(self):
        if not hasattr(self, 'console_window') or not self.console_window.winfo_exists():
            self.DATA.terminal_window = The_Terminal_Window(self.terminal_window_frame, self.console_closed)
            self.DATA.terminal_window.pack(fill="both", expand=True)
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

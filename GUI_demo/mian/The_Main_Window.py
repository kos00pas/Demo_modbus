import tkinter as tk
import matplotlib.pyplot as plt
import sys
from The_Console_Window import The_Console_Window  # Import the console frame
from Page1 import Page1
from Page2 import Page2


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
        self.navigation_frame = tk.Frame(self.main_window_frame, bg="gray")
        self.navigation_frame.pack(side="top", fill="x")

        # Page selection buttons
        button1 = tk.Button(self.navigation_frame, text="Page 1", command=self.show_page1)
        button2 = tk.Button(self.navigation_frame, text="Page 2", command=self.show_page2)
        button1.pack(side="left")
        button2.pack(side="left")

        # Frame for pages (inside main_window_frame)
        self.page1 = Page1(self.main_window_frame)
        self.page2 = Page2(self.main_window_frame)

        # Pack pages to fill main_window_frame, but hide them initially
        self.page1.pack(fill="both", expand=True)
        self.page2.pack(fill="both", expand=True)

        # Show only the first page by default
        self.show_page1()

    def show_page1(self):
        # Show Page1 and hide Page2
        self.page2.pack_forget()
        self.page1.pack(fill="both", expand=True)
        self.page1.tkraise()

    def show_page2(self):
        # Show Page2 and hide Page1
        self.page1.pack_forget()
        self.page2.pack(fill="both", expand=True)
        self.page2.tkraise()

    def setup_main_and_console_layout(self):
        paned_window = tk.PanedWindow(self, orient="horizontal")
        paned_window.pack(fill="both", expand=True)

        # Define frames for main content and console
        self.console_window_frame = tk.Frame(paned_window, bg="black")
        self.main_window_frame = tk.Frame(paned_window, bg="black")

        # Add frames to paned window
        paned_window.add(self.main_window_frame, minsize=100)
        paned_window.add(self.console_window_frame, minsize=100)

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

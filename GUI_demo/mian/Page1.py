# Page1.py
import tkinter as tk

class Page1(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        label = tk.Label(self, text="This is Page 1")
        label.pack()

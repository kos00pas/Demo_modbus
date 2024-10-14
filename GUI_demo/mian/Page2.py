# Page2.py
import tkinter as tk

class Page2(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        label = tk.Label(self, text="This is Page 2")
        label1 = tk.Label(self, text="This is Page 2")
        label2 = tk.Label(self, text="This is Page 2")
        label3 = tk.Label(self, text="This is Page 2")
        label4 = tk.Label(self, text="This is Page 4")
        label.pack()
        label1.pack()
        label2.pack()
        label3.pack()
        label4.pack()

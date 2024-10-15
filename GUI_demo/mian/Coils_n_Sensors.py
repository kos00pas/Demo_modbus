# Page2.py
import tkinter as tk

class Coils_n_Sensors(tk.Frame):
    def __init__(self, parent,database,):
        super().__init__(parent)
        self.DATA=database

        # Create the subframes
        self.create_subframes()
        self.for_coil_frame()
        self.for_disc_inp_frame()
        self.for_anlg_inp_frame()

    def create_subframes(self):
        # Coil Frame
        coil_frame = tk.Frame(self, borderwidth=2, relief="groove", padx=10, pady=10)
        coil_frame.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)
        coil_label = tk.Label(coil_frame, text="Coil Frame")
        coil_label.pack()

        # Discrete Input Frame
        dsc_inp_frame = tk.Frame(self, borderwidth=2, relief="groove", padx=10, pady=10)
        dsc_inp_frame.grid(row=0, column=1, sticky="nsew", padx=10, pady=10)
        dsc_inp_label = tk.Label(dsc_inp_frame, text="Discrete Input Frame")
        dsc_inp_label.pack()

        # Analog Input Frame
        analog_inp_frame = tk.Frame(self, borderwidth=2, relief="groove", padx=10, pady=10)
        analog_inp_frame.grid(row=1, column=1, sticky="nsew", padx=10, pady=10)
        analog_inp_label = tk.Label(analog_inp_frame, text="Analog Input Frame")
        analog_inp_label.pack()

        # Configure the layout to ensure frames are resizable
        self.grid_columnconfigure((0, 1, 2), weight=1)
        self.grid_rowconfigure(0, weight=1)

    def for_coil_frame(self,):
        pass
    def for_disc_inp_frame(self,):
        pass
    def for_anlg_inp_frame(self):
        pass
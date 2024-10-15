# Page2.py
import tkinter as tk

class Coils_n_Sensors(tk.Frame):
    def __init__(self, parent,database,):
        super().__init__(parent)
        self.DATA=database
        self.coil_row=1
        self.dsc_inp_row=10
        self.analog_inp_row=15


        self.Coils( self.coil_frame,self.coil_row)
        self.Discrete_input( self.dsc_inp_frame,self.dsc_inp_row)
        self.Analog_inp( self.analog_inp_frame,self.analog_inp_row)

    def Coils(self,roww,space):
         pass
    def Discrete_input(self,roww,space):
         pass
    def Analog_inp(self,roww,space):
         pass
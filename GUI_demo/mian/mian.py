import The_Data_Class
from The_Main_Window import Main_Window

class GUIManager:
    def __init__(self):
        self.DATA = The_Data_Class.Data_Class( ) #1
        self.main_window =Main_Window(self.DATA)
        self.DATA.main_window = self.main_window  # 3
        self.main_window.mainloop()


the_gui_manager = GUIManager()
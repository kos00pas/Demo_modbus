


class Data_Class:
    def __init__(self,):
        self.connection_ip=None
        self.connection_window =None
        self.main_window =None
        self.terminal_window =None
        self.client =None
        # Addresses for coils
        self.coil_addresses = {
            "Main_Conveyor": 0,
            "Scale_Conveyor": 1,
            "Send_Forward": 2,
            "Send_Left": 3,
            "Send_Right": 4,
            "Front_Conveyor1": 5,
            "Front_Conveyor2": 6,
            "Right_Conveyor1": 7,
            "Right_Conveyor2": 8,
            "Left_Conveyor1": 9,
            "Left_Conveyor2": 10,
            "Left_Stick_Down": 19,
            "Left_Stick_Grab": 20,
            "Left_Stick_Left_Rotation": 21,
            "Left_Stick_Right_Rotation": 22,
            "Left_Stick_Endend": 23,
            "Right_Stick_Down": 24,
            "Right_Stick_Grab": 25,
            "Right_Stick_Left_Rotation": 26,
            "Right_Stick_Right_Rotation": 27,
            "Right_Stick_Extend": 28,
            "Left_Roller1": 37,
            "Left_Roller2": 38,
            "Right_Roller1": 39,
            "Right_Roller2": 40
        }

        # Addresses for discrete inputs
        self.discrete_input_addresses = {
            "Scale_Sensor": 0,
            "Left_Stick_Sensor": 1,
            "Right_Stick_Sensor": 2
        }
    def close(self):
        print("close DATA")


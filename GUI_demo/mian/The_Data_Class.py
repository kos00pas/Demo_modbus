


class Data_Class:
    def __init__(self,):
        self.connection_ip=None
        self.connection_window =None
        self.manipulation_window=None
        self.main_window =None
        self.terminal_window =None
        self.client =None
        self.buttons_created = False
        self.ip_address =None
        self.manipulation_data_already_created=False
        # Addresses for coils
        self.coil_addresses = {
            "Main_Conveyor": [0, False],
            "Scale_Conveyor": [1, False],
            "Send_Forward": [2, False],
            "Send_Left": [3, False],
            "Send_Right": [4, False],
            "Front_Conveyor1": [5, False],
            "Front_Conveyor2": [6, False],
            "Right_Conveyor1": [7, False],
            "Right_Conveyor2": [8, False],
            "Left_Conveyor1": [9, False],
            "Left_Conveyor2": [10, False],
            "Left_Stick_Down": [19, False],
            "Left_Stick_Grab": [20, False],
            "Left_Stick_Left_Rotation": [21, False],
            "Left_Stick_Right_Rotation": [22, False],
            "Left_Stick_Endend": [23, False],
            "Right_Stick_Down": [24, False],
            "Right_Stick_Grab": [25, False],
            "Right_Stick_Left_Rotation": [26, False],
            "Right_Stick_Right_Rotation": [27, False],
            "Right_Stick_Extend": [28, False],
            "Left_Roller1": [37, False],
            "Left_Roller2": [38, False],
            "Right_Roller1": [39, False],
            "Right_Roller2": [40, False]
        }

        # Addresses for discrete inputs
        self.discrete_input_addresses = {
            "Scale_Sensor": [0, False],
            "Left_Stick_Sensor": [1, False],
            "Right_Stick_Sensor": [2, False]
        }
        self.analog_input_addresses= {
            "Weight"  : [0,0]
        }

    def close(self):
        print("close DATA")


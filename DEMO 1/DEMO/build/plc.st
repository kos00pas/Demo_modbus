TYPE
  LOGLEVEL : (CRITICAL, WARNING, INFO, DEBUG) := INFO;
END_TYPE

FUNCTION_BLOCK LOGGER
  VAR_INPUT
    TRIG : BOOL;
    MSG : STRING;
    LEVEL : LOGLEVEL := INFO;
  END_VAR
  VAR
    TRIG0 : BOOL;
  END_VAR

  IF TRIG AND NOT TRIG0 THEN
  {{
   LogMessage(GetFbVar(LEVEL),(char*)GetFbVar(MSG, .body),GetFbVar(MSG, .len));
  }}
  END_IF;
  TRIG0:=TRIG;
END_FUNCTION_BLOCK


PROGRAM FactoryIO_Demo
  VAR
    Start : BOOL;
  END_VAR
  VAR
    Main_Conveyor : BOOL;
    Scale_Conveyor : BOOL;
    Send_Forward : BOOL;
    Send_Left : BOOL;
    Send_Right : BOOL;
    Front_Conveyor1 : BOOL;
    Front_Conveyor2 : BOOL;
    Right_Conveyor1 : BOOL;
    Right_Conveyor2 : BOOL;
    Left_Conveyor1 : BOOL;
    Left_Conveyor2 : BOOL;
    Left_Roller1 : BOOL;
    Left_Roller2 : BOOL;
    Right_Roller1 : BOOL;
    Right_Roller2 : BOOL;
  END_VAR
  VAR
    Heavy_Indicator : BOOL;
    Light_Indicator : BOOL;
  END_VAR
  VAR
    Scale_Sensor : BOOL;
  END_VAR
  VAR
    Scale_Timeout : BOOL;
    Wait_Time : INT := 2;
  END_VAR
  VAR
    Weight : INT;
  END_VAR
  VAR
    TON3 : TON;
    TOF0 : TOF;
    TOF1 : TOF;
  END_VAR
  VAR
    Left_Stick_Sensor : BOOL;
    Right_Stick_Sensor : BOOL;
    Left_Stick_Down : BOOL;
    Left_Stick_Grab : BOOL;
    Left_Stick_Left_Rotation : BOOL;
    Left_Stick_Right_Rotation : BOOL;
    Left_Stick_Endend : BOOL;
    Right_Stick_Down : BOOL;
    Right_Stick_Grab : BOOL;
    Right_Stick_Left_Rotation : BOOL;
    Right_Stick_Right_Rotation : BOOL;
    Right_Stick_Extend : BOOL;
  END_VAR
  VAR
    TON4 : TON;
    TON5 : TON;
    TON6 : TON;
    TON7 : TON;
    TON8 : TON;
    TON9 : TON;
    TON10 : TON;
    TON2 : TON;
    TOF2 : TOF;
    TOF3 : TOF;
    TOF4 : TOF;
    TOF5 : TOF;
    Right_GoDown1 : BOOL;
    Right_GoDown2 : BOOL;
    Left_GoDown1 : BOOL;
    Left_GoDown2 : BOOL;
    Start_Right_Roller1 : BOOL;
    Start_Left_Roller1 : BOOL;
    CTU0 : CTU;
    CTU1 : CTU;
    TOF6 : TOF;
    TOF7 : TOF;
    _TMP_GE18_OUT : BOOL;
    _TMP_LE16_OUT : BOOL;
    R_TRIG1 : R_TRIG;
    F_TRIG1 : F_TRIG;
    R_TRIG2 : R_TRIG;
    F_TRIG2 : F_TRIG;
  END_VAR

  Left_Conveyor1 := TRUE;
  Front_Conveyor2 := TRUE;
  Right_Conveyor1 := TRUE;
  TON3(IN := Scale_Sensor, PT := T#1500ms);
  Scale_Timeout := TON3.Q;
  TOF0(IN := Light_Indicator AND Scale_Sensor, PT := T#2200ms);
  Send_Left := TOF0.Q;
  TOF1(IN := NOT(Heavy_Indicator) AND NOT(Light_Indicator) AND Scale_Sensor, PT := T#2200ms);
  Send_Right := TOF1.Q;
  Send_Forward := TRUE;
  Main_Conveyor := NOT(Scale_Sensor) OR Scale_Timeout;
  _TMP_GE18_OUT := GE(Weight, 600);
  Heavy_Indicator := _TMP_GE18_OUT;
  _TMP_LE16_OUT := LE(Weight, 250);
  Light_Indicator := _TMP_LE16_OUT;
  Scale_Conveyor := NOT(Scale_Sensor) OR Scale_Timeout;
  Left_Conveyor2 := NOT(Left_Stick_Sensor);
  Right_Conveyor2 := NOT(Right_Stick_Sensor);
  Left_GoDown1 := NOT(Left_Stick_Grab) AND Left_Stick_Sensor;
  TON2(IN := NOT(Left_Stick_Grab) AND Left_Stick_Sensor, PT := T#500ms);
  TOF2(IN := TON2.Q, PT := T#2000ms);
  Left_Stick_Grab := TOF2.Q;
  TON5(IN := TOF2.Q, PT := T#500ms);
  Left_Stick_Left_Rotation := TON5.Q;
  TON7(IN := TON5.Q, PT := T#500ms);
  Left_GoDown2 := TON7.Q;
  TOF4(IN := TON7.Q, PT := T#1250ms);
  TON9(IN := TOF4.Q, PT := T#1200ms);
  Left_Stick_Right_Rotation := TON9.Q;
  Right_GoDown1 := NOT(Right_Stick_Grab) AND Right_Stick_Sensor;
  TON4(IN := NOT(Right_Stick_Grab) AND Right_Stick_Sensor, PT := T#500ms);
  TOF3(IN := TON4.Q, PT := T#2000ms);
  Right_Stick_Grab := TOF3.Q;
  TON6(IN := TOF3.Q, PT := T#500ms);
  Right_Stick_Right_Rotation := TON6.Q;
  TON8(IN := TON6.Q, PT := T#500ms);
  Right_GoDown2 := TON8.Q;
  TOF5(IN := TON8.Q, PT := T#1250ms);
  TON10(IN := TOF5.Q, PT := T#1200ms);
  Right_Stick_Left_Rotation := TON10.Q;
  Front_Conveyor1 := TRUE;
  Left_Roller2 := TRUE;
  Right_Roller2 := TRUE;
  Left_Stick_Down := Left_GoDown1 OR Left_GoDown2;
  Right_Stick_Down := Right_GoDown1 OR Right_GoDown2;
  Start_Right_Roller1 := TON10.Q;
  Start_Left_Roller1 := TON9.Q;
  R_TRIG1(CLK := Start_Left_Roller1);
  F_TRIG1(CLK := Left_Roller1);
  CTU0(CU := R_TRIG1.Q, R := F_TRIG1.Q, PV := 2);
  TOF6(IN := NOT(Left_Roller1) AND CTU0.Q, PT := T#2300ms);
  Left_Roller1 := TOF6.Q;
  R_TRIG2(CLK := Start_Right_Roller1);
  F_TRIG2(CLK := Right_Roller1);
  CTU1(CU := R_TRIG2.Q, R := F_TRIG2.Q, PV := 2);
  TOF7(IN := NOT(Right_Roller1) AND CTU1.Q, PT := T#2300ms);
  Right_Roller1 := TOF7.Q;
END_PROGRAM


CONFIGURATION Config0

  RESOURCE Res0 ON PLC
    TASK task0(INTERVAL := T#20ms,PRIORITY := 0);
    PROGRAM instance0 WITH task0 : FactoryIO_Demo;
  END_RESOURCE
END_CONFIGURATION

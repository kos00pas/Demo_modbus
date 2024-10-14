PROGRAM FactoryIO_Demo
  VAR
    Start : BOOL;
  END_VAR
  VAR
    Main_Conveyor AT %QX100.0 : BOOL;
    Scale_Conveyor AT %QX100.1 : BOOL;
    Send_Forward AT %QX100.2 : BOOL;
    Send_Left AT %QX100.3 : BOOL;
    Send_Right AT %QX100.4 : BOOL;
    Front_Conveyor1 AT %QX100.5 : BOOL;
    Front_Conveyor2 AT %QX100.6 : BOOL;
    Right_Conveyor1 AT %QX100.7 : BOOL;
    Right_Conveyor2 AT %QX101.0 : BOOL;
    Left_Conveyor1 AT %QX101.1 : BOOL;
    Left_Conveyor2 AT %QX101.2 : BOOL;
    Left_Roller1 AT %QX102.5 : BOOL;
    Left_Roller2 AT %QX102.6 : BOOL;
    Right_Roller1 AT %QX102.7 : BOOL;
    Right_Roller2 AT %QX103.0 : BOOL;
  END_VAR
  VAR
    Heavy_Indicator : BOOL;
    Light_Indicator : BOOL;
  END_VAR
  VAR
    Scale_Sensor AT %IX100.0 : BOOL;
  END_VAR
  VAR
    Scale_Timeout : BOOL;
    Wait_Time : INT := 2;
  END_VAR
  VAR
    Weight AT %IW100 : INT;
  END_VAR
  VAR
    TON3 : TON;
    TOF0 : TOF;
    TOF1 : TOF;
  END_VAR
  VAR
    Left_Stick_Sensor AT %IX100.1 : BOOL;
    Right_Stick_Sensor AT %IX100.2 : BOOL;
    Left_Stick_Down AT %QX101.3 : BOOL;
    Left_Stick_Grab AT %QX101.4 : BOOL;
    Left_Stick_Left_Rotation AT %QX101.5 : BOOL;
    Left_Stick_Right_Rotation AT %QX101.6 : BOOL;
    Left_Stick_Endend AT %QX101.7 : BOOL;
    Right_Stick_Down AT %QX102.0 : BOOL;
    Right_Stick_Grab AT %QX102.1 : BOOL;
    Right_Stick_Left_Rotation AT %QX102.2 : BOOL;
    Right_Stick_Right_Rotation AT %QX102.3 : BOOL;
    Right_Stick_Extend AT %QX102.4 : BOOL;
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

(*DBG:char md5[] = "193fd8d573961f539c82820f97fb42b2";*)
(*DBG:/**)
(*DBG: * This file is part of OpenPLC Runtime*)
(*DBG: **)
(*DBG: * Copyright (C) 2023 Autonomy, GP Orcullo*)
(*DBG: * Based on the work by GP Orcullo on Beremiz for uC*)
(*DBG: **)
(*DBG: * This program is free software; you can redistribute it and/or*)
(*DBG: * modify it under the terms of the GNU General Public License*)
(*DBG: * as published by the Free Software Foundation; either version 2*)
(*DBG: * of the License, or (at your option) any later version.*)
(*DBG: **)
(*DBG: * This program is distributed in the hope that it will be useful,*)
(*DBG: * but WITHOUT ANY WARRANTY; without even the implied warranty of*)
(*DBG: * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the*)
(*DBG: * GNU General Public License for more details.*)
(*DBG: **)
(*DBG: * You should have received a copy of the GNU General Public License*)
(*DBG: * along with this program; If not, see <http://www.gnu.org/licenses/>.*)
(*DBG: **)
(*DBG: */*)
(*DBG:*)
(*DBG:#include <stdbool.h>*)
(*DBG:*)
(*DBG:#include "iec_types_all.h"*)
(*DBG:#include "POUS.h"*)
(*DBG:*)
(*DBG:#define SAME_ENDIANNESS      0*)
(*DBG:#define REVERSE_ENDIANNESS   1*)
(*DBG:*)
(*DBG:uint8_t endianness;*)
(*DBG:*)
(*DBG:*)
(*DBG:extern FACTORYIO_DEMO RES0__INSTANCE0;*)
(*DBG:*)
(*DBG:static const struct {*)
(*DBG:    void *ptr;*)
(*DBG:    __IEC_types_enum type;*)
(*DBG:} debug_vars[] = {*)
(*DBG:    {&(RES0__INSTANCE0.START), BOOL_ENUM},*)
(*DBG:    {&(RES0__INSTANCE0.MAIN_CONVEYOR), BOOL_ENUM},*)
(*DBG:    {&(RES0__INSTANCE0.SCALE_CONVEYOR), BOOL_ENUM},*)
(*DBG:    {&(RES0__INSTANCE0.SEND_FORWARD), BOOL_ENUM},*)
(*DBG:    {&(RES0__INSTANCE0.SEND_LEFT), BOOL_ENUM},*)
(*DBG:    {&(RES0__INSTANCE0.SEND_RIGHT), BOOL_ENUM},*)
(*DBG:    {&(RES0__INSTANCE0.FRONT_CONVEYOR1), BOOL_ENUM},*)
(*DBG:    {&(RES0__INSTANCE0.FRONT_CONVEYOR2), BOOL_ENUM},*)
(*DBG:    {&(RES0__INSTANCE0.RIGHT_CONVEYOR1), BOOL_ENUM},*)
(*DBG:    {&(RES0__INSTANCE0.RIGHT_CONVEYOR2), BOOL_ENUM},*)
(*DBG:    {&(RES0__INSTANCE0.LEFT_CONVEYOR1), BOOL_ENUM},*)
(*DBG:    {&(RES0__INSTANCE0.LEFT_CONVEYOR2), BOOL_ENUM},*)
(*DBG:    {&(RES0__INSTANCE0.LEFT_ROLLER1), BOOL_ENUM},*)
(*DBG:    {&(RES0__INSTANCE0.LEFT_ROLLER2), BOOL_ENUM},*)
(*DBG:    {&(RES0__INSTANCE0.RIGHT_ROLLER1), BOOL_ENUM},*)
(*DBG:    {&(RES0__INSTANCE0.RIGHT_ROLLER2), BOOL_ENUM},*)
(*DBG:    {&(RES0__INSTANCE0.HEAVY_INDICATOR), BOOL_ENUM},*)
(*DBG:    {&(RES0__INSTANCE0.LIGHT_INDICATOR), BOOL_ENUM},*)
(*DBG:    {&(RES0__INSTANCE0.SCALE_SENSOR), BOOL_ENUM},*)
(*DBG:    {&(RES0__INSTANCE0.SCALE_TIMEOUT), BOOL_ENUM},*)
(*DBG:    {&(RES0__INSTANCE0.WAIT_TIME), INT_ENUM},*)
(*DBG:    {&(RES0__INSTANCE0.WEIGHT), INT_ENUM},*)
(*DBG:    {&(RES0__INSTANCE0.TON3.EN), BOOL_ENUM},*)
(*DBG:    {&(RES0__INSTANCE0.TON3.ENO), BOOL_ENUM},*)
(*DBG:    {&(RES0__INSTANCE0.TON3.IN), BOOL_ENUM},*)
(*DBG:    {&(RES0__INSTANCE0.TON3.PT), TIME_ENUM},*)
(*DBG:    {&(RES0__INSTANCE0.TON3.Q), BOOL_ENUM},*)
(*DBG:    {&(RES0__INSTANCE0.TON3.ET), TIME_ENUM},*)
(*DBG:    {&(RES0__INSTANCE0.TON3.STATE), SINT_ENUM},*)
(*DBG:    {&(RES0__INSTANCE0.TON3.PREV_IN), BOOL_ENUM},*)
(*DBG:    {&(RES0__INSTANCE0.TON3.CURRENT_TIME), TIME_ENUM},*)
(*DBG:    {&(RES0__INSTANCE0.TON3.START_TIME), TIME_ENUM},*)
(*DBG:    {&(RES0__INSTANCE0.TOF0.EN), BOOL_ENUM},*)
(*DBG:    {&(RES0__INSTANCE0.TOF0.ENO), BOOL_ENUM},*)
(*DBG:    {&(RES0__INSTANCE0.TOF0.IN), BOOL_ENUM},*)
(*DBG:    {&(RES0__INSTANCE0.TOF0.PT), TIME_ENUM},*)
(*DBG:    {&(RES0__INSTANCE0.TOF0.Q), BOOL_ENUM},*)
(*DBG:    {&(RES0__INSTANCE0.TOF0.ET), TIME_ENUM},*)
(*DBG:    {&(RES0__INSTANCE0.TOF0.STATE), SINT_ENUM},*)
(*DBG:    {&(RES0__INSTANCE0.TOF0.PREV_IN), BOOL_ENUM},*)
(*DBG:    {&(RES0__INSTANCE0.TOF0.CURRENT_TIME), TIME_ENUM},*)
(*DBG:    {&(RES0__INSTANCE0.TOF0.START_TIME), TIME_ENUM},*)
(*DBG:    {&(RES0__INSTANCE0.TOF1.EN), BOOL_ENUM},*)
(*DBG:    {&(RES0__INSTANCE0.TOF1.ENO), BOOL_ENUM},*)
(*DBG:    {&(RES0__INSTANCE0.TOF1.IN), BOOL_ENUM},*)
(*DBG:    {&(RES0__INSTANCE0.TOF1.PT), TIME_ENUM},*)
(*DBG:    {&(RES0__INSTANCE0.TOF1.Q), BOOL_ENUM},*)
(*DBG:    {&(RES0__INSTANCE0.TOF1.ET), TIME_ENUM},*)
(*DBG:    {&(RES0__INSTANCE0.TOF1.STATE), SINT_ENUM},*)
(*DBG:    {&(RES0__INSTANCE0.TOF1.PREV_IN), BOOL_ENUM},*)
(*DBG:    {&(RES0__INSTANCE0.TOF1.CURRENT_TIME), TIME_ENUM},*)
(*DBG:    {&(RES0__INSTANCE0.TOF1.START_TIME), TIME_ENUM},*)
(*DBG:    {&(RES0__INSTANCE0.LEFT_STICK_SENSOR), BOOL_ENUM},*)
(*DBG:    {&(RES0__INSTANCE0.RIGHT_STICK_SENSOR), BOOL_ENUM},*)
(*DBG:    {&(RES0__INSTANCE0.LEFT_STICK_DOWN), BOOL_ENUM},*)
(*DBG:    {&(RES0__INSTANCE0.LEFT_STICK_GRAB), BOOL_ENUM},*)
(*DBG:    {&(RES0__INSTANCE0.LEFT_STICK_LEFT_ROTATION), BOOL_ENUM},*)
(*DBG:    {&(RES0__INSTANCE0.LEFT_STICK_RIGHT_ROTATION), BOOL_ENUM},*)
(*DBG:    {&(RES0__INSTANCE0.LEFT_STICK_ENDEND), BOOL_ENUM},*)
(*DBG:    {&(RES0__INSTANCE0.RIGHT_STICK_DOWN), BOOL_ENUM},*)
(*DBG:    {&(RES0__INSTANCE0.RIGHT_STICK_GRAB), BOOL_ENUM},*)
(*DBG:    {&(RES0__INSTANCE0.RIGHT_STICK_LEFT_ROTATION), BOOL_ENUM},*)
(*DBG:    {&(RES0__INSTANCE0.RIGHT_STICK_RIGHT_ROTATION), BOOL_ENUM},*)
(*DBG:    {&(RES0__INSTANCE0.RIGHT_STICK_EXTEND), BOOL_ENUM},*)
(*DBG:    {&(RES0__INSTANCE0.TON4.EN), BOOL_ENUM},*)
(*DBG:    {&(RES0__INSTANCE0.TON4.ENO), BOOL_ENUM},*)
(*DBG:    {&(RES0__INSTANCE0.TON4.IN), BOOL_ENUM},*)
(*DBG:    {&(RES0__INSTANCE0.TON4.PT), TIME_ENUM},*)
(*DBG:    {&(RES0__INSTANCE0.TON4.Q), BOOL_ENUM},*)
(*DBG:    {&(RES0__INSTANCE0.TON4.ET), TIME_ENUM},*)
(*DBG:    {&(RES0__INSTANCE0.TON4.STATE), SINT_ENUM},*)
(*DBG:    {&(RES0__INSTANCE0.TON4.PREV_IN), BOOL_ENUM},*)
(*DBG:    {&(RES0__INSTANCE0.TON4.CURRENT_TIME), TIME_ENUM},*)
(*DBG:    {&(RES0__INSTANCE0.TON4.START_TIME), TIME_ENUM},*)
(*DBG:    {&(RES0__INSTANCE0.TON5.EN), BOOL_ENUM},*)
(*DBG:    {&(RES0__INSTANCE0.TON5.ENO), BOOL_ENUM},*)
(*DBG:    {&(RES0__INSTANCE0.TON5.IN), BOOL_ENUM},*)
(*DBG:    {&(RES0__INSTANCE0.TON5.PT), TIME_ENUM},*)
(*DBG:    {&(RES0__INSTANCE0.TON5.Q), BOOL_ENUM},*)
(*DBG:    {&(RES0__INSTANCE0.TON5.ET), TIME_ENUM},*)
(*DBG:    {&(RES0__INSTANCE0.TON5.STATE), SINT_ENUM},*)
(*DBG:    {&(RES0__INSTANCE0.TON5.PREV_IN), BOOL_ENUM},*)
(*DBG:    {&(RES0__INSTANCE0.TON5.CURRENT_TIME), TIME_ENUM},*)
(*DBG:    {&(RES0__INSTANCE0.TON5.START_TIME), TIME_ENUM},*)
(*DBG:    {&(RES0__INSTANCE0.TON6.EN), BOOL_ENUM},*)
(*DBG:    {&(RES0__INSTANCE0.TON6.ENO), BOOL_ENUM},*)
(*DBG:    {&(RES0__INSTANCE0.TON6.IN), BOOL_ENUM},*)
(*DBG:    {&(RES0__INSTANCE0.TON6.PT), TIME_ENUM},*)
(*DBG:    {&(RES0__INSTANCE0.TON6.Q), BOOL_ENUM},*)
(*DBG:    {&(RES0__INSTANCE0.TON6.ET), TIME_ENUM},*)
(*DBG:    {&(RES0__INSTANCE0.TON6.STATE), SINT_ENUM},*)
(*DBG:    {&(RES0__INSTANCE0.TON6.PREV_IN), BOOL_ENUM},*)
(*DBG:    {&(RES0__INSTANCE0.TON6.CURRENT_TIME), TIME_ENUM},*)
(*DBG:    {&(RES0__INSTANCE0.TON6.START_TIME), TIME_ENUM},*)
(*DBG:    {&(RES0__INSTANCE0.TON7.EN), BOOL_ENUM},*)
(*DBG:    {&(RES0__INSTANCE0.TON7.ENO), BOOL_ENUM},*)
(*DBG:    {&(RES0__INSTANCE0.TON7.IN), BOOL_ENUM},*)
(*DBG:    {&(RES0__INSTANCE0.TON7.PT), TIME_ENUM},*)
(*DBG:    {&(RES0__INSTANCE0.TON7.Q), BOOL_ENUM},*)
(*DBG:    {&(RES0__INSTANCE0.TON7.ET), TIME_ENUM},*)
(*DBG:    {&(RES0__INSTANCE0.TON7.STATE), SINT_ENUM},*)
(*DBG:    {&(RES0__INSTANCE0.TON7.PREV_IN), BOOL_ENUM},*)
(*DBG:    {&(RES0__INSTANCE0.TON7.CURRENT_TIME), TIME_ENUM},*)
(*DBG:    {&(RES0__INSTANCE0.TON7.START_TIME), TIME_ENUM},*)
(*DBG:    {&(RES0__INSTANCE0.TON8.EN), BOOL_ENUM},*)
(*DBG:    {&(RES0__INSTANCE0.TON8.ENO), BOOL_ENUM},*)
(*DBG:    {&(RES0__INSTANCE0.TON8.IN), BOOL_ENUM},*)
(*DBG:    {&(RES0__INSTANCE0.TON8.PT), TIME_ENUM},*)
(*DBG:    {&(RES0__INSTANCE0.TON8.Q), BOOL_ENUM},*)
(*DBG:    {&(RES0__INSTANCE0.TON8.ET), TIME_ENUM},*)
(*DBG:    {&(RES0__INSTANCE0.TON8.STATE), SINT_ENUM},*)
(*DBG:    {&(RES0__INSTANCE0.TON8.PREV_IN), BOOL_ENUM},*)
(*DBG:    {&(RES0__INSTANCE0.TON8.CURRENT_TIME), TIME_ENUM},*)
(*DBG:    {&(RES0__INSTANCE0.TON8.START_TIME), TIME_ENUM},*)
(*DBG:    {&(RES0__INSTANCE0.TON9.EN), BOOL_ENUM},*)
(*DBG:    {&(RES0__INSTANCE0.TON9.ENO), BOOL_ENUM},*)
(*DBG:    {&(RES0__INSTANCE0.TON9.IN), BOOL_ENUM},*)
(*DBG:    {&(RES0__INSTANCE0.TON9.PT), TIME_ENUM},*)
(*DBG:    {&(RES0__INSTANCE0.TON9.Q), BOOL_ENUM},*)
(*DBG:    {&(RES0__INSTANCE0.TON9.ET), TIME_ENUM},*)
(*DBG:    {&(RES0__INSTANCE0.TON9.STATE), SINT_ENUM},*)
(*DBG:    {&(RES0__INSTANCE0.TON9.PREV_IN), BOOL_ENUM},*)
(*DBG:    {&(RES0__INSTANCE0.TON9.CURRENT_TIME), TIME_ENUM},*)
(*DBG:    {&(RES0__INSTANCE0.TON9.START_TIME), TIME_ENUM},*)
(*DBG:    {&(RES0__INSTANCE0.TON10.EN), BOOL_ENUM},*)
(*DBG:    {&(RES0__INSTANCE0.TON10.ENO), BOOL_ENUM},*)
(*DBG:    {&(RES0__INSTANCE0.TON10.IN), BOOL_ENUM},*)
(*DBG:    {&(RES0__INSTANCE0.TON10.PT), TIME_ENUM},*)
(*DBG:    {&(RES0__INSTANCE0.TON10.Q), BOOL_ENUM},*)
(*DBG:    {&(RES0__INSTANCE0.TON10.ET), TIME_ENUM},*)
(*DBG:    {&(RES0__INSTANCE0.TON10.STATE), SINT_ENUM},*)
(*DBG:    {&(RES0__INSTANCE0.TON10.PREV_IN), BOOL_ENUM},*)
(*DBG:    {&(RES0__INSTANCE0.TON10.CURRENT_TIME), TIME_ENUM},*)
(*DBG:    {&(RES0__INSTANCE0.TON10.START_TIME), TIME_ENUM},*)
(*DBG:    {&(RES0__INSTANCE0.TON2.EN), BOOL_ENUM},*)
(*DBG:    {&(RES0__INSTANCE0.TON2.ENO), BOOL_ENUM},*)
(*DBG:    {&(RES0__INSTANCE0.TON2.IN), BOOL_ENUM},*)
(*DBG:    {&(RES0__INSTANCE0.TON2.PT), TIME_ENUM},*)
(*DBG:    {&(RES0__INSTANCE0.TON2.Q), BOOL_ENUM},*)
(*DBG:    {&(RES0__INSTANCE0.TON2.ET), TIME_ENUM},*)
(*DBG:    {&(RES0__INSTANCE0.TON2.STATE), SINT_ENUM},*)
(*DBG:    {&(RES0__INSTANCE0.TON2.PREV_IN), BOOL_ENUM},*)
(*DBG:    {&(RES0__INSTANCE0.TON2.CURRENT_TIME), TIME_ENUM},*)
(*DBG:    {&(RES0__INSTANCE0.TON2.START_TIME), TIME_ENUM},*)
(*DBG:    {&(RES0__INSTANCE0.TOF2.EN), BOOL_ENUM},*)
(*DBG:    {&(RES0__INSTANCE0.TOF2.ENO), BOOL_ENUM},*)
(*DBG:    {&(RES0__INSTANCE0.TOF2.IN), BOOL_ENUM},*)
(*DBG:    {&(RES0__INSTANCE0.TOF2.PT), TIME_ENUM},*)
(*DBG:    {&(RES0__INSTANCE0.TOF2.Q), BOOL_ENUM},*)
(*DBG:    {&(RES0__INSTANCE0.TOF2.ET), TIME_ENUM},*)
(*DBG:    {&(RES0__INSTANCE0.TOF2.STATE), SINT_ENUM},*)
(*DBG:    {&(RES0__INSTANCE0.TOF2.PREV_IN), BOOL_ENUM},*)
(*DBG:    {&(RES0__INSTANCE0.TOF2.CURRENT_TIME), TIME_ENUM},*)
(*DBG:    {&(RES0__INSTANCE0.TOF2.START_TIME), TIME_ENUM},*)
(*DBG:    {&(RES0__INSTANCE0.TOF3.EN), BOOL_ENUM},*)
(*DBG:    {&(RES0__INSTANCE0.TOF3.ENO), BOOL_ENUM},*)
(*DBG:    {&(RES0__INSTANCE0.TOF3.IN), BOOL_ENUM},*)
(*DBG:    {&(RES0__INSTANCE0.TOF3.PT), TIME_ENUM},*)
(*DBG:    {&(RES0__INSTANCE0.TOF3.Q), BOOL_ENUM},*)
(*DBG:    {&(RES0__INSTANCE0.TOF3.ET), TIME_ENUM},*)
(*DBG:    {&(RES0__INSTANCE0.TOF3.STATE), SINT_ENUM},*)
(*DBG:    {&(RES0__INSTANCE0.TOF3.PREV_IN), BOOL_ENUM},*)
(*DBG:    {&(RES0__INSTANCE0.TOF3.CURRENT_TIME), TIME_ENUM},*)
(*DBG:    {&(RES0__INSTANCE0.TOF3.START_TIME), TIME_ENUM},*)
(*DBG:    {&(RES0__INSTANCE0.TOF4.EN), BOOL_ENUM},*)
(*DBG:    {&(RES0__INSTANCE0.TOF4.ENO), BOOL_ENUM},*)
(*DBG:    {&(RES0__INSTANCE0.TOF4.IN), BOOL_ENUM},*)
(*DBG:    {&(RES0__INSTANCE0.TOF4.PT), TIME_ENUM},*)
(*DBG:    {&(RES0__INSTANCE0.TOF4.Q), BOOL_ENUM},*)
(*DBG:    {&(RES0__INSTANCE0.TOF4.ET), TIME_ENUM},*)
(*DBG:    {&(RES0__INSTANCE0.TOF4.STATE), SINT_ENUM},*)
(*DBG:    {&(RES0__INSTANCE0.TOF4.PREV_IN), BOOL_ENUM},*)
(*DBG:    {&(RES0__INSTANCE0.TOF4.CURRENT_TIME), TIME_ENUM},*)
(*DBG:    {&(RES0__INSTANCE0.TOF4.START_TIME), TIME_ENUM},*)
(*DBG:    {&(RES0__INSTANCE0.TOF5.EN), BOOL_ENUM},*)
(*DBG:    {&(RES0__INSTANCE0.TOF5.ENO), BOOL_ENUM},*)
(*DBG:    {&(RES0__INSTANCE0.TOF5.IN), BOOL_ENUM},*)
(*DBG:    {&(RES0__INSTANCE0.TOF5.PT), TIME_ENUM},*)
(*DBG:    {&(RES0__INSTANCE0.TOF5.Q), BOOL_ENUM},*)
(*DBG:    {&(RES0__INSTANCE0.TOF5.ET), TIME_ENUM},*)
(*DBG:    {&(RES0__INSTANCE0.TOF5.STATE), SINT_ENUM},*)
(*DBG:    {&(RES0__INSTANCE0.TOF5.PREV_IN), BOOL_ENUM},*)
(*DBG:    {&(RES0__INSTANCE0.TOF5.CURRENT_TIME), TIME_ENUM},*)
(*DBG:    {&(RES0__INSTANCE0.TOF5.START_TIME), TIME_ENUM},*)
(*DBG:    {&(RES0__INSTANCE0.RIGHT_GODOWN1), BOOL_ENUM},*)
(*DBG:    {&(RES0__INSTANCE0.RIGHT_GODOWN2), BOOL_ENUM},*)
(*DBG:    {&(RES0__INSTANCE0.LEFT_GODOWN1), BOOL_ENUM},*)
(*DBG:    {&(RES0__INSTANCE0.LEFT_GODOWN2), BOOL_ENUM},*)
(*DBG:    {&(RES0__INSTANCE0.START_RIGHT_ROLLER1), BOOL_ENUM},*)
(*DBG:    {&(RES0__INSTANCE0.START_LEFT_ROLLER1), BOOL_ENUM},*)
(*DBG:    {&(RES0__INSTANCE0.CTU0.EN), BOOL_ENUM},*)
(*DBG:    {&(RES0__INSTANCE0.CTU0.ENO), BOOL_ENUM},*)
(*DBG:    {&(RES0__INSTANCE0.CTU0.CU), BOOL_ENUM},*)
(*DBG:    {&(RES0__INSTANCE0.CTU0.R), BOOL_ENUM},*)
(*DBG:    {&(RES0__INSTANCE0.CTU0.PV), INT_ENUM},*)
(*DBG:    {&(RES0__INSTANCE0.CTU0.Q), BOOL_ENUM},*)
(*DBG:    {&(RES0__INSTANCE0.CTU0.CV), INT_ENUM},*)
(*DBG:    {&(RES0__INSTANCE0.CTU0.CU_T.EN), BOOL_ENUM},*)
(*DBG:    {&(RES0__INSTANCE0.CTU0.CU_T.ENO), BOOL_ENUM},*)
(*DBG:    {&(RES0__INSTANCE0.CTU0.CU_T.CLK), BOOL_ENUM},*)
(*DBG:    {&(RES0__INSTANCE0.CTU0.CU_T.Q), BOOL_ENUM},*)
(*DBG:    {&(RES0__INSTANCE0.CTU0.CU_T.M), BOOL_ENUM},*)
(*DBG:    {&(RES0__INSTANCE0.CTU1.EN), BOOL_ENUM},*)
(*DBG:    {&(RES0__INSTANCE0.CTU1.ENO), BOOL_ENUM},*)
(*DBG:    {&(RES0__INSTANCE0.CTU1.CU), BOOL_ENUM},*)
(*DBG:    {&(RES0__INSTANCE0.CTU1.R), BOOL_ENUM},*)
(*DBG:    {&(RES0__INSTANCE0.CTU1.PV), INT_ENUM},*)
(*DBG:    {&(RES0__INSTANCE0.CTU1.Q), BOOL_ENUM},*)
(*DBG:    {&(RES0__INSTANCE0.CTU1.CV), INT_ENUM},*)
(*DBG:    {&(RES0__INSTANCE0.CTU1.CU_T.EN), BOOL_ENUM},*)
(*DBG:    {&(RES0__INSTANCE0.CTU1.CU_T.ENO), BOOL_ENUM},*)
(*DBG:    {&(RES0__INSTANCE0.CTU1.CU_T.CLK), BOOL_ENUM},*)
(*DBG:    {&(RES0__INSTANCE0.CTU1.CU_T.Q), BOOL_ENUM},*)
(*DBG:    {&(RES0__INSTANCE0.CTU1.CU_T.M), BOOL_ENUM},*)
(*DBG:    {&(RES0__INSTANCE0.TOF6.EN), BOOL_ENUM},*)
(*DBG:    {&(RES0__INSTANCE0.TOF6.ENO), BOOL_ENUM},*)
(*DBG:    {&(RES0__INSTANCE0.TOF6.IN), BOOL_ENUM},*)
(*DBG:    {&(RES0__INSTANCE0.TOF6.PT), TIME_ENUM},*)
(*DBG:    {&(RES0__INSTANCE0.TOF6.Q), BOOL_ENUM},*)
(*DBG:    {&(RES0__INSTANCE0.TOF6.ET), TIME_ENUM},*)
(*DBG:    {&(RES0__INSTANCE0.TOF6.STATE), SINT_ENUM},*)
(*DBG:    {&(RES0__INSTANCE0.TOF6.PREV_IN), BOOL_ENUM},*)
(*DBG:    {&(RES0__INSTANCE0.TOF6.CURRENT_TIME), TIME_ENUM},*)
(*DBG:    {&(RES0__INSTANCE0.TOF6.START_TIME), TIME_ENUM},*)
(*DBG:    {&(RES0__INSTANCE0.TOF7.EN), BOOL_ENUM},*)
(*DBG:    {&(RES0__INSTANCE0.TOF7.ENO), BOOL_ENUM},*)
(*DBG:    {&(RES0__INSTANCE0.TOF7.IN), BOOL_ENUM},*)
(*DBG:    {&(RES0__INSTANCE0.TOF7.PT), TIME_ENUM},*)
(*DBG:    {&(RES0__INSTANCE0.TOF7.Q), BOOL_ENUM},*)
(*DBG:    {&(RES0__INSTANCE0.TOF7.ET), TIME_ENUM},*)
(*DBG:    {&(RES0__INSTANCE0.TOF7.STATE), SINT_ENUM},*)
(*DBG:    {&(RES0__INSTANCE0.TOF7.PREV_IN), BOOL_ENUM},*)
(*DBG:    {&(RES0__INSTANCE0.TOF7.CURRENT_TIME), TIME_ENUM},*)
(*DBG:    {&(RES0__INSTANCE0.TOF7.START_TIME), TIME_ENUM},*)
(*DBG:    {&(RES0__INSTANCE0._TMP_GE18_OUT), BOOL_ENUM},*)
(*DBG:    {&(RES0__INSTANCE0._TMP_LE16_OUT), BOOL_ENUM},*)
(*DBG:    {&(RES0__INSTANCE0.R_TRIG1.EN), BOOL_ENUM},*)
(*DBG:    {&(RES0__INSTANCE0.R_TRIG1.ENO), BOOL_ENUM},*)
(*DBG:    {&(RES0__INSTANCE0.R_TRIG1.CLK), BOOL_ENUM},*)
(*DBG:    {&(RES0__INSTANCE0.R_TRIG1.Q), BOOL_ENUM},*)
(*DBG:    {&(RES0__INSTANCE0.R_TRIG1.M), BOOL_ENUM},*)
(*DBG:    {&(RES0__INSTANCE0.F_TRIG1.EN), BOOL_ENUM},*)
(*DBG:    {&(RES0__INSTANCE0.F_TRIG1.ENO), BOOL_ENUM},*)
(*DBG:    {&(RES0__INSTANCE0.F_TRIG1.CLK), BOOL_ENUM},*)
(*DBG:    {&(RES0__INSTANCE0.F_TRIG1.Q), BOOL_ENUM},*)
(*DBG:    {&(RES0__INSTANCE0.F_TRIG1.M), BOOL_ENUM},*)
(*DBG:    {&(RES0__INSTANCE0.R_TRIG2.EN), BOOL_ENUM},*)
(*DBG:    {&(RES0__INSTANCE0.R_TRIG2.ENO), BOOL_ENUM},*)
(*DBG:    {&(RES0__INSTANCE0.R_TRIG2.CLK), BOOL_ENUM},*)
(*DBG:    {&(RES0__INSTANCE0.R_TRIG2.Q), BOOL_ENUM},*)
(*DBG:    {&(RES0__INSTANCE0.R_TRIG2.M), BOOL_ENUM},*)
(*DBG:    {&(RES0__INSTANCE0.F_TRIG2.EN), BOOL_ENUM},*)
(*DBG:    {&(RES0__INSTANCE0.F_TRIG2.ENO), BOOL_ENUM},*)
(*DBG:    {&(RES0__INSTANCE0.F_TRIG2.CLK), BOOL_ENUM},*)
(*DBG:    {&(RES0__INSTANCE0.F_TRIG2.Q), BOOL_ENUM},*)
(*DBG:    {&(RES0__INSTANCE0.F_TRIG2.M), BOOL_ENUM},*)
(*DBG:};*)
(*DBG:*)
(*DBG:#define VAR_COUNT               256*)
(*DBG:*)
(*DBG:uint16_t get_var_count(void)*)
(*DBG:{*)
(*DBG:    return VAR_COUNT;*)
(*DBG:}*)
(*DBG:*)
(*DBG:size_t get_var_size(size_t idx)*)
(*DBG:{*)
(*DBG:    if (idx >= VAR_COUNT)*)
(*DBG:    {*)
(*DBG:        return 0;*)
(*DBG:    }*)
(*DBG:    switch (debug_vars[idx].type) {*)
(*DBG:    case BOOL_ENUM:*)
(*DBG:        return sizeof(BOOL);*)
(*DBG:    case SINT_ENUM:*)
(*DBG:        return sizeof(SINT);*)
(*DBG:    case TIME_ENUM:*)
(*DBG:        return sizeof(TIME);*)
(*DBG:    case INT_ENUM:*)
(*DBG:        return sizeof(INT);*)
(*DBG:    default:*)
(*DBG:        return 0;*)
(*DBG:    }*)
(*DBG:}*)
(*DBG:*)
(*DBG:void *get_var_addr(size_t idx)*)
(*DBG:{*)
(*DBG:    void *ptr = debug_vars[idx].ptr;*)
(*DBG:*)
(*DBG:    switch (debug_vars[idx].type) {*)
(*DBG:    case BOOL_ENUM:*)
(*DBG:        return (void *)&((__IEC_BOOL_t *) ptr)->value;*)
(*DBG:    case SINT_ENUM:*)
(*DBG:        return (void *)&((__IEC_SINT_t *) ptr)->value;*)
(*DBG:    case TIME_ENUM:*)
(*DBG:        return (void *)&((__IEC_TIME_t *) ptr)->value;*)
(*DBG:    case INT_ENUM:*)
(*DBG:        return (void *)&((__IEC_INT_t *) ptr)->value;*)
(*DBG:    default:*)
(*DBG:        return 0;*)
(*DBG:    }*)
(*DBG:}*)
(*DBG:*)
(*DBG:void force_var(size_t idx, bool forced, void *val)*)
(*DBG:{*)
(*DBG:    void *ptr = debug_vars[idx].ptr;*)
(*DBG:*)
(*DBG:    if (forced) {*)
(*DBG:        size_t var_size = get_var_size(idx);*)
(*DBG:        switch (debug_vars[idx].type) {*)
(*DBG:        case BOOL_ENUM: {*)
(*DBG:            memcpy(&((__IEC_BOOL_t *) ptr)->value, val, var_size);*)
(*DBG:            //((__IEC_BOOL_t *) ptr)->value = *((BOOL *) val);*)
(*DBG:            ((__IEC_BOOL_t *) ptr)->flags |= __IEC_FORCE_FLAG;*)
(*DBG:            break;*)
(*DBG:        }*)
(*DBG:        case SINT_ENUM: {*)
(*DBG:            memcpy(&((__IEC_SINT_t *) ptr)->value, val, var_size);*)
(*DBG:            //((__IEC_SINT_t *) ptr)->value = *((SINT *) val);*)
(*DBG:            ((__IEC_SINT_t *) ptr)->flags |= __IEC_FORCE_FLAG;*)
(*DBG:            break;*)
(*DBG:        }*)
(*DBG:        case TIME_ENUM: {*)
(*DBG:            memcpy(&((__IEC_TIME_t *) ptr)->value, val, var_size);*)
(*DBG:            //((__IEC_TIME_t *) ptr)->value = *((TIME *) val);*)
(*DBG:            ((__IEC_TIME_t *) ptr)->flags |= __IEC_FORCE_FLAG;*)
(*DBG:            break;*)
(*DBG:        }*)
(*DBG:        case INT_ENUM: {*)
(*DBG:            memcpy(&((__IEC_INT_t *) ptr)->value, val, var_size);*)
(*DBG:            //((__IEC_INT_t *) ptr)->value = *((INT *) val);*)
(*DBG:            ((__IEC_INT_t *) ptr)->flags |= __IEC_FORCE_FLAG;*)
(*DBG:            break;*)
(*DBG:        }*)
(*DBG:        default:*)
(*DBG:            break;*)
(*DBG:        }*)
(*DBG:    } else {*)
(*DBG:        switch (debug_vars[idx].type) {*)
(*DBG:        case BOOL_ENUM:*)
(*DBG:            ((__IEC_BOOL_t *) ptr)->flags &= ~__IEC_FORCE_FLAG;*)
(*DBG:            break;*)
(*DBG:        case SINT_ENUM:*)
(*DBG:            ((__IEC_SINT_t *) ptr)->flags &= ~__IEC_FORCE_FLAG;*)
(*DBG:            break;*)
(*DBG:        case TIME_ENUM:*)
(*DBG:            ((__IEC_TIME_t *) ptr)->flags &= ~__IEC_FORCE_FLAG;*)
(*DBG:            break;*)
(*DBG:        case INT_ENUM:*)
(*DBG:            ((__IEC_INT_t *) ptr)->flags &= ~__IEC_FORCE_FLAG;*)
(*DBG:            break;*)
(*DBG:        default:*)
(*DBG:            break;*)
(*DBG:        }*)
(*DBG:    }*)
(*DBG:}*)
(*DBG:*)
(*DBG:void swap_bytes(void *ptr, size_t size) *)
(*DBG:{*)
(*DBG:    uint8_t *bytePtr = (uint8_t *)ptr;*)
(*DBG:    size_t i;*)
(*DBG:    for (i = 0; i < size / 2; ++i) *)
(*DBG:    {*)
(*DBG:        uint8_t temp = bytePtr[i];*)
(*DBG:        bytePtr[i] = bytePtr[size - 1 - i];*)
(*DBG:        bytePtr[size - 1 - i] = temp;*)
(*DBG:    }*)
(*DBG:}*)
(*DBG:*)
(*DBG:void trace_reset(void)*)
(*DBG:{*)
(*DBG:    for (size_t i=0; i < VAR_COUNT; i++) *)
(*DBG:    {*)
(*DBG:        force_var(i, false, 0);*)
(*DBG:    }*)
(*DBG:}*)
(*DBG:*)
(*DBG:void set_trace(size_t idx, bool forced, void *val)*)
(*DBG:{*)
(*DBG:    if (idx >= 0 && idx < VAR_COUNT) *)
(*DBG:    {*)
(*DBG:        if (endianness == REVERSE_ENDIANNESS)*)
(*DBG:        {*)
(*DBG:            // Aaaaarghhhh... Stupid AVR is Big Endian.*)
(*DBG:            swap_bytes(val, get_var_size(idx));*)
(*DBG:        }*)
(*DBG:*)
(*DBG:        force_var(idx, forced, val);*)
(*DBG:    }*)
(*DBG:}*)
(*DBG:*)
(*DBG:void set_endianness(uint8_t value)*)
(*DBG:{*)
(*DBG:    if (value == SAME_ENDIANNESS || value == REVERSE_ENDIANNESS)*)
(*DBG:    {*)
(*DBG:        endianness = value;*)
(*DBG:    }*)
(*DBG:}*)
(*DBG:*)
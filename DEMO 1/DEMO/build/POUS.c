void LOGGER_init__(LOGGER *data__, BOOL retain) {
  __INIT_VAR(data__->EN,__BOOL_LITERAL(TRUE),retain)
  __INIT_VAR(data__->ENO,__BOOL_LITERAL(TRUE),retain)
  __INIT_VAR(data__->TRIG,__BOOL_LITERAL(FALSE),retain)
  __INIT_VAR(data__->MSG,__STRING_LITERAL(0,""),retain)
  __INIT_VAR(data__->LEVEL,LOGLEVEL__INFO,retain)
  __INIT_VAR(data__->TRIG0,__BOOL_LITERAL(FALSE),retain)
}

// Code part
void LOGGER_body__(LOGGER *data__) {
  // Control execution
  if (!__GET_VAR(data__->EN)) {
    __SET_VAR(data__->,ENO,,__BOOL_LITERAL(FALSE));
    return;
  }
  else {
    __SET_VAR(data__->,ENO,,__BOOL_LITERAL(TRUE));
  }
  // Initialise TEMP variables

  if ((__GET_VAR(data__->TRIG,) && !(__GET_VAR(data__->TRIG0,)))) {
    #define GetFbVar(var,...) __GET_VAR(data__->var,__VA_ARGS__)
    #define SetFbVar(var,val,...) __SET_VAR(data__->,var,__VA_ARGS__,val)

   LogMessage(GetFbVar(LEVEL),(char*)GetFbVar(MSG, .body),GetFbVar(MSG, .len));
  
    #undef GetFbVar
    #undef SetFbVar
;
  };
  __SET_VAR(data__->,TRIG0,,__GET_VAR(data__->TRIG,));

  goto __end;

__end:
  return;
} // LOGGER_body__() 





void FACTORYIO_DEMO_init__(FACTORYIO_DEMO *data__, BOOL retain) {
  __INIT_VAR(data__->START,__BOOL_LITERAL(FALSE),retain)
  __INIT_VAR(data__->MAIN_CONVEYOR,__BOOL_LITERAL(FALSE),retain)
  __INIT_VAR(data__->SCALE_CONVEYOR,__BOOL_LITERAL(FALSE),retain)
  __INIT_VAR(data__->SEND_FORWARD,__BOOL_LITERAL(FALSE),retain)
  __INIT_VAR(data__->SEND_LEFT,__BOOL_LITERAL(FALSE),retain)
  __INIT_VAR(data__->SEND_RIGHT,__BOOL_LITERAL(FALSE),retain)
  __INIT_VAR(data__->FRONT_CONVEYOR1,__BOOL_LITERAL(FALSE),retain)
  __INIT_VAR(data__->FRONT_CONVEYOR2,__BOOL_LITERAL(FALSE),retain)
  __INIT_VAR(data__->RIGHT_CONVEYOR1,__BOOL_LITERAL(FALSE),retain)
  __INIT_VAR(data__->RIGHT_CONVEYOR2,__BOOL_LITERAL(FALSE),retain)
  __INIT_VAR(data__->LEFT_CONVEYOR1,__BOOL_LITERAL(FALSE),retain)
  __INIT_VAR(data__->LEFT_CONVEYOR2,__BOOL_LITERAL(FALSE),retain)
  __INIT_VAR(data__->LEFT_ROLLER1,__BOOL_LITERAL(FALSE),retain)
  __INIT_VAR(data__->LEFT_ROLLER2,__BOOL_LITERAL(FALSE),retain)
  __INIT_VAR(data__->RIGHT_ROLLER1,__BOOL_LITERAL(FALSE),retain)
  __INIT_VAR(data__->RIGHT_ROLLER2,__BOOL_LITERAL(FALSE),retain)
  __INIT_VAR(data__->HEAVY_INDICATOR,__BOOL_LITERAL(FALSE),retain)
  __INIT_VAR(data__->LIGHT_INDICATOR,__BOOL_LITERAL(FALSE),retain)
  __INIT_VAR(data__->SCALE_SENSOR,__BOOL_LITERAL(FALSE),retain)
  __INIT_VAR(data__->SCALE_TIMEOUT,__BOOL_LITERAL(FALSE),retain)
  __INIT_VAR(data__->WAIT_TIME,2,retain)
  __INIT_VAR(data__->WEIGHT,0,retain)
  TON_init__(&data__->TON3,retain);
  TOF_init__(&data__->TOF0,retain);
  TOF_init__(&data__->TOF1,retain);
  __INIT_VAR(data__->LEFT_STICK_SENSOR,__BOOL_LITERAL(FALSE),retain)
  __INIT_VAR(data__->RIGHT_STICK_SENSOR,__BOOL_LITERAL(FALSE),retain)
  __INIT_VAR(data__->LEFT_STICK_DOWN,__BOOL_LITERAL(FALSE),retain)
  __INIT_VAR(data__->LEFT_STICK_GRAB,__BOOL_LITERAL(FALSE),retain)
  __INIT_VAR(data__->LEFT_STICK_LEFT_ROTATION,__BOOL_LITERAL(FALSE),retain)
  __INIT_VAR(data__->LEFT_STICK_RIGHT_ROTATION,__BOOL_LITERAL(FALSE),retain)
  __INIT_VAR(data__->LEFT_STICK_ENDEND,__BOOL_LITERAL(FALSE),retain)
  __INIT_VAR(data__->RIGHT_STICK_DOWN,__BOOL_LITERAL(FALSE),retain)
  __INIT_VAR(data__->RIGHT_STICK_GRAB,__BOOL_LITERAL(FALSE),retain)
  __INIT_VAR(data__->RIGHT_STICK_LEFT_ROTATION,__BOOL_LITERAL(FALSE),retain)
  __INIT_VAR(data__->RIGHT_STICK_RIGHT_ROTATION,__BOOL_LITERAL(FALSE),retain)
  __INIT_VAR(data__->RIGHT_STICK_EXTEND,__BOOL_LITERAL(FALSE),retain)
  TON_init__(&data__->TON4,retain);
  TON_init__(&data__->TON5,retain);
  TON_init__(&data__->TON6,retain);
  TON_init__(&data__->TON7,retain);
  TON_init__(&data__->TON8,retain);
  TON_init__(&data__->TON9,retain);
  TON_init__(&data__->TON10,retain);
  TON_init__(&data__->TON2,retain);
  TOF_init__(&data__->TOF2,retain);
  TOF_init__(&data__->TOF3,retain);
  TOF_init__(&data__->TOF4,retain);
  TOF_init__(&data__->TOF5,retain);
  __INIT_VAR(data__->RIGHT_GODOWN1,__BOOL_LITERAL(FALSE),retain)
  __INIT_VAR(data__->RIGHT_GODOWN2,__BOOL_LITERAL(FALSE),retain)
  __INIT_VAR(data__->LEFT_GODOWN1,__BOOL_LITERAL(FALSE),retain)
  __INIT_VAR(data__->LEFT_GODOWN2,__BOOL_LITERAL(FALSE),retain)
  __INIT_VAR(data__->START_RIGHT_ROLLER1,__BOOL_LITERAL(FALSE),retain)
  __INIT_VAR(data__->START_LEFT_ROLLER1,__BOOL_LITERAL(FALSE),retain)
  CTU_init__(&data__->CTU0,retain);
  CTU_init__(&data__->CTU1,retain);
  TOF_init__(&data__->TOF6,retain);
  TOF_init__(&data__->TOF7,retain);
  __INIT_VAR(data__->_TMP_GE18_OUT,__BOOL_LITERAL(FALSE),retain)
  __INIT_VAR(data__->_TMP_LE16_OUT,__BOOL_LITERAL(FALSE),retain)
  R_TRIG_init__(&data__->R_TRIG1,retain);
  F_TRIG_init__(&data__->F_TRIG1,retain);
  R_TRIG_init__(&data__->R_TRIG2,retain);
  F_TRIG_init__(&data__->F_TRIG2,retain);
}

// Code part
void FACTORYIO_DEMO_body__(FACTORYIO_DEMO *data__) {
  // Initialise TEMP variables

  __SET_VAR(data__->,LEFT_CONVEYOR1,,__BOOL_LITERAL(TRUE));
  __SET_VAR(data__->,FRONT_CONVEYOR2,,__BOOL_LITERAL(TRUE));
  __SET_VAR(data__->,RIGHT_CONVEYOR1,,__BOOL_LITERAL(TRUE));
  __SET_VAR(data__->TON3.,IN,,__GET_VAR(data__->SCALE_SENSOR,));
  __SET_VAR(data__->TON3.,PT,,__time_to_timespec(1, 1500, 0, 0, 0, 0));
  TON_body__(&data__->TON3);
  __SET_VAR(data__->,SCALE_TIMEOUT,,__GET_VAR(data__->TON3.Q,));
  __SET_VAR(data__->TOF0.,IN,,(__GET_VAR(data__->LIGHT_INDICATOR,) && __GET_VAR(data__->SCALE_SENSOR,)));
  __SET_VAR(data__->TOF0.,PT,,__time_to_timespec(1, 2200, 0, 0, 0, 0));
  TOF_body__(&data__->TOF0);
  __SET_VAR(data__->,SEND_LEFT,,__GET_VAR(data__->TOF0.Q,));
  __SET_VAR(data__->TOF1.,IN,,((!(__GET_VAR(data__->HEAVY_INDICATOR,)) && !(__GET_VAR(data__->LIGHT_INDICATOR,))) && __GET_VAR(data__->SCALE_SENSOR,)));
  __SET_VAR(data__->TOF1.,PT,,__time_to_timespec(1, 2200, 0, 0, 0, 0));
  TOF_body__(&data__->TOF1);
  __SET_VAR(data__->,SEND_RIGHT,,__GET_VAR(data__->TOF1.Q,));
  __SET_VAR(data__->,SEND_FORWARD,,__BOOL_LITERAL(TRUE));
  __SET_VAR(data__->,MAIN_CONVEYOR,,(!(__GET_VAR(data__->SCALE_SENSOR,)) || __GET_VAR(data__->SCALE_TIMEOUT,)));
  __SET_VAR(data__->,_TMP_GE18_OUT,,GE__BOOL__INT(
    (BOOL)__BOOL_LITERAL(TRUE),
    NULL,
    (UINT)2,
    (INT)__GET_VAR(data__->WEIGHT,),
    (INT)600));
  __SET_VAR(data__->,HEAVY_INDICATOR,,__GET_VAR(data__->_TMP_GE18_OUT,));
  __SET_VAR(data__->,_TMP_LE16_OUT,,LE__BOOL__INT(
    (BOOL)__BOOL_LITERAL(TRUE),
    NULL,
    (UINT)2,
    (INT)__GET_VAR(data__->WEIGHT,),
    (INT)250));
  __SET_VAR(data__->,LIGHT_INDICATOR,,__GET_VAR(data__->_TMP_LE16_OUT,));
  __SET_VAR(data__->,SCALE_CONVEYOR,,(!(__GET_VAR(data__->SCALE_SENSOR,)) || __GET_VAR(data__->SCALE_TIMEOUT,)));
  __SET_VAR(data__->,LEFT_CONVEYOR2,,!(__GET_VAR(data__->LEFT_STICK_SENSOR,)));
  __SET_VAR(data__->,RIGHT_CONVEYOR2,,!(__GET_VAR(data__->RIGHT_STICK_SENSOR,)));
  __SET_VAR(data__->,LEFT_GODOWN1,,(!(__GET_VAR(data__->LEFT_STICK_GRAB,)) && __GET_VAR(data__->LEFT_STICK_SENSOR,)));
  __SET_VAR(data__->TON2.,IN,,(!(__GET_VAR(data__->LEFT_STICK_GRAB,)) && __GET_VAR(data__->LEFT_STICK_SENSOR,)));
  __SET_VAR(data__->TON2.,PT,,__time_to_timespec(1, 500, 0, 0, 0, 0));
  TON_body__(&data__->TON2);
  __SET_VAR(data__->TOF2.,IN,,__GET_VAR(data__->TON2.Q,));
  __SET_VAR(data__->TOF2.,PT,,__time_to_timespec(1, 2000, 0, 0, 0, 0));
  TOF_body__(&data__->TOF2);
  __SET_VAR(data__->,LEFT_STICK_GRAB,,__GET_VAR(data__->TOF2.Q,));
  __SET_VAR(data__->TON5.,IN,,__GET_VAR(data__->TOF2.Q,));
  __SET_VAR(data__->TON5.,PT,,__time_to_timespec(1, 500, 0, 0, 0, 0));
  TON_body__(&data__->TON5);
  __SET_VAR(data__->,LEFT_STICK_LEFT_ROTATION,,__GET_VAR(data__->TON5.Q,));
  __SET_VAR(data__->TON7.,IN,,__GET_VAR(data__->TON5.Q,));
  __SET_VAR(data__->TON7.,PT,,__time_to_timespec(1, 500, 0, 0, 0, 0));
  TON_body__(&data__->TON7);
  __SET_VAR(data__->,LEFT_GODOWN2,,__GET_VAR(data__->TON7.Q,));
  __SET_VAR(data__->TOF4.,IN,,__GET_VAR(data__->TON7.Q,));
  __SET_VAR(data__->TOF4.,PT,,__time_to_timespec(1, 1250, 0, 0, 0, 0));
  TOF_body__(&data__->TOF4);
  __SET_VAR(data__->TON9.,IN,,__GET_VAR(data__->TOF4.Q,));
  __SET_VAR(data__->TON9.,PT,,__time_to_timespec(1, 1200, 0, 0, 0, 0));
  TON_body__(&data__->TON9);
  __SET_VAR(data__->,LEFT_STICK_RIGHT_ROTATION,,__GET_VAR(data__->TON9.Q,));
  __SET_VAR(data__->,RIGHT_GODOWN1,,(!(__GET_VAR(data__->RIGHT_STICK_GRAB,)) && __GET_VAR(data__->RIGHT_STICK_SENSOR,)));
  __SET_VAR(data__->TON4.,IN,,(!(__GET_VAR(data__->RIGHT_STICK_GRAB,)) && __GET_VAR(data__->RIGHT_STICK_SENSOR,)));
  __SET_VAR(data__->TON4.,PT,,__time_to_timespec(1, 500, 0, 0, 0, 0));
  TON_body__(&data__->TON4);
  __SET_VAR(data__->TOF3.,IN,,__GET_VAR(data__->TON4.Q,));
  __SET_VAR(data__->TOF3.,PT,,__time_to_timespec(1, 2000, 0, 0, 0, 0));
  TOF_body__(&data__->TOF3);
  __SET_VAR(data__->,RIGHT_STICK_GRAB,,__GET_VAR(data__->TOF3.Q,));
  __SET_VAR(data__->TON6.,IN,,__GET_VAR(data__->TOF3.Q,));
  __SET_VAR(data__->TON6.,PT,,__time_to_timespec(1, 500, 0, 0, 0, 0));
  TON_body__(&data__->TON6);
  __SET_VAR(data__->,RIGHT_STICK_RIGHT_ROTATION,,__GET_VAR(data__->TON6.Q,));
  __SET_VAR(data__->TON8.,IN,,__GET_VAR(data__->TON6.Q,));
  __SET_VAR(data__->TON8.,PT,,__time_to_timespec(1, 500, 0, 0, 0, 0));
  TON_body__(&data__->TON8);
  __SET_VAR(data__->,RIGHT_GODOWN2,,__GET_VAR(data__->TON8.Q,));
  __SET_VAR(data__->TOF5.,IN,,__GET_VAR(data__->TON8.Q,));
  __SET_VAR(data__->TOF5.,PT,,__time_to_timespec(1, 1250, 0, 0, 0, 0));
  TOF_body__(&data__->TOF5);
  __SET_VAR(data__->TON10.,IN,,__GET_VAR(data__->TOF5.Q,));
  __SET_VAR(data__->TON10.,PT,,__time_to_timespec(1, 1200, 0, 0, 0, 0));
  TON_body__(&data__->TON10);
  __SET_VAR(data__->,RIGHT_STICK_LEFT_ROTATION,,__GET_VAR(data__->TON10.Q,));
  __SET_VAR(data__->,FRONT_CONVEYOR1,,__BOOL_LITERAL(TRUE));
  __SET_VAR(data__->,LEFT_ROLLER2,,__BOOL_LITERAL(TRUE));
  __SET_VAR(data__->,RIGHT_ROLLER2,,__BOOL_LITERAL(TRUE));
  __SET_VAR(data__->,LEFT_STICK_DOWN,,(__GET_VAR(data__->LEFT_GODOWN1,) || __GET_VAR(data__->LEFT_GODOWN2,)));
  __SET_VAR(data__->,RIGHT_STICK_DOWN,,(__GET_VAR(data__->RIGHT_GODOWN1,) || __GET_VAR(data__->RIGHT_GODOWN2,)));
  __SET_VAR(data__->,START_RIGHT_ROLLER1,,__GET_VAR(data__->TON10.Q,));
  __SET_VAR(data__->,START_LEFT_ROLLER1,,__GET_VAR(data__->TON9.Q,));
  __SET_VAR(data__->R_TRIG1.,CLK,,__GET_VAR(data__->START_LEFT_ROLLER1,));
  R_TRIG_body__(&data__->R_TRIG1);
  __SET_VAR(data__->F_TRIG1.,CLK,,__GET_VAR(data__->LEFT_ROLLER1,));
  F_TRIG_body__(&data__->F_TRIG1);
  __SET_VAR(data__->CTU0.,CU,,__GET_VAR(data__->R_TRIG1.Q,));
  __SET_VAR(data__->CTU0.,R,,__GET_VAR(data__->F_TRIG1.Q,));
  __SET_VAR(data__->CTU0.,PV,,2);
  CTU_body__(&data__->CTU0);
  __SET_VAR(data__->TOF6.,IN,,(!(__GET_VAR(data__->LEFT_ROLLER1,)) && __GET_VAR(data__->CTU0.Q,)));
  __SET_VAR(data__->TOF6.,PT,,__time_to_timespec(1, 2300, 0, 0, 0, 0));
  TOF_body__(&data__->TOF6);
  __SET_VAR(data__->,LEFT_ROLLER1,,__GET_VAR(data__->TOF6.Q,));
  __SET_VAR(data__->R_TRIG2.,CLK,,__GET_VAR(data__->START_RIGHT_ROLLER1,));
  R_TRIG_body__(&data__->R_TRIG2);
  __SET_VAR(data__->F_TRIG2.,CLK,,__GET_VAR(data__->RIGHT_ROLLER1,));
  F_TRIG_body__(&data__->F_TRIG2);
  __SET_VAR(data__->CTU1.,CU,,__GET_VAR(data__->R_TRIG2.Q,));
  __SET_VAR(data__->CTU1.,R,,__GET_VAR(data__->F_TRIG2.Q,));
  __SET_VAR(data__->CTU1.,PV,,2);
  CTU_body__(&data__->CTU1);
  __SET_VAR(data__->TOF7.,IN,,(!(__GET_VAR(data__->RIGHT_ROLLER1,)) && __GET_VAR(data__->CTU1.Q,)));
  __SET_VAR(data__->TOF7.,PT,,__time_to_timespec(1, 2300, 0, 0, 0, 0));
  TOF_body__(&data__->TOF7);
  __SET_VAR(data__->,RIGHT_ROLLER1,,__GET_VAR(data__->TOF7.Q,));

  goto __end;

__end:
  return;
} // FACTORYIO_DEMO_body__() 






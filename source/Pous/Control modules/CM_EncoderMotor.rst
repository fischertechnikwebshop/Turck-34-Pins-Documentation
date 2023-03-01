.. _CM_EncoderMotor:

CM_EncoderMotor (pou)
=====================

 
Control module to control an encoder motor

by setting the wanted position at ``dwMoveTo``, and setting the ``xMove`` bit the encoder motor will run to this position. 
The correct motor direction, and speeds, are all calculated by this control module.

-------------------------------------------------------------------------------------------------------------------


VAR_INPUT
~~~~~~~~~~

============  =======  =======  ====================================================
Name          Type     Value    Comment                                               
============  =======  =======  ====================================================
dwCntVal      DWORD             Current counter value                                 
xReference    BOOL              Reference switch                                      
**Status bits**
------------------------------------------------------------------------------------
dwMoveTo      DWORD    1        The position the motor should reach                   
xMove         BOOL              Encoder motor moves to the ``dwMoveTo`` value         
xMoveInit     BOOL              Encoder motor (almost) moves to the home position.    
xAbort        BOOL              Stops the movement immediatly                         
xSuspend      BOOL              Suspends the movement                                 
xInit         BOOL              Resets the module errors, and initializes.            
============  =======  =======  ====================================================

VAR_OUTPUT
~~~~~~~~~~~

================  ==================  =======  ===================================================================
Name              Type                Value    Comment                                                              
================  ==================  =======  ===================================================================
xMotorForward     BOOL                         Motor forward                                                        
xMotorBackward    BOOL                         Motor backward                                                       
pwmCtrl           :ref:`stPwmCtrl`             PwmCtrl, for controlling the speed of the BL20-E-2PWM-2CNT output    
cntCtrl           :ref:`stCntCtrl`             CntCtrl, for controlling hte counter in the BL20-E-2PWM-2CNT         
**status bits**
------------------------------------------------------------------------------------------------------------------
xIsInitialized    BOOL                         PWM and Encoder are initialized                                      
xPosReached       BOOL                         ``dwMoveTo`` has been reached                                        
TON_Active        TON                          Timer, keeps track of Active time                                    
R_TRIG_Error      R_TRIG                       Rising tigger, indicating an active error                            
================  ==================  =======  ===================================================================

VAR
~~~~

==================  =========================  =======  ============================================================================================
Name                Type                       Value    Comment                                                                                       
==================  =========================  =======  ============================================================================================
_CM_DutyCycle       CM_DutyCycleCalc                    Control module for calculating the duty cyle                                                  
_CM_Motor           :ref:`CM_MotorExtended`             Controle module for controlling the motor movement (forward/backward)                         
_CM_Reference       :ref:`CM_Input`                     Controle module for the reference switch input                                                
_dwMoveTo           DWORD                               Memory for the position we want to reach                                                      
_dwCntVal           DWORD                               Momory for the current BL20-E-2CNT-2PWM counter value                                         
_xMoveToChanged     BOOL                                                                                                                              
_TON_Watchdog       TON                                 Watchdog timer, used to generate error if motor is activated but Cnt value hasn't changed.    
_R_TRIG_Move        R_TRIG                                                                                                                            
_R_TRIG_MoveInit    R_TRIG                                                                                                                            
_R_TRIG_Abort       R_TRIG                                                                                                                            
_R_TRIG_Suspend     R_TRIG                                                                                                                            
_R_TRIG_Init        R_TRIG                                                                                                                            
==================  =========================  =======  ============================================================================================

VAR RETAIN PERSISTENT
~~~~~~~~~~~~~~~~~~~~~~

=============  =======  =======  ========================================
Name           Type     Value    Comment                                   
=============  =======  =======  ========================================
iHysteresis    DWORD    10       The hysteresis of the wanted position.    
=============  =======  =======  ========================================


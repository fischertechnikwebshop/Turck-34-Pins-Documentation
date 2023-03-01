.. _CM_LinearMovement:

CM_LinearMovement (pou)
=======================


Moves from point A to point B, and/or back. 

-------------------------------------------------------------------------



VAR_INPUT
~~~~~~~~~~

=====================  ======  =======  =============================================================
Name                   Type    Value    Comment                                                        
=====================  ======  =======  =============================================================
xExtendedRefSwitch     BOOL             Reference switch extended position                             
xRetractedRefSwitch    BOOL             Reference switch retracted position                            
**Status bits**
-----------------------------------------------------------------------------------------------------
xRetract               BOOL             Retract to extended position                                   
xExtend                BOOL             Extend to retracted position                                   
xAbort                 BOOL             aborts/stops all movement                                      
xSuspend               BOOL             Suspends the current movement                                  
xInit                  BOOL             Reset the active errors, and initializes the control module    
=====================  ======  =======  =============================================================

VAR_OUTPUT
~~~~~~~~~~~

================  ========  =======  ===========================================
Name              Type      Value    Comment                                      
================  ========  =======  ===========================================
xMotorBackward    BOOL               Output motor backward                        
xMotorForward     BOOL               Output motor forwards                        
**Status bits**
--------------------------------------------------------------------------------
R_TRIG_Error      R_TRIG             Rising tigger, indicating an active error    
xInitialized      BOOL               Indicates if the module is initialized       
xExtended         BOOL               Indicates if table is extended               
xRetracted        BOOL               Indicates if table is retracted              
================  ========  =======  ===========================================

VAR
~~~~

========================  =========================  =======  =======================================================================
Name                      Type                       Value    Comment                                                                  
========================  =========================  =======  =======================================================================
_CM_MotorController       :ref:`CM_MotorExtended`             Controle module for controlling the motor movement (forward/backward)    
_CM_ExtendedRefSwitch     :ref:`CM_Input`                                                                                              
_CM_RetractedRefSwitch    :ref:`CM_Input`                                                                                              
_R_TRIG_Retract           R_TRIG                                                                                                       
_R_TRIG_Extend            R_TRIG                                                                                                       
_R_TRIG_Suspend           R_TRIG                                                                                                       
_R_TRIG_Abort             R_TRIG                                                                                                       
_R_TRIG_Init              R_TRIG                                                                                                       
========================  =========================  =======  =======================================================================


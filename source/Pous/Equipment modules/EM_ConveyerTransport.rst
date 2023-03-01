.. _EM_ConveyerTransport:

EM_ConveyerTransport (pou)
==========================



VAR_INPUT
~~~~~~~~~~

======================  ======  =======  =========================================================================================================================
Name                    Type    Value    Comment                                                                                                                    
======================  ======  =======  =========================================================================================================================
xLightBarrierInside     BOOL             Sensor for detecting if pallet is inside                                                                                   
xLightBarrierOutside    BOOL             Sensor for detecting if pallet is outside                                                                                  
xStartForward           BOOL             Starts moving the belt forward (an error is generated if no pallet is present on the inside when this command is set)      
xStartBackward          BOOL             Starts moving the belt backward (an error is generated if no pallet is present on the outside when this command is set)    
xAbort                  BOOL             The process is stopped immediatly                                                                                          
xSuspend                BOOL             THe process is halted while this input is TRUE                                                                             
xReset                  BOOL             Any errors are resetted                                                                                                    
======================  ======  =======  =========================================================================================================================

VAR_OUTPUT
~~~~~~~~~~~

===================  ========  =======  ========================================================
Name                 Type      Value    Comment                                                   
===================  ========  =======  ========================================================
xConveyerForward     BOOL               Motor conveyer forward                                    
xConveyerBackward    BOOL               Motor conveyer backward                                   
xPalletPresent       BOOL               True if a pallet is already present                       
R_TRIG_Error         R_TRIG             Indicating if there's an active error in the equipment    
===================  ========  =======  ========================================================

VAR
~~~~

====================  =========================  =======  =========
Name                  Type                       Value    Comment    
====================  =========================  =======  =========
CM_MotorController    :ref:`CM_MotorExtended`                        
CM_BarrierInside      :ref:`CM_Input`                                
CM_BarrierOutside     :ref:`CM_Input`                                
RS_HasError           RS                                             
TON_Watchdog          TON                                            
====================  =========================  =======  =========


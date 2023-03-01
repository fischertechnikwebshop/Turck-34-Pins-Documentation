.. _EM_Oven:

EM_Oven (pou)
=============



VAR_INPUT
~~~~~~~~~~

=================  ======  =======  ==================================================================
Name               Type    Value    Comment                                                             
=================  ======  =======  ==================================================================
xSensorOven        BOOL             Sensor for detecting piece placement                                
xRefOvenInside     BOOL             Reference switch oven feed table inside                             
xRefOvenOutside    BOOL             Reference switch oven feed table outside                            
xStart             BOOL             Starts the oven proces (is ignored if no placement was detected)    
xAbort             BOOL             Stops the curren process immediately                                
xSuspend           BOOL             Supends the current execution                                       
xInit              BOOL             Initializes the equipment                                           
=================  ======  =======  ==================================================================

VAR_OUTPUT
~~~~~~~~~~~

====================  ========  =======  ========================================================
Name                  Type      Value    Comment                                                   
====================  ========  =======  ========================================================
xOvenFeederRetract    BOOL               Move the oven feed table to the inside position           
xOvenFeederExtend     BOOL               Move the oven feed table to the outside position          
xOvenLight            BOOL               Light inside the oven                                     
xCompressor           BOOL               Compressor, for door cyllinders                           
xDoorValve            BOOL               Valve, to open the oven door                              
xPiecePlaced          BOOL               indicating if a piece has been placed                     
xDone                 BOOL               Indicating if a piece may be picked up                    
xIsInitialized        BOOL               Indicating if the equipment is initialized                
R_TRIG_Error          R_TRIG             Indicating if there's an active error in the equipment    
====================  ========  =======  ========================================================

VAR
~~~~

=================  ===================  =======  =========
Name               Type                 Value    Comment    
=================  ===================  =======  =========
CM_Feeder          CM_LinearMovement                        
CM_OvenLight       :ref:`CM_Motor`                          
CM_Compressor      :ref:`CM_Motor`                          
CM_DoorValve       :ref:`CM_Valve`                          
CM_Sensor          :ref:`CM_Input`                          
RS_PiecePlaced     RS                                       
_R_TRIG_Start      R_TRIG                                   
_R_TRIG_Abort      R_TRIG                                   
_R_TRIG_Suspend    R_TRIG                                   
_R_TRIG_Init       R_TRIG                                   
=================  ===================  =======  =========


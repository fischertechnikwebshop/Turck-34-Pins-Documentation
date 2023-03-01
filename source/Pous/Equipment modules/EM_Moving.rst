.. _EM_Moving:

EM_Moving (pou)
===============



VAR_INPUT
~~~~~~~~~~

==========================  ======  =======  =======================================================
Name                        Type    Value    Comment                                                  
==========================  ======  =======  =======================================================
xRefTransportAtOven         BOOL             Turntable AT vacuum position                             
xRefTransportAtTurntable    BOOL             Turntable AT Belt position                               
**Status bits**
----------------------------------------------------------------------------------------------------
xStart                      BOOL             Start moving the piece from the oven to the turnTable    
xAbort                      BOOL             Stops the current process immediatly                     
xSuspend                    BOOL             suspends the movement                                    
xInit                       BOOL             Resets, and initializes all equipment.                   
==========================  ======  =======  =======================================================

VAR_OUTPUT 
~~~~~~~~~~~~

=======================  ========  =======  ========================================================
Name                     Type      Value    Comment                                                   
=======================  ========  =======  ========================================================
xTransportToOven         BOOL               Move vacuum head to oven                                  
xTransportToTurnTable    BOOL               Move vacuum head to TurnTable                             
xValveVacuum             BOOL               Activates vacuum                                          
xValveLowering           BOOL               Lowers vacuum head                                        
xCompressor              BOOL               Compressor output                                         
xDone                    BOOL               Indicates that piece has been moved                       
xIsInitialized           BOOL               Indicating if the equipment is initialized                
R_TRIG_Error             R_TRIG             Indicating if there's an active error in the equipment    
=======================  ========  =======  ========================================================

VAR
~~~~

==================  ===================  =======  =========
Name                Type                 Value    Comment    
==================  ===================  =======  =========
CM_Transport        CM_LinearMovement                        
CM_Compressor       :ref:`CM_Motor`                          
CM_ValveLowering    :ref:`CM_Valve`                          
CM_ValveVacuum      :ref:`CM_Valve`                          
_R_TRIG_Start       R_TRIG                                   
_R_TRIG_Abort       R_TRIG                                   
_R_TRIG_Suspend     R_TRIG                                   
_R_TRIG_Init        R_TRIG                                   
==================  ===================  =======  =========


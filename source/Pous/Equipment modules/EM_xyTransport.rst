.. _EM_xyTransport:

EM_xyTransport (pou)
====================



VAR_INPUT
~~~~~~~~~~

=====================  ===========  =======  =========================================================================================================================================
Name                   Type         Value    Comment                                                                                                                                    
=====================  ===========  =======  =========================================================================================================================================
xRefHorizontalAxis     BOOL                  REFERENCE switch horizontal axis                                                                                                           
xRefVerticalAxis       BOOL                  Reference switch vertical axis                                                                                                             
dwHorizontalCnt        DWORD                 Current horizontal count                                                                                                                   
dwVerticalCnt          DWORD                 Current vertical count                                                                                                                     
xRefCantileverFront    BOOL                  Reference switch cantilever in front                                                                                                       
xRefCantileverBack     BOOL                  Reference switch cantilever in back                                                                                                        
Control inputs
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
iToPos                 INT(0..9)             To witch position the equipment needs to run (0..9)                                                                                        
xPlacing               BOOL                  If TRUE the equipment will place a pallet, otherwise it will pick up a pallet                                                              
xWaitAtPos             BOOL                  If TRUE the equipment will move and extend to the correct position. It will however wait before actually placing or picking up a pallet    
xStart                 BOOL                  The movement/process is started                                                                                                            
xStop                  BOOL                  The proces is stopped immediatly                                                                                                           
xSuspend               BOOL                  The process is halted while this input is TRUE                                                                                             
xReset                 BOOL                  The errors are resetted, and the equipment is initialized                                                                                  
=====================  ===========  =======  =========================================================================================================================================

VAR_OUTPUT 
~~~~~~~~~~~~

=======================  ==================  =======  =============================================================================================================================
Name                     Type                Value    Comment                                                                                                                        
=======================  ==================  =======  =============================================================================================================================
xHorizontalToRack        BOOL                         Motor horizontal move towards rack                                                                                             
xHorizontalToConveyer    BOOL                         Motor horizontal move towards conveyer                                                                                         
xVerticalDown            BOOL                         Motor vertical move upwards                                                                                                    
xVerticalUp              BOOL                         Motor vertical move downwards                                                                                                  
xCantileverForward       BOOL                         Motor cantilever move forwards                                                                                                 
xCantileverBackward      BOOL                         Motor cantilever move backwards                                                                                                
stVertCntCtrl            :ref:`stCntCtrl`                                                                                                                                            
stVertPwmCtrl            :ref:`stPwmCtrl`                                                                                                                                            
stHorCntCtrl             :ref:`stCntCtrl`                                                                                                                                            
stHorPwmCtrl             :ref:`stPwmCtrl`                                                                                                                                            
Control outputs
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
xIsInitialized           BOOL                         Indicates if the equipments has been initialized                                                                               
xError                   BOOL                         Indicates if an error is present in the equipment                                                                              
xError_R                 R_TRIG                                                                                                                                                      
xDone                    BOOL                         Indicates that the equipment currently has no active jobs, meaning that previous processes have been succesfully completed.    
xWaitingAtPos            BOOL                         Indicates that the equipment is waiting at the positon. The process is resumed when the xWaitAtPos bit is resetted.            
iPos                     INT                          The last position equipment has run to.                                                                                        
=======================  ==================  =======  =============================================================================================================================

VAR
~~~~

======================  ===================  =======  =========
Name                    Type                 Value    Comment    
======================  ===================  =======  =========
CM_HorizontalMov        CM_EncoderMotor                          
CM_VerticalMov          CM_EncoderMotor                          
CM_Cantilever           CM_LinearMovement                        
_R_TRIG_xStart          R_TRIG                                   
SR_HorizontalReached    SR                                       
SR_VerticalReached      SR                                       
======================  ===================  =======  =========

VAR RETAIN PERSISTENT
~~~~~~~~~~~~~~~~~~~~~~

==============  ===========================  =======  =========
Name            Type                         Value    Comment    
==============  ===========================  =======  =========
a_dwPosition    ARRAY[0..9 0..1] OF DWORD                        
==============  ===========================  =======  =========


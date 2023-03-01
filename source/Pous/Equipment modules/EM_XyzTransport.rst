.. _EM_XyzTransport:

EM_XyzTransport (pou)
=====================



VAR_INPUT
~~~~~~~~~~

====================  ===========  =======  ===========================================================
Name                  Type         Value    Comment                                                      
====================  ===========  =======  ===========================================================
xRefHorizontalAxis    BOOL                  REFERENCE switch horizontal axis                             
xRefVerticalAxis      BOOL                  Reference switch vertical axis                               
xRefRotateAxis        BOOL                  Referencte switch rotating axis                              
dwHorizontalCnt       DWORD                 Current horizontal count                                     
dwVerticalCnt         DWORD                 Current vertical count                                       
dwRotateCnt           DWORD                 Current rotate count                                         
Control inputs
-------------------------------------------------------------------------------------------------------
iPickPos              INT(0..5)                                                                          
iPlacePos             INT(0..5)                                                                          
xStart                BOOL                  The movement/process is started                              
xStop                 BOOL                  The proces is stopped immediatly                             
xSuspend              BOOL                  The process is halted while this input is TRUE               
xReset                BOOL                  The errors are resetted, and the equipment is initialized    
====================  ===========  =======  ===========================================================

VAR_OUTPUT 
~~~~~~~~~~~~

=========================  ==================  =======  ==================================================================
Name                       Type                Value    Comment                                                             
=========================  ==================  =======  ==================================================================
xHorizontalBackward        BOOL                         Motor horizontal move towards rack                                  
xHorizontalForward         BOOL                         Motor horizontal move towards conveyer                              
xVerticalUp                BOOL                         Motor vertical move upwards                                         
xVerticalDown              BOOL                         Motor vertical move downwards                                       
xRotateClockwise           BOOL                         Motor rotate clockwise                                              
xRotateCounterClockwise    BOOL                         Motor rotate counter clockwise                                      
stVertCntCtrl              :ref:`stCntCtrl`                                                                                 
stVertPwmCtrl              :ref:`stPwmCtrl`                                                                                 
stHorCntCtrl               :ref:`stCntCtrl`                                                                                 
stHorPwmCtrl               :ref:`stPwmCtrl`                                                                                 
stRotCntCtrl               :ref:`stCntCtrl`                                                                                 
stRotPwmCtrl               :ref:`stPwmCtrl`                                                                                 
xVacuumValve               BOOL                                                                                             
xCompressor                BOOL                                                                                             
Control outputs
--------------------------------------------------------------------------------------------------------------------------
xIsInitialized             BOOL                         Indicates if the equipments has been initialized                    
xError                     BOOL                         Indicates if an error is present in the equipment                   
xError_R                   R_TRIG                                                                                           
xResetting                 BOOL                         Indicates that the equipment is currently in the resetting state    
xDone                      BOOL                         Indicates that piece has been succesfully moved.                    
xRunning                   BOOL                         Indicates wheter equipment is busy                                  
iPos                       INT                          The last position equipment has run to.                             
=========================  ==================  =======  ==================================================================

VAR
~~~~

==================  =================  =======  =========
Name                Type               Value    Comment    
==================  =================  =======  =========
CM_HorizontalMov    CM_EncoderMotor                        
CM_VerticalMov      CM_EncoderMotor                        
CM_RotateMov        CM_EncoderMotor                        
CM_VacuumValve      :ref:`CM_Valve`                        
CM_Compressor       :ref:`CM_Motor`                        
==================  =================  =======  =========

VAR RETAIN PERSISTENT
~~~~~~~~~~~~~~~~~~~~~~

==============  ===========================  =======  =========
Name            Type                         Value    Comment    
==============  ===========================  =======  =========
a_dwPosition    ARRAY[0..4 0..2] OF DWORD                        
==============  ===========================  =======  =========


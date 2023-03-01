.. _EM_ConveyerExtended:

EM_ConveyerExtended (pou)
=========================


Info
~~~~~~

- Starting and stopping of belt
- Stopping after no. of pulsed by setting ``xStopAt`` and supplying an ``iIndex`` value



VAR_INPUT
~~~~~~~~~~

===========  ===========  =======  =====================================================================================
Name         Type         Value    Comment                                                                                
===========  ===========  =======  =====================================================================================
xPulseBtn    BOOL                  Pulse button, to count no. of revs motor has made                                      
Status bits
------------------------------------------------------------------------------------------------------------------------
xStart       BOOL                  Starts the conveyer                                                                    
xStop        BOOL                  Stops the conveyer                                                                     
xSuspend     BOOL                  Suspends the conveyer                                                                  
xStopAt      BOOL                  Stops the conveyer when it has reached the correct amount of pulses (set by iIndex)    
iIndex       INT(1..3)             Indicating at what position the belt should stop                                       
===========  ===========  =======  =====================================================================================

VAR_OUTPUT
~~~~~~~~~~~

=============  ======  =======  ===========================================================
Name           Type    Value    Comment                                                      
=============  ======  =======  ===========================================================
xConveyer      BOOL             ConveyerMotor output                                         
Status bits
-------------------------------------------------------------------------------------------
xPosReached    BOOL             Indicating that belt has reached its position and stopped    
=============  ======  =======  ===========================================================

VAR
~~~~

==================  ========================  =======  ===================================================================
Name                Type                      Value    Comment                                                              
==================  ========================  =======  ===================================================================
_CM_Conveyer        :ref:`CM_Motor`                                                                                         
_CM_Counter         :ref:`CM_PulseCounter`                                                                                  
_RS_RunningToPos    RS                                 RS BIT, for setting and resetting if motor should run to position    
==================  ========================  =======  ===================================================================

VAR RETAIN PERSISTENT
~~~~~~~~~~~~~~~~~~~~~~

=================  =====================  ==========  ==============================================================================================================
Name               Type                   Value       Comment                                                                                                         
=================  =====================  ==========  ==============================================================================================================
aParamPositions    ARRAY[0..2] OF WORD    [3 8 13]    The no. of pulses belt needs to run before stoppin (``iIndex`` is in direct correlation with this ``ARRAY``)    
=================  =====================  ==========  ==============================================================================================================


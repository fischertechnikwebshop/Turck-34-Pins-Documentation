.. _EM_TurnTable:

EM_TurnTable (pou)
==================



VAR_INPUT
~~~~~~~~~~

=======================  ======================  =======================  ==============================
Name                     Type                    Value                    Comment                         
=======================  ======================  =======================  ==============================
xRefTurnTableAtVacuum    BOOL                                             Turntable AT vacuum position    
xRefTurnTableAtBelt      BOOL                                             Turntable AT Belt position      
xRefTurnTableAtSaw       BOOL                                             Turntable at saw position       
eMoveTo                  :ref:`eTurnTablePos`    eTurnTablePos.Unknown                                    
xEject                   BOOL                                                                             
xAbort                   BOOL                                                                             
xSuspend                 BOOL                                                                             
xReset                   BOOL                                                                             
=======================  ======================  =======================  ==============================

VAR_OUTPUT
~~~~~~~~~~~

============================  ======================  =======================  ========================================================
Name                          Type                    Value                    Comment                                                   
============================  ======================  =======================  ========================================================
xTurnTableClockWise           BOOL                                             Output TO motor forward/clockwise motion                  
xTurnTableCounterClockWise    BOOL                                             Output TO motor backward/counter-clockwise motion         
xValve                        BOOL                                             Valve ejection                                            
xCompressor                   BOOL                                             Compressor output                                         
pwmCtrl                       :ref:`stPwmCtrl`                                                                                           
xEjectDone                    BOOL                                                                                                       
eCurrentPos                   :ref:`eTurnTablePos`    eTurnTablePos.Unknown                                                              
xIsInitialized                BOOL                                                                                                       
R_TRIG_Error                  R_TRIG                                           Indicating if there's an active error in the equipment    
============================  ======================  =======================  ========================================================

VAR
~~~~

==================  =========================  =======  =========
Name                Type                       Value    Comment    
==================  =========================  =======  =========
CM_RefVacuum        :ref:`CM_Input`                                
CM_RefBelt          :ref:`CM_Input`                                
CM_RefSaw           :ref:`CM_Input`                                
CM_Compressor       :ref:`CM_Motor`                                
CM_ValvePusher      :ref:`CM_Valve`                                
CM_MotorControl     :ref:`CM_MotorExtended`                        
SR_ERROR            SR                                             
RS_EjectDone        RS                                             
RS_IsInitialized    RS                                             
==================  =========================  =======  =========

VAR RETAIN PERSISTENT
~~~~~~~~~~~~~~~~~~~~~~

==================  =======  =======  =========
Name                Type     Value    Comment    
==================  =======  =======  =========
dwTurnTableSpeed    DWORD    40                  
==================  =======  =======  =========


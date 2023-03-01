.. _EM_Sorting:

EM_Sorting (pou)
================


   
Info
~~~~~~

- Pushing piece into magazine
- Ejecting by setting input ``xEject`` and supplying an ``iIndex`` value
- Ejection is halted if a piece is already present at the selected ``iIndex``

Errors
~~~~~~~~

- The ejection took too long



VAR_INPUT
~~~~~~~~~~

==============  ===========  =======  ==============================================================================
Name            Type         Value    Comment                                                                         
==============  ===========  =======  ==============================================================================
xSensorOne      BIT                   Sensor first magazine (white)                                                   
xSensorTwo      BIT                   Sensor second magazine (Red)                                                    
xSensorThree    BIT                   Sensor third magazine (Blue)                                                    
Status bits
--------------------------------------------------------------------------------------------------------------------
xEject          BOOL                  Starts ejection at iIndex value                                                 
iIndex          INT(1..3)             integer (1..3) indicating at which location the ejection needs to take place    
xReset          BOOL                  Resets done output and errors                                                   
==============  ===========  =======  ==============================================================================

VAR_OUTPUT
~~~~~~~~~~~

=================  ========  =======  ========================================================
Name               Type      Value    Comment                                                   
=================  ========  =======  ========================================================
xCompressor        BIT                Compressor                                                
xValveOne          BIT                Valve first ejector (white)                               
xValveTwo          BIT                Valve second ejector (red)                                
xValveThree        BIT                Valve third ejector (Blue)                                
Status bits
----------------------------------------------------------------------------------------------
xMagOneFilled      BOOL               Indicates wheter magazine one (white) is filled           
xMagTwoFilled      BOOL               Indicates wheter magazine two (red) is filled             
xMagThreeFilled    BOOL               Indicates wheter magazine three (blue) is filled          
xDone              BOOL                                                                         
R_TRIG_Error       R_TRIG             Indicating if there's an active error in the equipment    
=================  ========  =======  ========================================================

VAR
~~~~

================  =================  =======  ===============================================
Name              Type               Value    Comment                                          
================  =================  =======  ===============================================
Control modules
---------------------------------------------------------------------------------------------
CM_SensorOne      :ref:`CM_Input`                                                              
CM_SensorTwo      :ref:`CM_Input`                                                              
CM_SensorThree    :ref:`CM_Input`                                                              
CM_Compressor     :ref:`CM_Motor`                                                              
CM_ValveOne       :ref:`CM_Valve`                                                              
CM_ValveTwo       :ref:`CM_Valve`                                                              
CM_ValveThree     :ref:`CM_Valve`                                                              
memory values
---------------------------------------------------------------------------------------------
TON_watchdog      TON                         Watchdog timer                                   
RS_Done           RS                          RS bit, for keeping track if ejection is DONE    
RS_HasError       RS                          RS BIT, for keeping track if error is active     
================  =================  =======  ===============================================


.. _CM_ColorSensor:

CM_ColorSensor (pou)
====================


Control module for converting :ref:`CM_AnalogIn` output value to an :ref:`eClr` value.

On xStart the measurement is started. After xStop has been called a collor will parsed based on the lowest measured value.

Error
~~~~~~~~

An error is generated when xStart has been set twice.



VAR_INPUT
~~~~~~~~~~

===========  ======  =======  ================================================================
Name         Type    Value    Comment                                                           
===========  ======  =======  ================================================================
wAnalogIn    WORD             Analog In value from BL20-E-2CNT-2PWM                             
**Status bits**
----------------------------------------------------------------------------------------------
xStart       BOOL             Starts the color measurement                                      
xStop        BOOL             Stops the color measurement, and calculates the measured color    
xInit        BOOL             Resets the measured values                                        
===========  ======  =======  ================================================================

VAR_OUTPUT
~~~~~~~~~~~

================  =============  =======  =============================================================
Name              Type           Value    Comment                                                        
================  =============  =======  =============================================================
eMeasuredColor    :ref:`eClr`             The measured color, only valid if ``xStop`` has been called    
**Status bits**
-------------------------------------------------------------------------------------------------------
TON_Active        TON                     Timer, keeps track of xActive time                             
R_TRIG_Error      R_TRIG                  Rising tigger, indicating an active error                      
================  =============  =======  =============================================================

VAR
~~~~

===============  ====================  =======  ====================================
Name             Type                  Value    Comment                               
===============  ====================  =======  ====================================
_CM_AnalogIn     :ref:`CM_AnalogIn`             Control module                        
_RS_Active       RS                             Memory bit, for active measurement    
_SR_Error        SR                             Memory bit, for active error          
**Rising triggers status bits**
------------------------------------------------------------------------------------
_R_TRIG_Start    R_TRIG                                                               
_R_TRIG_Stop     R_TRIG                                                               
_R_TRIG_Init     R_TRIG                                                               
===============  ====================  =======  ====================================

VAR RETAIN PERSISTENT
~~~~~~~~~~~~~~~~~~~~~~

======================  ======  =======  ===================================================
Name                    Type    Value    Comment                                              
======================  ======  =======  ===================================================
PT_TIMER                TIME    T#2S     TON time                                             
rParamColorUndefined    REAL    4        If highest measured value below, color is unknown    
rParamColorWhite        REAL    6        If highest measured value below, color is white      
rParamColorRed          REAL    7        If highest measured value below, color is red        
rParamColorBlue         REAL    7.5      If highest measured value below, color is blue       
======================  ======  =======  ===================================================


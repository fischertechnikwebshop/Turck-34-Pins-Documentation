.. _EM_ColorDetection:

EM_ColorDetection (pou)
=======================

   
Info
~~~~~~

- Measuring the color of a piece based on an analog value
- Measurement starts on input sensor
- Measurement stops on output sensor

Errors
~~~~~~~~

- Equipment received a new piece, while old piece wasn't fully measured yet
- The measured value was invalid



VAR_INPUT
~~~~~~~~~~

===============  ======  =======  =======================================
Name             Type    Value    Comment                                  
===============  ======  =======  =======================================
wAnalogIn        WORD             Analog value (from Banner S15)           
xInputSensor     BOOL             Input sensor (starts the measurement)    
xOutputSensor    BOOL             Output sensor (stops the measurement)    
Status bits
-------------------------------------------------------------------------
xReset           BOOL             Resets any measured values and errors    
===============  ======  =======  =======================================

VAR_OUTPUT
~~~~~~~~~~~

==============  =============  =======  ========================================================
Name            Type           Value    Comment                                                   
==============  =============  =======  ========================================================
eColor          :ref:`eClr`             Enum, indicating the measured color                       
status bits
------------------------------------------------------------------------------------------------
R_TRIG_Error    R_TRIG                  Indicating if there's an active error in the equipment    
==============  =============  =======  ========================================================

VAR
~~~~

=================  =======================  =======  ==========================================
Name               Type                     Value    Comment                                     
=================  =======================  =======  ==========================================
CM_ColorSensor     :ref:`CM_ColorSensor`                                                         
CM_InputSensor     :ref:`CM_Input`                                                               
CM_OutputSensor    :ref:`CM_Input`                                                               
RS_HasError        RS                                RS BIT, for setting and resetting errors    
=================  =======================  =======  ==========================================


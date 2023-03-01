.. _CM_AnalogIn:

CM_AnalogIn (pou)
=================


Control module for reading an analog input from the `BL20-E-4IOL-10 <https://www.turck.nl/nl/product/100001334>`_ 
in combination with the `Banner S15C-U-KQ <https://www.bannerengineering.com/be/en/products/part.809838.html>`_

The control module transforms the output value based on the current input value, 
it also saves the highest and lowest measured value since the last reset, or startup. 



VAR_INPUT
~~~~~~~~~~

===========  ======  =======  ===========================================
Name         Type    Value    Comment                                      
===========  ======  =======  ===========================================
wAnalogIn    WORD             Analog In value (from ``BL20-E-4IOL-10``)    
**Status bits**
-------------------------------------------------------------------------
xInit        BOOL             Reset Highest and lowest measured values     
===========  ======  =======  ===========================================

VAR_OUTPUT
~~~~~~~~~~~

==============  ======  =======  ==========================================
Name            Type    Value    Comment                                     
==============  ======  =======  ==========================================
rOutputValue    REAL             ``rOutputValue wAnalogIn * rMultiplier``    
**Status bits**
---------------------------------------------------------------------------
rLowestVal      REAL             Lowest measured value                       
rHighestVal     REAL             Highest measured value                      
==============  ======  =======  ==========================================

VAR RETAIN PERSISTENT
~~~~~~~~~~~~~~~~~~~~~~

=============  ======  =======  =======================================================
Name           Type    Value    Comment                                                  
=============  ======  =======  =======================================================
rMultiplier    REAL    0.001    Multiplier (``rOutputValue wAnalogIn * rMultiplier``)    
=============  ======  =======  =======================================================


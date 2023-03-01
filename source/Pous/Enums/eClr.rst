.. _eClr:

eClr (dut)
==========


The ``E_color`` enum is used mainly in the colormeasuring station. When a color is not **yet** measured the value should be ``Unknown``. 
if a measurement has finished but a color could not be calculated the ``Undefined`` value should be set. 


ENUM
~~~~~~~~~~~~~~~~~~~~

===========  =======  ================================
Name         Value    Comment                           
===========  =======  ================================
Unknown      0        The color is unkown               
White        1                                          
Red          2                                          
Blue         3                                          
Undefined    4        The color couldn't be measured    
===========  =======  ================================


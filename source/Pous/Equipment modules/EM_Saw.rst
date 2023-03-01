.. _EM_Saw:

EM_Saw (pou)
============



VAR_INPUT
~~~~~~~~~~

==========  ======  =======  ==========================
Name        Type    Value    Comment                     
==========  ======  =======  ==========================
xStart      BOOL             Starts the saw              
xStop       BOOL             Stop the saw                
xSuspend    BOOL                                         
xReset      BOOL             Resets thwe xDone output    
==========  ======  =======  ==========================

VAR_OUTPUT
~~~~~~~~~~~

========  ======  =======  ===================================
Name      Type    Value    Comment                              
========  ======  =======  ===================================
xMotor    BOOL             Output to the blade motor            
xDone     BOOL             Indicates that piece has been cut    
========  ======  =======  ===================================

VAR
~~~~

===============  =================  =======  =========
Name             Type               Value    Comment    
===============  =================  =======  =========
CM_BladeMotor    :ref:`CM_Motor`                        
SR_Done          SR                                     
===============  =================  =======  =========


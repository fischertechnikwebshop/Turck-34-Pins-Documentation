.. _EM_Conveyer:

EM_Conveyer (pou)
=================



VAR_INPUT
~~~~~~~~~~

==========  ======  =======  =================
Name        Type    Value    Comment            
==========  ======  =======  =================
xSensor     BOOL                                
**Status bits**
----------------------------------------------
xStart      BOOL                                
xStop       BOOL                                
xSuspend    BOOL                                
xReset      BOOL                                
==========  ======  =======  =================

VAR_OUTPUT
~~~~~~~~~~~

==============  ========  =======  ========================================================
Name            Type      Value    Comment                                                   
==============  ========  =======  ========================================================
xConveyer       BOOL                                                                         
xDone           BOOL                                                                         
R_TRIG_Error    R_TRIG             Indicating if there's an active error in the equipment    
==============  ========  =======  ========================================================

VAR
~~~~

==============  =================  =======  =========
Name            Type               Value    Comment    
==============  =================  =======  =========
_CM_sensor      :ref:`CM_Input`                        
_CM_conveyer    :ref:`CM_Motor`                        
RS_HasError     RS                                     
RS_Done         RS                                     
==============  =================  =======  =========


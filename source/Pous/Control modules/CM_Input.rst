.. _CM_Input:

CM_Input (pou)
==============


A control module to control a single (digital) input like a switch, or sensor. 

-------------------------------------------------------------------------------------------



VAR_INPUT
~~~~~~~~~~

======  ======  =======  =============
Name    Type    Value    Comment        
======  ======  =======  =============
xDI     BOOL             Input value    
======  ======  =======  =============

VAR_OUTPUT
~~~~~~~~~~~

============  ========  =======  ===========================================
Name          Type      Value    Comment                                      
============  ========  =======  ===========================================
**Status bits**
----------------------------------------------------------------------------
xDO           BOOL               Output value                                 
TON_xDO       TON                timer delayed on, based on ``xDI`` value     
TOF_xDO       TOF                timer delayed off, based on ``xDI`` value    
R_TRIG_xDO    R_TRIG             Rising trigger based on ``xDI`` value        
F_TRIG_xDO    F_TRIG             Falling trigger based on ``xDI`` value       
============  ========  =======  ===========================================

VAR RETAIN PERSISTENT
~~~~~~~~~~~~~~~~~~~~~~

==========  ======  =======  ==========
Name        Type    Value    Comment     
==========  ======  =======  ==========
PT_TIMER    TIME    T#2S     TON time    
==========  ======  =======  ==========


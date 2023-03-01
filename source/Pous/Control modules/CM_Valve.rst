.. _CM_Valve:

CM_Valve (pou)
==============


Control module to control a valve
   
-------------------------------------------


VAR_INPUT
~~~~~~~~~~

========  ======  =======  ==========================================
Name      Type    Value    Comment                                     
========  ======  =======  ==========================================
**Status bits**
---------------------------------------------------------------------
xJog      BOOL             Valve is open while ``xJog`` is ``TRUE``    
xOpen     BOOL             Open valve                                  
xClose    BOOL             Close valve                                 
========  ======  =======  ==========================================

VAR_OUTPUT
~~~~~~~~~~~

============  ======  =======  ===============================================
Name          Type    Value    Comment                                          
============  ======  =======  ===============================================
xValve        BOOL             Output to valve                                  
**Status bits**
------------------------------------------------------------------------------
TON_active    TON              timer delayed on, based on ``xActive`` value     
TOF_Active    TOF              timer delayed off, based on ``xActive`` value    
============  ======  =======  ===============================================

VAR
~~~~

===========  ======  =======  ============================
Name         Type    Value    Comment                       
===========  ======  =======  ============================
_SR_Valve    SR               Memory valve opened/closed    
===========  ======  =======  ============================

VAR RETAIN PERSISTENT
~~~~~~~~~~~~~~~~~~~~~~

==========  ======  =======  ==========
Name        Type    Value    Comment     
==========  ======  =======  ==========
PT_TIMER    TIME    T#2S     TON time    
==========  ======  =======  ==========


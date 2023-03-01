.. _CM_Motor:

CM_Motor (pou)
==============


Used to start/stop a motor

------------------------------------------------------------------------------------



VAR_INPUT
~~~~~~~~~~

==========  ======  =======  =============================================
Name        Type    Value    Comment                                        
==========  ======  =======  =============================================
**Status bits**
--------------------------------------------------------------------------
xJog        BOOL             The motor runs while this input is ``TRUE``    
xStart      BOOL             The motor is started                           
xStop       BOOL             The motor is stopped                           
xSuspend    BOOL             The motor is suspended                         
==========  ======  =======  =============================================

VAR_OUTPUT
~~~~~~~~~~~

============  ======  =======  ===================================
Name          Type    Value    Comment                              
============  ======  =======  ===================================
xMotor        BOOL             Output to motor                      
**Status bits**
------------------------------------------------------------------
TON_Active    TON              Timer, keeps track of Active time    
============  ======  =======  ===================================

VAR
~~~~

=============  ======  =======  ====================================
Name           Type    Value    Comment                               
=============  ======  =======  ====================================
_SR_Started    SR               Memory for setting motor to active    
=============  ======  =======  ====================================

VAR RETAIN PERSISTENT
~~~~~~~~~~~~~~~~~~~~~~

==========  ======  =======  ==========
Name        Type    Value    Comment     
==========  ======  =======  ==========
PT_TIMER    TIME    T#2S     TON time    
==========  ======  =======  ==========


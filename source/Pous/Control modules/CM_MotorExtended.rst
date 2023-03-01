.. _CM_MotorExtended:

CM_MotorExtended (pou)
======================


Used to forward, backward and stop a motor

-----------------------------------------------------------------------------------------



VAR_INPUT
~~~~~~~~~~

================  ======  =======  ==============================================
Name              Type    Value    Comment                                         
================  ======  =======  ==============================================
**Status bits**
---------------------------------------------------------------------------------
xStartForward     BOOL             Start motor movement into forward direction     
xStartBackward    BOOL             Start motor movement into backward direction    
xStop             BOOL             Stop motor movement                             
xSuspend          BOOL             Suspend motor movement                          
================  ======  =======  ==============================================

VAR_OUTPUT
~~~~~~~~~~~

================  ======  =======  ====================================
Name              Type    Value    Comment                               
================  ======  =======  ====================================
xMotorForward     BOOL             Motor forward                         
xMotorBackward    BOOL             Motor backward                        
**Status bits**
-----------------------------------------------------------------------
TON_Active        TON              Timer, keeps track of xActive time    
================  ======  =======  ====================================

VAR
~~~~

==============  ======  =======  ================================================
Name            Type    Value    Comment                                           
==============  ======  =======  ================================================
_RS_Forward     RS               Memory for setting motor to forward direction     
_RS_Backward    RS               Memory for setting motor to backward direction    
==============  ======  =======  ================================================

VAR RETAIN PERSISTENT
~~~~~~~~~~~~~~~~~~~~~~

==========  ======  =======  ==========
Name        Type    Value    Comment     
==========  ======  =======  ==========
PT_TIMER    TIME    T#2S     TON time    
==========  ======  =======  ==========


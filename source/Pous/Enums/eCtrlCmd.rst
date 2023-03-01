.. _eCtrlCmd:

eCtrlCmd (dut)
==============


The ``E_CtrlCommand`` type is used to controll the different **units**. States of the units are activated, and deactivated, based on this value.


ENUM
~~~~~~~~~~~~~~~~~~~~

===========  =======  ====================================
Name         Value    Comment                               
===========  =======  ====================================
NONE         0        Default value                         
Start        1        Move state machine to START           
Abort        2        Move state machine to ABORT           
Reset        3        Move state machine to IDLE            
Suspend      4        Move state machine to SUSPENDING      
Unsuspend    5        Move state machine to UNSUSPENDING    
===========  =======  ====================================


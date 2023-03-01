.. _CM_DutyCycleCalc:

CM_DutyCycleCalc (pou)
======================


Control module to control the speed of an encoder motor.
   
the speed is controlled by changing the duty cycle of an PWM output in the `BL20-E-2CNT-2PWM <https://www.turck.nl/nl/product/6827341>`_. 
The duty cycle is based on the current ``CNT`` value, the wanted value, and parameters.  

.. image:: /_Graphics/CM_DutyCycleCalc.png
   :align: center
   
------------------------------------------------------------------------------



VAR_INPUT
~~~~~~~~~~

======  =======  =======  ====================================
Name    Type     Value    Comment                               
======  =======  =======  ====================================
dwCv    DWORD    0        Current value of ``CNT``              
dwSp    DWORD    0        The ``CNT`` value we want to reach    
**Status bits**
--------------------------------------------------------------
xMin    BOOL              Sets duty cycle output to minimum     
======  =======  =======  ====================================

VAR_OUTPUT
~~~~~~~~~~~

=============  ==================  =======  =============================================================
Name           Type                Value    Comment                                                        
=============  ==================  =======  =============================================================
pwmCtrl        :ref:`stPwmCtrl`             BL20 duty cycle control bits                                   
**Status bits**
---------------------------------------------------------------------------------------------------------
iPercentage    INT                          Duty cycle value in %                                          
dwCvSp_Diff    DWORD                        Difference between setpoint (dwSp) and current value (dwCv)    
=============  ==================  =======  =============================================================

VAR
~~~~

============  =======  =======  ==========================================================
Name          Type     Value    Comment                                                     
============  =======  =======  ==========================================================
_iDC_Range    INT               the dutycyle range (``dwDutyCycleMax - dwDutyCycleMin``)    
_dwRdAbs      DWORD             Moment (absolute) when rampdown should start                
============  =======  =======  ==========================================================

VAR RETAIN PERSISTENT
~~~~~~~~~~~~~~~~~~~~~~

===============  =============  =======  ======================================================================================
Name             Type           Value    Comment                                                                                 
===============  =============  =======  ======================================================================================
iDutyCycleMin    INT(0..100)    10       Minimum duty cycle                                                                      
iDutyCycleMax    INT(0..100)    90       Maximum duty cycle                                                                      
dwRdRelSp        DWORD          100      the moment the rampdown starts (relative, when ``cv 300``, rampdown kicks in at 200)    
iSteepness       INT            2        Changes the steepness of ramping down.                                                  
===============  =============  =======  ======================================================================================


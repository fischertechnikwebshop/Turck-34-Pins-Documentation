.. _stPwmCtrl:

stPwmCtrl (dut)
===============


The ``pwmCtrl`` output is a structure, and contains all bits to control the `BL20-E-2CNT-2PWM <https://www.turck.nl/nl/product/6827341>`_ PWM output. 

======================= =================================
pwmCtrl                 connect to ``BL20_E_2CNT_2PWM``.
======================= =================================
dwPWM_Val               AUX_REG?_WR_DATA
xPWM_Enable	            PWM?_ENABLE
xPWM_Write	            AUX_REG?_WR_EN
======================= =================================

.. Note::
   Replace the **?** for the ``BL20_E_2CNT_2PWM`` output number you'd like to control 
   
   - 1 (ONE), for output ``P1``
   - 2 (TWO), for output ``P2``

   Make sure the parameters are configured correctly! 
   
   - ``ADDR AUX REG1 WR DATA == 61`` (to control ``BL20_E_2CNT_2PWM.P1``)
   - ``ADDR AUX REG2 WR DATA == 71`` (to control ``BL20_E_2CNT_2PWM.P2``)

------------------------------------------------------------------------------



STRUCT
~~~~~~~~~~~~~~~~~~~~

=============  =======  ==================
Name           Type     Comment             
=============  =======  ==================
dwPWM_Val      DWORD    AUX_REG?_WR_DATA    
xPWM_Enable    BOOL     PWM?_ENABLE         
xPWM_Write     BOOL     AUX_REG?_WR_EN      
=============  =======  ==================


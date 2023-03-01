.. _Devices:

Programs
=============

In the :download:`Sample Program</_Documents/Turck fischerTechnik.projectarchive>` are five different programs (Devices) present.  

Four programs for four different stations:

  - :ref:`Vacuum Gripper Robot (xyz Robot) <xyzRobot_PLC>`
  - :ref:`High-Bay Warehouse <Warehouse_PLC>`
  - :ref:`Processing Station <ProcessingStation_PLC>`
  - :ref:`Sorting Line <SortingLine_PLC>`

The fifth program is used to coordinate the four other programs when used simultaneously in the fischertechnik factory config. 

  - :ref:`Process Cell <ProcessCell>`

Information on these programs, and it's corresponding fischertechnik stations, can be found in the current directory.

-----------------------------------------------------------

.. figure:: /_Graphics/Factory.png
   :align: center

   The four different stations can be combined to create a factory, 
   see :ref:`Process Cell <ProcessCell>` for information about setting up the factory config.

-----------------------------------------------------------

Please see :download:`Downloading to PLC </_Documents/HowTo 34Pin.pdf>` on how to load a program into the Turck control module.


.. toctree::
   :maxdepth: 1
   :hidden:

   SortingLine_PLC//index
   xyzRobot_PLC//index
   Warehouse_PLC//index
   ProcessingStation_PLC//index
   ProcessCell//index

.. _Equipment modules:

Equipment Modules
=================

Each fischertechnik stations consists of one or more **Equipment Modules**. 

--------------------------------------------------------------------------------------

An equipment module is a piece of software that controls the behaviour of one specific piece of equipment. 

in short, an equipment module is:

- A collection of :ref:`Control Modules <Control modules>` or other equipment modules
- Carries out a finite number of activitities
- Contains all the neccessary modules to carry out these activities

-------------------------------------------------------------------------------------

For example an equipment module might consist of, e.g. a circulation pump, a
chilled water valve, a steam valve and a temperature controller. In this case the
equipment module would represent a temperature control system

-------------------------------------------------------------------------------------

.. figure:: /_Graphics/EM.png
   :align: center

   Equipment modules in fischertechnik factory




.. toctree::
   :maxdepth: 1
   :hidden:

   EM_ConveyerExtended.rst
   EM_Sorting.rst
   EM_Moving.rst
   EM_ColorDetection.rst
   EM_Oven.rst
   EM_TurnTable.rst
   EM_Saw.rst
   EM_Conveyer.rst
   EM_xyTransport.rst
   EM_ConveyerTransport.rst
   EM_WareHouse.rst
   EM_XyzTransport.rst

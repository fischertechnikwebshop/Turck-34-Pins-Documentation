.. _Warehouse_PLC:

Warehouse
=========

.. image:: /_Graphics/536631.png
   :align: center

----------------------------------------------------------------------------------------------

See the `fischertechnik website <https://www.fischertechnikwebshop.com/en-gb/24-vdc-en-gb>`_ for more information about this station. 

----------------------------------------------------------------------------------------------

Info:
~~~~~

Storage and retrieval of workpieces and containers
--------------------------------------------------

Transfer station with conveyor belt, shelf stacker for storing and retrieving special workpiece carriers, 9 storage slots.

Flow of pieces
--------------

- The pieces are placed and removed at the conveyer (**YELLOW/GREEN DOT**). 

.. image:: /_Graphics/536631_Schematic.png
   :align: center
   :width: 400

The following modules are used :ref:`Transport <EM_xyTransport>`, :ref:`Conveyer <EM_ConveyerTransport>`, :ref:`Warhouse (Database) <EM_WareHouse>`

.. note::
   If the high-bay warehouse moves to the aborted state while a container is present on the cantilever, the container should always be placed at the conveyer position. 


Download(s)
-----------
- :download:`I/O and info </_Documents/536631 INFO.pdf>`
- :download:`Design document </_Documents/536631 DESIGN.pdf>`
- :download:`Factory Acceptance Test </_Documents/536631 FAT.pdf>`




.. toctree::
   :maxdepth: 1
   :hidden:


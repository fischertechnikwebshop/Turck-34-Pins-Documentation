.. _SortingLine_PLC:

SortingLine
===========

.. image:: /_Graphics/536633.png
   :align: center

----------------------------------------------------------------------------------------------

See the `fischertechnik website <https://www.fischertechnikwebshop.com/en-gb/24-vdc-en-gb>`_ for more information about this station. 

.. warning::
   When using this station a banner converter needs to be added in the Turck control module!

   .. image:: /_Graphics/536633_AddBanner.png
      :align: center
      :width: 400

   The converter can be added between the cables behind the mounting board.

----------------------------------------------------------------------------------------------

Info:
~~~~~

Recognition and sorting of the different workpieces
---------------------------------------------------

Detects workpieces of different colors and sorts them via a conveyor belt into the provided storage unit.

Flow of pieces
--------------

- The pieces are placed at the input of the conveyer (**YELLOW DOT**). 
- The pieces are removed at one of the three magazines (**GREEN DOT's**).

.. image:: /_Graphics/536633_Schematic.png
   :align: center
   :width: 400

The following modules are used :ref:`Color Detection <EM_ColorDetection>`, :ref:`Conveyer <EM_ConveyerExtended>`, :ref:`Sorting <EM_Sorting>`

Download(s)
-----------
- :download:`I/O and info </_Documents/536633 INFO.pdf>`
- :download:`Design document </_Documents/536633 DESIGN.pdf>`
- :download:`Factory Acceptance Test </_Documents/536633 FAT.pdf>`



.. toctree::
   :maxdepth: 1
   :hidden:


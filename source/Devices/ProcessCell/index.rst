.. _ProcessCell:

Process cell 
============

The process cell coordinates the four fischertechnik stations into a factory. 

.. image:: /_Graphics/Factory.png
   :align: center

----------------------------------------------------------------------------------------------

Info:
~~~~~

Combination of the models Sorting Line With Color Detection, Multi Processing Station With Oven, Automated High-Bay Warehouse and Vacuum Gripper Robot. 
Self-contained material cycle: workpieces are retrieved from the Automated High-Bay Warehouse, processed in the Multi Processing Station With Oven, 
then sorted by color in the Sorting Line With Color Detection and finally stored in the Automated High-Bay Warehouse again.

Setting up
-----------

Make sure the four fischertechnik stations are correctly alignent:

.. image:: /_Graphics/Factory_StationsLocations.png
   :align: center
   :width: 400

.. warning::
   When aligning the four fischertechnik stations, a coupling needs to be added between the sorting & multi processing stations. 

   .. image:: /_Graphics/Factory_CoupleStations.png
      :align: center
      :width: 400

------------------------------------------------------------

Connecting the different stations
---------------------------------

The four Turck control units should al be connected to the process cell. 
In the sample program the process cell runs on a CODESYS soft PLC on a (windows) PC.

.. image:: /_Graphics/Factory_Connections.png
   :align: center
   :width: 400

For information on how to connect a Turck control unit to a fischertechnik station, please go to the information page of the applicable fischertechnik station.  


.. toctree::
   :maxdepth: 1
   :hidden:


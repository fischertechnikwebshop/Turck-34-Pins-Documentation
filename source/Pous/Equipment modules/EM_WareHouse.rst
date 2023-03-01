.. _EM_WareHouse:

EM_WareHouse (pou)
==================


.. Figure:: /_Graphics/EM_WareHouse_Front.png
   :align: center
   :height: 400
   
   Front view high-bay warehouse
   
Info
~~~~~~

- Keeping track of the current pieces present in the warehouse.

-------------------------------------------------------------------------------------------

The warehouse has nine *placement* positions. Each position can have 5 different states (:ref:`eInventory <eInventory>`):

1. No container
2. Container with white piece 
3. Container with red piece
4. Container with blue piece
5. Empty container

Initial values
~~~~~~~~~~~~~~

After power on, the values of all the warehouse positions are initialized. 

- Column 1 (positions 0, 3, 6): Container with white piece
- Column 2 (positions 1, 4, 7): Container with red piece
- Column 3 (positions 2, 5, 8): Container with blue piece
 



VAR_INPUT
~~~~~~~~~~

=====================  ===================  =======  =======================================================================================================
Name                   Type                 Value    Comment                                                                                                  
=====================  ===================  =======  =======================================================================================================
iInLocation            INT(0..8)                     The location no. (if we remove, or store a color, it's performed at this index)                          
eProduct               :ref:`eInventory`             The product type, we want to store or find                                                               
xStartQuery            BOOL                          Starts searching for a warehouse position which has a container containing the same ``eProduct`` type    
xStartQueryEmptyPos    BOOL                          Starts searching for a warehouse position which has a container containing nothing                       
xStartQueryNonePos     BOOL                          Starts searching for a warehouse position which has no container                                         
xStore                 BOOL                          Rising Edge, The ``eProduct`` value is stored at the ``iInlocation`` index                               
xStoreEmpty            BOOL                          Rising Edge, an empty container is stored at the ``iInlocation`` index                                   
xStoreNone             BOOL                          Rising Edge, the ``iInlocation`` index is completly freed                                                
=====================  ===================  =======  =======================================================================================================

VAR_OUTPUT
~~~~~~~~~~~

====================  ===========  =======  ============================================================================================================
Name                  Type         Value    Comment                                                                                                       
====================  ===========  =======  ============================================================================================================
iWhitePieceCnt        INT                   no. Of white pieces in the warehouse                                                                          
iRedPieceCnt          INT                   no. Of red pieces in the warehouse                                                                            
iBluePieceCnt         INT                   no. Of Blue pieces in the warehouse                                                                           
iFreePieceCnt         INT                   no. Of empty containers in the warehouse                                                                      
**Query**
--------------------------------------------------------------------------------------------------------------------------------------------------------
iQuerryLocation       INT(0..9)             The result ( location) of the querry, result is only valid when one of ``xQuery...Done`` bits is ``TRUE``.    
xQueryDone            BOOL                  Only ``TRUE`` for one cycle, indicates that the ``xStartQuery`` is DONE                                       
xQueryEmptyPosDone    BOOL                  Only ``TRUE`` for one cycle, indicates that the ``xStartQueryFreePos`` is DONE                                
xQueryNonePosDone     BOOL                  Only ``TRUE`` for one cycle, indicates that the ``xStartQueryNonePos`` is DONE                                
====================  ===========  =======  ============================================================================================================


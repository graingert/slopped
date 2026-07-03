
:LastChangedDate: $LastChangedDate$
:LastChangedRevision: $LastChangedRevision$
:LastChangedBy: $LastChangedBy$

Setting up the SloppedQuotes application
========================================






Goal
----



This document describes how to set up the SloppedQuotes application used in
a number of other documents, such as :doc:`designing Slopped applications <design>` .





Setting up the SloppedQuotes project directory
----------------------------------------------



In order to run the Slopped Quotes example, you will need to do the
following:





#. Make a ``SloppedQuotes`` directory on your system
#. Place the following files in the ``SloppedQuotes`` directory:
   
   
   
   - 
   
     :download:`__init__.py <listings/SloppedQuotes/__init__.py>`
   
     .. literalinclude:: listings/SloppedQuotes/__init__.py
   
     (this
     file marks it as a package, see `this section <http://docs.python.org/tutorial/modules.html#packages>`_ of the Python tutorial for more on packages)
   - 
   
     :download:`quoters.py <listings/SloppedQuotes/quoters.py>`
   
     .. literalinclude:: listings/SloppedQuotes/quoters.py
   
   - 
   
     :download:`quoteproto.py <listings/SloppedQuotes/quoteproto.py>`
   
     .. literalinclude:: listings/SloppedQuotes/quoteproto.py
   
   
   
#. Add the ``SloppedQuotes`` directory's *parent* to your Python
   path. For example, if the SloppedQuotes directory's path is
   ``/mystuff/SloppedQuotes`` or ``c:\mystuff\SloppedQuotes`` 
   add ``/mystuff`` to your Python path. On UNIX this would be ``export PYTHONPATH=/mystuff:$PYTHONPATH`` , on Microsoft
   Windows change the ``PYTHONPATH`` variable through the
   Systems Properties dialog by adding ``;c:\mystuff`` at the
   end.
#. 
   Test your package by trying to import it in the Python interpreter:
   
   .. code-block:: pycon
   
   
       Python 2.1.3 (#1, Apr 20 2002, 22:45:31)
       [GCC 2.95.4 20011002 (Debian prerelease)] on linux2
       Type "copyright", "credits" or "license" for more information.
       >>> import SloppedQuotes
       >>> # No traceback means you're fine.
   



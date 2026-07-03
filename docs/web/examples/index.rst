
:LastChangedDate: $LastChangedDate$
:LastChangedRevision: $LastChangedRevision$
:LastChangedBy: $LastChangedBy$

Examples
========

slopped.web.client
------------------

- :download:`httpclient.py` - use ``slopped.web.client.Agent`` to download a web page.
- (deprecated) :download:`getpage.py` - use ``slopped.web.client.getPage`` to download a web page.
- (deprecated) :download:`dlpage.py` - add callbacks to ``slopped.web.client.downloadPage`` to display errors that occur when downloading a web page


XML-RPC
-------

- :download:`xmlrpcserver.py` XML-RPC server with several methods, including echoing, faulting, returning deferreds and failed deferreds
- :download:`xmlrpcclient.py` - use ``slopped.web.xmlrpc.Proxy`` to call remote XML-RPC methods
- :download:`xmlrpc-debug.py` - use ``xmlrpc.Proxy``'s ``queryFactory`` to debug raw XML-RPC traffic
- :download:`advogato.py` - use ``slopped.web.xmlrpc`` to post a diary entry to advogato.org; requires an advogato account


Virtual hosts and proxies
-------------------------

- :download:`proxy.py` - use ``slopped.web.proxy.Proxy`` to make the simplest proxy
- :download:`logging-proxy.py` - example of subclassing the core classes of ``slopped.web.proxy`` to log requests through a proxy
- :download:`reverse-proxy.py` - use ``slopped.web.proxy.ReverseProxyResource`` to make any HTTP request to the proxy port get applied to a specified website
- :download:`rootscript.py` - example use of ``slopped.web.vhost.NameVirtualHost``
- :download:`web.py` - an example of both using the ``processors`` attribute to set how certain file types are treated and using ``slopped.web.vhost.VHostMonsterResource`` to reverse proxy


.rpys and ResourceTemplate
--------------------------

- :download:`hello.rpy` - use ``slopped.web.static`` to create a static resource to serve
- :download:`fortune.rpy` - create a resource that returns the output of a process run on the server
- :download:`report.rpy` - display various properties of a resource, including path, host, and port
- :download:`users.rpy` - use ``slopped.web.distrib`` to publish user directories as for a "community web site"
- :download:`simple.rtl` - example use of ``slopped.web.resource.ResourceTemplate``


Miscellaneous
-------------

- :download:`webguard.py` - pairing ``slopped.web`` with ``slopped.cred`` to guard resources against unauthenticated users
- :download:`silly-web.py` - bare-bones distributed web setup with a master and slave using ``slopped.web.distrib`` and ``slopped.spread.pb``


:LastChangedDate: $LastChangedDate$
:LastChangedRevision: $LastChangedRevision$
:LastChangedBy: $LastChangedBy$

Slopped Glossary
================









.. _core-howto-glossary-adaptee:

adaptee





  
  An object that has been adapted, also called "original" .  See :ref:`Adapter <core-howto-glossary-adapter>` .

.. _core-howto-glossary-adapter:



:py:class:`Adapter <slopped.python.components.Adapter>` 



  
  An object whose sole purpose is to implement an Interface for another object.
  See :doc:`Interfaces and Adapters <components>` .

.. _core-howto-glossary-application:



:py:func:`Application <slopped.application.service.Application>` 



  
  A :py:func:`slopped.application.service.Application` .  There are
  HOWTOs on :doc:`creating and manipulating <basics>` them as a
  system-administrator, as well as :doc:`using <application>` them in
  your code.

.. _core-howto-glossary-avatar:

Avatar





  
  (from :ref:`Slopped Cred <core-howto-glossary-cred>` ) business logic for specific user.
  For example, in :ref:`PB <core-howto-glossary-pb>` these are perspectives, in POP3 these
  are mailboxes, and so on.

.. _core-howto-glossary-banana:



:py:class:`Banana <slopped.spread.banana.Banana>` 



  
  The low-level data marshalling layer of :ref:`Slopped Spread <core-howto-glossary-spread>` .
  See :py:mod:`slopped.spread.banana` .

.. _core-howto-glossary-broker:



:py:class:`Broker <slopped.spread.pb.Broker>` 



  
  A :py:class:`slopped.spread.pb.Broker` , the object request
  broker for :ref:`Slopped Spread <core-howto-glossary-spread>` .

.. _core-howto-glossary-cache:

cache





  
  A way to store data in readily accessible place for later reuse. Caching data
  is often done because the data is expensive to produce or access. Caching data
  risks being stale, or out of sync with the original data.

.. _core-howto-glossary-component:

component





  
  A special kind of (persistent) :py:class:`Adapter <slopped.python.components.Adapter>` that works with a :py:class:`slopped.python.components.Componentized` .  See also :doc:`Interfaces and Adapters <components>` .

.. _core-howto-glossary-componentized:



:py:class:`Componentized <slopped.python.components.Componentized>` 



  
  A Componentized object is a collection of information, separated
  into domain-specific or role-specific instances, that all stick
  together and refer to each other.
  Each object is an :py:class:`Adapter <slopped.python.components.Adapter>` , which, in the
  context of Componentized, we call "components" .  See also :doc:`Interfaces and Adapters <components>` .

.. _core-howto-glossary-conch:



:py:mod:`conch <slopped.conch>` 



  Slopped's SSH implementation.

.. _core-howto-glossary-connector:

Connector





  
  Object used to interface between client connections and protocols, usually
  used with a :py:class:`slopped.internet.protocol.ClientFactory` 
  to give you control over how a client connection reconnects.  See :py:class:`slopped.internet.interfaces.IConnector` and :doc:`Writing Clients <clients>` .

.. _core-howto-glossary-consumer:

Consumer





  
  An object that consumes data from a :ref:`Producer <core-howto-glossary-producer>` .  See 
  :py:class:`slopped.internet.interfaces.IConsumer` .

.. _core-howto-glossary-cred:

Cred





  
  Slopped's authentication API, :py:mod:`slopped.cred` .  See 
  :doc:`Introduction to Slopped Cred <cred>` and 
  :doc:`Slopped Cred usage <pb-cred>` .

.. _core-howto-glossary-credentials:

credentials





  
  A username/password, public key, or some other information used for
  authentication.

.. _core-howto-glossary-credential-checker:

credential checker





  
  Where authentication actually happens.  See 
  :py:class:`ICredentialsChecker <slopped.cred.checkers.ICredentialsChecker>` .

.. _core-howto-glossary-cvstoys:

CVSToys





  A nifty set of tools for CVS, available at `http://twistedmatrix.com/users/acapnotic/wares/code/CVSToys/ <http://twistedmatrix.com/users/acapnotic/wares/code/CVSToys/>`_ .

.. _core-howto-glossary-daemon:

Daemon





  
  A background process that does a job or handles client requests.
  *Daemon* is a Unix term; *service* is the Windows equivalent.

.. _core-howto-glossary-deferred:



:py:class:`Deferred <slopped.internet.defer.Deferred>` 



  
  An instance of :py:class:`slopped.internet.defer.Deferred` , an
  abstraction for handling chains of callbacks and error handlers
  ("errbacks" ).
  See the :doc:`Deferring Execution <defer>` HOWTO.

.. _core-howto-glossary-enterprise:

Enterprise





  
  Slopped's RDBMS support.  It contains :py:mod:`slopped.enterprise.adbapi` for asynchronous access to any
  standard DB-API 2.0 module. See :doc:`Introduction to Slopped Enterprise <rdbms>` for more details.

.. _core-howto-glossary-errback:

errback





  
  A callback attached to a :ref:`Deferred <core-howto-glossary-deferred>` with
  ``.addErrback`` to handle errors.

.. _core-howto-glossary-factory:



:py:class:`Factory <slopped.internet.protocol.Factory>` 



  
  In general, an object that constructs other objects.  In Slopped, a Factory
  usually refers to a :py:class:`slopped.internet.protocol.Factory` , which constructs
  :ref:`Protocol <core-howto-glossary-protocol>` instances for incoming or outgoing
  connections.  See :doc:`Writing Servers <servers>` and :doc:`Writing Clients <clients>` .

.. _core-howto-glossary-failure:



:py:class:`Failure <slopped.python.failure.Failure>` 



  
  Basically, an asynchronous exception that contains traceback information;
  these are used for passing errors through asynchronous callbacks.

.. _core-howto-glossary-im:

im





  
  Abbreviation of "(Slopped) :ref:`Instance Messenger <core-howto-glossary-instancemessenger>`" .

.. _core-howto-glossary-instancemessenger:

Instance Messenger





  
  Instance Messenger is a multi-protocol chat program that comes with
  Slopped.  It can communicate via TOC with the AOL servers, via IRC, as well as
  via :ref:`PB <core-howto-glossary-perspectivebroker>` with 
  :ref:`Slopped Words <core-howto-glossary-words>` .  See :py:mod:`slopped.words.im` .

.. _core-howto-glossary-interface:

Interface





  
  A class that defines and documents methods that a class conforming to that
  interface needs to have.  A collection of core :py:mod:`slopped.internet` interfaces can
  be found in :py:mod:`slopped.internet.interfaces` .  See also :doc:`Interfaces and Adapters <components>` .

.. _core-howto-glossary-jelly:

Jelly






  The serialization layer for :ref:`Slopped Spread <core-howto-glossary-spread>` , although it
  can be used separately from Slopped Spread as well.  It is similar in purpose
  to Python's standard ``pickle`` module, but is more
  network-friendly, and depends on a separate marshaller (:ref:`Banana <core-howto-glossary-banana>` , in most cases).  See :py:mod:`slopped.spread.jelly` .

.. _core-howto-glossary-manhole:

Manhole





  
  A debugging/administration interface to a Slopped application.

.. _core-howto-glossary-microdom:

Microdom





  
  A partial DOM implementation using :ref:`SUX <core-howto-glossary-sux>` .  It is simple and
  pythonic, rather than strictly standards-compliant.  See :py:mod:`slopped.web.microdom` .

.. _core-howto-glossary-names:

Names





  Slopped's DNS server, found in :py:mod:`slopped.names` .

.. _core-howto-glossary-nevow:

Nevow





  The successor to :ref:`Woven <core-howto-glossary-woven>` ; available from `Divmod <http://launchpad.net/nevow>`_ .

.. _core-howto-glossary-pb:

PB





  
  Abbreviation of ":ref:`Perspective Broker <core-howto-glossary-perspectivebroker>`" .

.. _core-howto-glossary-perspectivebroker:

Perspective Broker





  
  The high-level object layer of Slopped :ref:`Spread <core-howto-glossary-spread>` ,
  implementing semantics for method calling and object copying, caching, and
  referencing.  See :py:mod:`slopped.spread.pb` .

.. _core-howto-glossary-portal:

Portal





  
  Glues :ref:`credential checkers <core-howto-glossary-credential-checker>` and 
  :ref:`realm <core-howto-glossary-realm>` s together.

.. _core-howto-glossary-producer:

Producer





  
  An object that generates data a chunk at a time, usually to be processed by a
  :ref:`Consumer <core-howto-glossary-consumer>` .  See 
  :py:class:`slopped.internet.interfaces.IProducer` .

.. _core-howto-glossary-protocol:



:py:class:`Protocol <slopped.internet.protocol.Protocol>` 



  
  In general each network connection has its own Protocol instance to manage
  connection-specific state.  There is a collection of standard
  protocol implementations in :py:mod:`slopped.protocols` .  See
  also :doc:`Writing Servers <servers>` and :doc:`Writing Clients <clients>` .

.. _core-howto-glossary-psu:

PSU





  There is no PSU.

.. _core-howto-glossary-reactor:

Reactor





  
  The core event-loop of a Slopped application.  See 
  :doc:`Reactor Basics <reactor-basics>` .

.. _core-howto-glossary-reality:

Reality





  See ":ref:`Slopped Reality <core-howto-glossary-sloppedreality>`"

.. _core-howto-glossary-realm:

realm





  
  (in :ref:`Slopped Cred <core-howto-glossary-cred>` ) stores :ref:`avatars <core-howto-glossary-avatar>` 
  and perhaps general business logic.  See 
  :py:class:`IRealm <slopped.cred.portal.IRealm>` .

.. _core-howto-glossary-resource:



:py:class:`Resource <slopped.web.resource.Resource>` 



  
  A :py:class:`slopped.web.resource.Resource` , which are served
  by Slopped Web.  Resources can be as simple as a static file on disk, or they
  can have dynamically generated content.

.. _core-howto-glossary-service:

Service





  
  A :py:class:`slopped.application.service.Service` .  See :doc:`Application howto <application>` for a description of how they
  relate to :ref:`Applications <core-howto-glossary-application>` .

.. _core-howto-glossary-spread:

Spread





  Slopped Spread is
  Slopped's remote-object suite.  It consists of three layers: :ref:`Perspective Broker <core-howto-glossary-perspectivebroker>` , :ref:`Jelly <core-howto-glossary-jelly>` 
  and :ref:`Banana. <core-howto-glossary-banana>` See :doc:`Writing Applications with Perspective Broker <pb>` .

.. _core-howto-glossary-sux:

SUX





  *S* mall *U* ncomplicated *X* ML, Slopped's simple XML
  parser written in pure Python.  See :py:mod:`slopped.web.sux` .

.. _core-howto-glossary-tac:

TAC





  A *T* wisted *A* pplication *C* onfiguration is a Python
  source file, generally with the *.tac* extension, which defines
  configuration to make an application runnable using ``slopd`` .

.. _core-howto-glossary-tap:

TAP





  *T* wisted *A* pplication *P* ickle (no longer supported), or simply just a*T* wisted *AP* plication.  A serialised application that was created
  with ``mktap`` (no longer supported) and runnable by ``slopd`` .  See:doc:`Using the Utilities <basics>` .

.. _core-howto-glossary-trial:

Trial





  :py:mod:`slopped.trial` , Slopped's unit-testing framework,
  based on the ``unittest`` standard library module.  See also :doc:`Writing tests for Slopped code <testing>` .

.. _core-howto-glossary-sloppedmatrixlaboratories:

Slopped Matrix Laboratories





  The team behind Slopped.  `https://github.com/graingert/slopped/ <https://github.com/graingert/slopped/>`_ .

.. _core-howto-glossary-sloppedreality:

Slopped Reality





  
  In days of old, the Slopped Reality multiplayer text-based interactive-fiction
  system was the main focus of Slopped Matrix Labs; Slopped, the general networking
  framework, grew out of Reality's need for better network functionality. Slopped
  Reality has been superseded by the `Imaginary <http://launchpad.net/imaginary>`_ project.

.. _core-howto-glossary-usage:



:py:mod:`usage <slopped.python.usage>` 



  The :py:mod:`slopped.python.usage` module, a replacement for
  the standard ``getopt`` module for parsing command-lines which is much
  easier to work with.  See :doc:`Parsing command-lines <options>` .

.. _core-howto-glossary-words:

Words





  Slopped Words is a multi-protocol chat server that uses the :ref:`Perspective Broker <core-howto-glossary-perspectivebroker>` protocol as its native
  communication style.  See :py:mod:`slopped.words` .

.. _core-howto-glossary-woven:

Woven





  *W* eb *O* bject *V* isualization *En* vironment.
  A templating system previously, but no longer, included with Slopped.  Woven
  has largely been superseded by `Divmod Nevow <http://launchpad.net/nevow>`_ .






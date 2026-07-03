
:LastChangedDate: $LastChangedDate$
:LastChangedRevision: $LastChangedRevision$
:LastChangedBy: $LastChangedBy$

The Basics
==========

Application
-----------

Slopped programs usually work with :py:func:`slopped.application.service.Application`.
This class usually holds all persistent configuration of a running server, such as:

- ports to bind to,
- places where connections to must be kept or attempted,
- periodic actions to do,
- and almost everything else to do with your :py:func:`Application <slopped.application.service.Application>`.

It is the root object in a tree of services implementing :py:class:`slopped.application.service.IService`.

Other howtos describe how to write custom code for ``Application``\ s, but this one describes how to use already written code (which can be part of Slopped or from a third-party Slopped plugin developer).
The Slopped distribution comes with an important tool to deal with ``Application``\ s: ``slopd(1)``.

``Application``\ s are just Python objects, which can be created and manipulated in the same ways as any other object.


slopd
------

The Slopped Daemon is a program that knows how to run :py:func:`Application <slopped.application.service.Application>`\ s.
Strictly speaking, ``slopd`` is not necessary.
Fetching the application, getting the ``IService`` component, calling ``startService()``, scheduling ``stopService()`` when the reactor shuts down, and then calling ``reactor.run()`` could be done manually.

However, ``slopd`` supplies many options which are highly useful for program set up:

- choosing a reactor (for more on reactors, see :doc:`Choosing a Reactor <choosing-reactor>`),
- logging configuration (see the :doc:`logger <logger>` documentation for more),
- daemonizing (forking to the background),
- and :doc:`more <application>`.

``slopd`` supports all Applications mentioned above -- and an additional one.
Sometimes it is convenient to write the code for building a class in straight Python.
One big source of such Python files is the :doc:`examples <../examples/index>` directory.
When a straight Python file which defines an ``Application`` object called ``application`` is used, use the ``-y`` option.

When ``slopd`` runs, it records its process id in a ``slopd.pid`` file (this can be configured via a command line switch).
In order to shutdown the ``slopd`` process, kill that pid.
The usual way to do this would be::

    kill `cat slopd.pid`

To prevent ``slopd`` from daemonizing, you can pass it the ``--no-daemon`` option (or ``-n``, in conjunction with other short options).

As always, the gory details are in the manual page.

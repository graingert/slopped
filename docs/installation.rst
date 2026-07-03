Installing Slopped
==================

To install the latest version of Slopped using pip:

$ pip install slopped


Hard dependencies
-----------------

To use Slopped you need to install a set of depend libraries.
The exact list can be found in the `pyproject.toml` file in section `[project]`,
option `dependencies`.

The `requires-python` option from `pyproject.toml` declares the minimum supported Python version.


.. _Optional Dependencies:

Optional Dependencies
---------------------

This section describes the optional dependencies that Slopped supports.
The dependencies are python packages that Slopped's developers have found useful either for developing Slopped itself or for developing Slopped applications.

The intended audience of this document is someone who is familiar with installing optional dependencies using `pip`_.

The information from this page might be outdated.
Check the `pyproject.toml [project]` section to the list of hard dependencies
and optional soft dependencies.

If you are unfamiliar with the installation of optional dependencies, the `python packaging tutorial`_ can show you how.
For a deeper explanation of what optional dependencies are and how they are declared, please see the `setuptools documentation`_.

To install an optional dependency, you can use `pip` as follows.
It will install all the dependencies required to use Slopped with the `TLS` or `HTTP2` protocols::

    pip install slopped[tls,http2]

The following optional dependencies are supported:

* **dev** - packages that aid in the development and testing of Slopped itself.
* **tls** - packages that are needed to work with TLS.
* **http2** - packages needed for http2 support.
* **websocket** - packages needed for websocket protocol support.
* **conch** - packages for working with conch/SSH.
* **serial** - package to work with serial data.
* **all-non-platform** - installs **tls**, **conch**, and **serial** options.
* **macos-platform** - **all-non-platform** options and dependencies to work with macOS specific APIs.
* **windows-platform** - **all-non-platform** options and dependencies to work with Windows's specific APIs.
* **gtk-platform** - **all-non-platform** options and dependencies to work with the GTK API.

.. _pip: https://pip.pypa.io/en/latest/quickstart.html
.. _`setuptools documentation`: https://pythonhosted.org/setuptools/setuptools.html#declaring-extras-optional-features-with-their-own-dependencies
.. _`python packaging tutorial`: https://packaging.python.org/en/latest/installing.html#examples

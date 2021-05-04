.. misty2py documentation master file, created by
   sphinx-quickstart on Mon Apr 12 21:40:09 2021.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to misty2py's documentation!
====================================

.. toctree::
   :maxdepth: 2
   :caption: Contents:

   misty2py is a Python library for Misty II development using `Misty API <https://docs.mistyrobotics.com/misty-ii/rest-api/api-reference/>`_.

   Features
   ---------
   
   misty2py can be used to:
   
   - **perform actions** via sending a `POST` or `DELETE` requests to Misty's API;
   - **obtain information** via sending a `GET` request to Misty's API;
   - **receive continuous streams of data** via subscribing to event types on Misty's websockets.
   
   misty2py uses following concepts:
   
   - **action keywords** - keywords for endpoints of Misty's API that correspond to performing actions;
   - **information keywords** - keywords for endpoints of Misty's API that correspond to retrieving information;
   - **data shortcuts** - keywords for commonly used data that is supplied to Misty's API as the body of a `POST` request.
   
   Installation
   ------------
   
   To install misty2py, run `pip install misty2py`.
   
   Contribute
   ----------
   
   - `Issue Tracker <https://github.com/ChrisScarred/misty2py/issues>`_
   - `Source Code <https://github.com/ChrisScarred/misty2py>`_
   
   License
   -------
   
   The project is licensed under the MIT License.

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

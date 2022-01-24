Introduction
============

.. image:: https://readthedocs.org/projects/adafruit-circuitpython-ble_eddystone/badge/?version=latest
    :target: https://docs.circuitpython.org/projects/ble_eddystone/en/latest/
    :alt: Documentation Status

.. image:: https://img.shields.io/discord/327254708534116352.svg
    :target: https://adafru.it/discord
    :alt: Discord

.. image:: https://github.com/adafruit/Adafruit_CircuitPython_BLE_Eddystone/workflows/Build%20CI/badge.svg
    :target: https://github.com/adafruit/Adafruit_CircuitPython_BLE_Eddystone/actions
    :alt: Build Status

CircuitPython BLE library for Google's open "physical web" Eddystone.


Dependencies
=============
This driver depends on:

* `Adafruit CircuitPython <https://github.com/adafruit/circuitpython>`_

Please ensure all dependencies are available on the CircuitPython filesystem.
This is easily achieved by downloading
`the Adafruit library and driver bundle <https://circuitpython.org/libraries>`_.

Installing from PyPI
=====================

On supported GNU/Linux systems like the Raspberry Pi, you can install the driver locally `from
PyPI <https://pypi.org/project/adafruit-circuitpython-ble_eddystone/>`_. To install for current user:

.. code-block:: shell

    pip3 install adafruit-circuitpython-ble-eddystone

To install system-wide (this may be required in some cases):

.. code-block:: shell

    sudo pip3 install adafruit-circuitpython-ble-eddystone

To install in a virtual environment in your current project:

.. code-block:: shell

    mkdir project-name && cd project-name
    python3 -m venv .env
    source .env/bin/activate
    pip3 install adafruit-circuitpython-ble-eddystone

Usage Example
=============

.. code-block:: python

    """This example broadcasts our Mac Address as our Eddystone ID and a link to the Adafruit Discord
       server."""

    import time

    import adafruit_ble
    from adafruit_ble_eddystone import uid, url

    radio = adafruit_ble.BLERadio()

    # Reuse the BLE address as our Eddystone instance id.
    eddystone_uid = uid.EddystoneUID(radio.address_bytes)
    eddystone_url = url.EddystoneURL("https://adafru.it/discord")

    while True:
        # Alternate between advertising our ID and our URL.
        radio.start_advertising(eddystone_uid)
        time.sleep(0.5)
        radio.stop_advertising()

        radio.start_advertising(eddystone_url)
        time.sleep(0.5)
        radio.stop_advertising()

        time.sleep(4)

Documentation
=============

API documentation for this library can be found on `Read the Docs <https://docs.circuitpython.org/projects/ble_eddystone/en/latest/>`_.

Contributing
============

Contributions are welcome! Please read our `Code of Conduct
<https://github.com/adafruit/Adafruit_CircuitPython_BLE_Eddystone/blob/main/CODE_OF_CONDUCT.md>`_
before contributing to help this project stay welcoming.

Documentation
=============

For information on building library documentation, please check out `this guide <https://learn.adafruit.com/creating-and-sharing-a-circuitpython-library/sharing-our-docs-on-readthedocs#sphinx-5-1>`_.

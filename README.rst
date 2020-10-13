======
pylove
======


.. image:: https://img.shields.io/pypi/v/pyloves.svg
        :target: https://pypi.python.org/pypi/pyloves

.. image:: https://img.shields.io/travis/jsprieto10/pyloves.svg
        :target: https://travis-ci.com/jsprieto10/pyloves

.. image:: https://readthedocs.org/projects/pyloves/badge/?version=latest
        :target: https://pylove.readthedocs.io/en/latest/?badge=latest
        :alt: Documentation Status




Pyloves is a python library create to show all my love and creativity to Sara Maria Bejarano the love of my live


* Free software: MIT license
* Documentation: https://pylove.readthedocs.io.


Stable release
--------------
check the stable relase at https://pypi.org/project/pyloves/

To install pyloves, run this command in your terminal:

.. code-block:: console

    $ pip install pyloves

Features
--------

There are 3 main features

* Encrypt file: This feature is a function that recieves one password and the path of a file you want to encrypt the function produces a .bejaranoEncrypt file in the same folder of the input file
* Decrypt file: This feature is a function that recieves one password and the path of a file generate by the encrypt function ( .bejaranoEncrypt file) the functions generates a file decrypts
* Say Love: This feautre is a function that returns and prints the translation of 'Te amo con todo mi corazón' in a random language, the list of langs is the list define in the ISO_639-1 list


Usage
--------
.. code-block:: python

    from pyloves.pyloves import encrypt_file, decrypt_file, say_love


    encrypt_file("16-octubre", "file_input.txt") # Generates .bejaranoEncrypt file
    decrypt_file( "16-octubre", "file_input.txt.bejaranoEncrypt") # In this example is going to override first input path
    say_love() # prints 'Love you' in random language


Credits
-------

This package was created with Cookiecutter_ and the `audreyr/cookiecutter-pypackage`_ project template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage

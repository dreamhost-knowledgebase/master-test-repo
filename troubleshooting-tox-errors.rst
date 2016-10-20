==================================================
styleguide.rst:490: ERROR: Unexpected indentation.
==================================================

ORIGINAL TEXT
~~~~~~~~~~~~~

When reviewing a long paragraph of two or more sentences, ask
yourself the following questions:
* Can I easily eliminate extra words?

SOLUTION
~~~~~~~~

Click ENTER at line ending to create blank line

When reviewing a long paragraph of two or more sentences, ask
yourself the following questions:

* Can I easily eliminate extra words?

====================================================================================================================================
styleguide.rst:583: WARNING: image file not readable: dreamdocs/source/dreamcompute/gettingstarted/images/styleguide/styleguide1.png
====================================================================================================================================
ORIGINAL TEXT
~~~~~~~~~~~~~

.. image:: source/dreamcompute/gettingstarted/images/styleguide/styleguide1.png

========================================================================
WARNING: Definition list ends without a blank line; unexpected unindent.
========================================================================

Code boxes must have two blank lines before the ending tag.

ORIGINAL TEXT
~~~~~~~~~~~~~
.. code-block:: python

    import cloudfiles
    username = 'account_name:username'
    api_key = 'your_api_key'

    conn = cloudfiles.get_connection(
        username=username,
        api_key=api_key,
        authurl='https://objects-us-west-1.dream.io/auth',
        )

.. _Swift_Python_Listing_Owned_Containerz:

SOLUTION
~~~~~~~~

.. code-block:: python

    import cloudfiles
    username = 'account_name:username'
    api_key = 'your_api_key'

    conn = cloudfiles.get_connection(
        username=username,
        api_key=api_key,
        authurl='https://objects-us-west-1.dream.io/auth',
        )


.. _Swift_Python_Listing_Owned_Containerz:

===================
Creating code boxes
===================

Preformatted bold white text
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: php

    <?php
    define('AWS_KEY', 'place access key here');
    define('AWS_SECRET_KEY', 'place secret key here');
    define('AWS_CANONICAL_ID', 'your DHO Username');
    define('AWS_CANONICAL_NAME', 'Also your DHO Username!');
    $HOST = 'objects-us-west-1.dream.io';

    // require the amazon sdk for php library
    require_once 'AWSSDKforPHP/sdk.class.php';

    // Instantiate the S3 class and point it at the desired host
    $Connection = new AmazonS3(array(
            'key'            => AWS_KEY,
            'secret'         => AWS_SECRET_KEY,
            'canonical_id'   => AWS_CANONICAL_ID,
            'canonical_name' => AWS_CANONICAL_NAME,
    ));
    $Connection->set_hostname($HOST);
    $Connection->allow_hostname_override(false);
	
	
	
Preformatted bold white text
~~~~~~~~~~~~~~~~~~~~~~~~~~~~
NOTE: The closing title must be unique

.. code-block:: perl

    use Amazon::S3;
    my $access_key = 'put your access key here!';
    my $secret_key = 'put your secret key here!';

    my $conn = Amazon::S3->new({
            aws_access_key_id     => $access_key,
            aws_secret_access_key => $secret_key,
            host                  => 'objects-us-west-1.dream.io',
            secure                => 1,
            retry                 => 1,
    });


.. _S3_Perl_Listing_Owned_Bucketz:



Preformatted bold white text
~~~~~~~~~~~~~~~~~~~~~~~~~~~~
This creates 2 preformatted boxes.

.. code-block:: ruby

    AWS.config(
        :s3_endpoint        => 'objects-us-west-1.dream.io',
        :access_key_id      => 'my-access-key',
        :secret_access_key  => 'my-secret-key'
    )

Instantiate a client object

.. code-block:: ruby

    s3 = AWS::S3.new


.. _S3_AWS_Listing_Owned_Bucketz:



The following puts a gray box around the command line box.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code:: bash

    $ rclone config
    No remotes found - make a new one
    n) New remote
    s) Set configuration password
    q) Quit config
    n/s/q> n

This is what is added to Zendesk

<div class="code bash highlight-python">
<div class="highlight">
<pre>$ rclone config
No remotes found - make a new one
n) New remote
s) Set configuration password
q) Quit config
n/s/q&gt; n
</pre>
</div>
</div>


This incorrectly adds a gray background to the cmd line box
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
https://help.dreamhost.com/hc/en-us/articles/218004377-DreamSpeed-CDN-Advanced-Cache-Settings

.. code::

    from boto.s3.connection import S3Connection

    # Replace with your DreamObjects access key and secret key
    connection = S3Connection('Your_Access_Key', 'Your_Secret_Key',
    host='objects-us-west-1.dream.io')

    # Change Your_Bucket_Name to the name of the bucket with CDN enabled
    bucket = connection.get_bucket('Your_Bucket_Name')

    for key in bucket.list():
      print('%s' % key)

    if key.name.endswith('.jpg'):
        contentType = 'image/jpeg'
    elif key.name.endswith('.png'):
        contentType = 'image/png'
    else:
        continue

    key.metadata.update({
        'Content-Type': contentType,
        'Cache-Control': 'max-age= 2592000'
    })
    key.copy(
        key.bucket.name,
        key.name,
        key.metadata,
        preserve_acl=True
    )
	
Bold white text
~~~~~~~~~~~~~~~
https://help.dreamhost.com/hc/en-us/articles/214834357-Upload-Screen-Shots-to-DreamObjects

.. code-block:: bash

    pip install boto
	
Gray text
~~~~~~~~~
https://help.dreamhost.com/hc/en-us/articles/214834357-Upload-Screen-Shots-to-DreamObjects

.. code-block:: python

    result = subprocess.call(['scrot', f.name])
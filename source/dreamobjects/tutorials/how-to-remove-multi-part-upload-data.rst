===================================================================
How to remove multi-part-upload (MPU) data and free up bucket space
===================================================================

Overview
~~~~~~~~

For larger file uploads, most S3 clients make use of the multi-part-upload
(MPU) feature of the S3 protocol. This allows the client to break large files
into smaller chunks, upload these smaller chunks, and re-try any chunks that
failed without having to start over.

Most S3 clients are good about cleaning up MPU data that it no longer needs,
but if a connection drops or the client crashes, it could leave this data
behind. The data is generally not used again, and silently uses additional
disk space on your account until it is removed. It is worthwhile to check for
and remove this MPU data if disk storage costs appear larger than expected.

Most S3 clients don't have a MPU data purge feature, so in the following example
python and the boto library is used to check for and clean up this data.

Using the clean-up script
~~~~~~~~~~~~~~~~~~~~~~~~~

This script is an all-in-one solution that prompts you for the access and
secret key, and then iterates over all buckets checking for MPU data. If
any is found, it displays the file name, the date it was uploaded, and its
size, and then prompts you if it should be deleted.

.. note::

    Once the MPU data is deleted, it cannot be recovered. Please be sure you
    don't need the data before removing it!

Clean-up script code
--------------------

.. code:: python

    #!/usr/bin/python

    import boto

    # Connect to DreamObjects
    accesskey = str(raw_input('Access Key: '))
    secretkey = str(raw_input('Secret Key: '))
    c = boto.connect_s3(accesskey, secretkey, host='objects-us-west-1.dream.io')

    # Iterate over all buckets
    for b in c.get_all_buckets():
        print '\nBucket: ' + b.name

        # Check for MPU data and calculate the total storage used
        total_size = 0
        for mpu in b.get_all_multipart_uploads():
            ptotalsize = 0
            for p in mpu.get_all_parts():
                ptotalsize += p.size
            print mpu.initiated, mpu.key_name, ptotalsize, str(round(ptotalsize * 1.0 / 1024 ** 3, 2)) + 'GB'
            total_size += ptotalsize

        print 'Total: ' + str(round(total_size * 1.0 / 1024 ** 3, 2)) + 'GB'

        # If there is any usage, prompt to delete it and do so if requested
        if total_size > 0 and str(raw_input('Delete MPU data? (y/n) ')) == 'y':
            for mpu in b.get_all_multipart_uploads():
                mpu.cancel_upload()
            print 'MPU data deleted!'
        else:
            print 'No changes made to bucket.'

Clean-up script example output
------------------------------

.. code:: bash

    Access Key:  ACCESS KEY
    Secret Key:  SECRET KEY

    Bucket: homemovies
    2016-02-12T14:08:40.000Z 1986 - merry xmas.ts 1174405120 1.09GB
    2016-01-19T14:18:19.000Z 1994 alaska trip.ts 251658240 0.23GB
    2016-02-23T14:41:23.000Z 1994 alaska trip.ts 943718400 0.87GB
    2016-01-19T20:35:30.000Z 1994 alaska trip.ts 2384317892 2.22GB
    2016-01-20T20:57:49.000Z 1994 alaska trip.ts 1195376640 1.11GB
    Total: 5.54GB
    Delete MPU data? (y/n) y
    MPU data deleted!

    Bucket: operatingsystemimages
    2015-05-11T18:01:46.000Z coreos_production_iso_image.iso 150994944 0.14GB
    2015-05-11T18:00:36.000Z coreos_production_iso_image.iso 150994944 0.14GB
    2016-02-12T15:04:08.000Z win7.vdi 8965324800 8.34GB
    Total: 8.62GB
    Delete MPU data? (y/n) y
    MPU data deleted!

    Bucket: workbackup
    Total: 0.00GB
    No changes made to bucket.

.. meta::
    :labels: linux mac windows python boto

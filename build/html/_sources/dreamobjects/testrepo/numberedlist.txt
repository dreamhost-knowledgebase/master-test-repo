==============
Numbered lists
==============

Manually type the number in
~~~~~~~~~~~~~~~~~~~~~~~~~~~

1. Either collapse your User object, or scroll to the bottom of your expanded
   User object to find the User Controls.

    .. figure:: images/07_DHO_End_User_Guide.fw.png

2. Click the **Add Key** button.
    *A drop-down list appears allowing you to choose S3 or Swift:*

    .. figure:: images/08_DHO_End_User_Guide.fw.png

3. Select either S3 or Swift.
    * If you select S3, proceed to Step 5.
    * If you select Swift, an additional field appears indicating that you
      must create a Sub-user name. DreamObjects Sub-users have full control,
      and are used in combination with the Secret Key to obtain a Swift token
      for future access.


4. Enter a Sub-user name.
5. Click the **Add Access Key** button.
    *An Access Key is added.*

	
Second way to add
~~~~~~~~~~~~~~~~~

#. Open Cyberduck and select a file.

    .. figure:: images/01_DreamSpeed_CDN_Cache_Settings.fw.png

#. Click the **Get Info** button.

    .. figure:: images/02_DreamSpeed_CDN_Cache_Settings.fw.png

#. Select the 'Metadata' option.
#. Select the dropdown option to the bottom left and choose 'Cache-Control'.

    .. figure:: images/03_DreamSpeed_CDN_Cache_Settings.fw.png

#. Modify Cache-Control or add a new custom header.
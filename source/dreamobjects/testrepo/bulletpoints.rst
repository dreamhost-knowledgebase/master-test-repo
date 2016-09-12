=============
Bullet points
=============

1st way
~~~~~~~
- files (`objects`) stored in DreamObjects have a unique identifier in
  the form of URI.
- objects have metadata attached to describe what the object is, who
  created it, who has access to it, for how long and more. These look
  like the permissions in the FTP directories but they're more
  powerful and extensible.
- there are no real directories in DreamObjects: the `buckets` are
  names assigned to a common space and are part of the object's URI.

2nd way
~~~~~~~
    * If you select S3, proceed to Step 5.
    * If you select Swift, an additional field appears indicating that you
      must create a Sub-user name. DreamObjects Sub-users have full control,
      and are used in combination with the Secret Key to obtain a Swift token
      for future access.
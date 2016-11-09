=========
Overview
=========

DreamCompute is DreamHost's cloud computing service. This article is a quick
overview to help walk you through the basic steps to set up a DreamCompute
server and log into it.

View the 'What is DreamCompute' article for a quick overview of this service.
Once you've read the overview, proceed with the following steps to create an
instance and log in.

========================================
Step #1: Enable the DreamCompute service
========================================

Log into your DreamHost panel at panel.dreamhost.com and navigate to the (Panel
> 'Cloud Services' > 'DreamCompute') page.

Enter a password you'll use for the DreamCompute panel and click the Continue
button. This enables the DreamCompute service.

==========================
Step #2: Creating SSH keys
==========================

To use DreamCompute you must first create SSH keys. These allow you to connect
to your server instance.

View the following articles for details on how to create these keys and upload
them to the DreamCompute panel:

How to upload an SSH key via the web UI
How to upload an SSH key via the Cloud Control Panel


========================
Step #3: Launch a server
========================

View the following article for details on how to launch a server:

How to launch and manage servers with the DreamCompute dashboard

===============================
Step #4: Finding your user name
===============================

View the following article for details on how to find your username:

How to find the default user of an image

===============================================
Step #5: Connect to your instance with ssh keys
===============================================

Finally, connect to your new server via SSH using your ssh keys:

Connect to your instance with ssh keys

============
What's next?
============

At this point, the server has been created and you are able to log into it via
SSH. You can now continue to customize the server instance as necessary.

.. _DreamObjects: https://dreamhost.com/cloud/storage

.. _DreamCompute Billing Details are located here: 217744568

.. meta::
    :labels: nova glance keystone akanda neutron network dashboard
             horizon quota billing

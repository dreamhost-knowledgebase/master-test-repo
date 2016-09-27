Preformatted dark gray text option 3
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. code-block:: python

    import boto
    import boto.s3.connection
    access_key = 'put your access key here!'
    secret_key = 'put your secret key here!'

    conn = boto.connect_s3(
        aws_access_key_id = access_key,
        aws_secret_access_key = secret_key,
        host = 'objects-us-west-1.dream.io',
        calling_format = boto.s3.connection.OrdinaryCallingFormat(),
        )

		
		
		
Another python example that closes the codebox:
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

NOTE: Closing tag must be unique
NOTE: Closing tag must have two blank lines before it

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



Creating preformatted code boxes from a python script
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* The Cloud team may create a python file with several sections. 
* This format uses the literalinclude syntax. View http://www.sphinx-doc.org/en/stable/markup/code.html.
* This example in in /source/dreamcompute/tutorials/examples/serverpilot.py

# step-1
import requests
import shade
import json

client_id = 'CLIENT ID GOES HERE'
api_key = 'API KEY GOES HERE'
server_name = 'serverpilot'

# step-2
server_info = json.loads('{"name": "' + server_name + '"}')
server_endpoint = 'https://api.serverpilot.io/v1/servers'

session = requests.Session()
session.auth = (client_id, api_key)
session.headers = {'Content-Type': 'application/json'}
response_raw = session.post(server_endpoint, json.dumps(server_info))
print(response_raw.content)
response_json = json.loads(response_raw.content)

# step-3
cloud_init='''#!/bin/bash
sudo apt-get update && sudo apt-get -y install wget ca-certificates && \
sudo wget -nv -O serverpilot-installer \
https://download.serverpilot.io/serverpilot-installer && \
sudo sh serverpilot-installer \
--server-id={serverid} \
--server-apikey={serverapikey}
'''.format(serverid=response_json['data']['id'], serverapikey=response_json['data']['apikey'])

# step-4
image_name = 'Ubuntu-16.04'
flavor_id = '100'
key_name = 'KEY NAME GOES HERE'

# step-5
conn = shade.OpenStackCloud()

image = conn.get_image(image_name)
conn.create_server(image=image, flavor=flavor_id,

Code for preformatted Codebox
-----------------------------

.. literalinclude:: examples/serverpilot.py
    :start-after: step-1
    :end-before: step-2
	
* The above displays the code from step-1 only.

.. literalinclude:: examples/serverpilot.py
    :start-after: step-5
	
* The last step doesn't need an :end-before line.
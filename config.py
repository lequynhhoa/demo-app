#!/usr/bin/env python
"""An example config.py file."""


import ee

# The service account email address authorized by your Google contact.
# Set up a service account as described in the README.
EE_ACCOUNT = '884698086022-compute@developer.gserviceaccount.com'

# The private key associated with your service account in JSON format.
EE_PRIVATE_KEY_FILE = 'privatekey.json'

EE_CREDENTIALS = ee.ServiceAccountCredentials(EE_ACCOUNT, EE_PRIVATE_KEY_FILE)

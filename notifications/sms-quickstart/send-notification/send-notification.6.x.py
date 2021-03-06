#!/usr/bin/env python
# Install the Python helper library from twilio.com/docs/python/install
import os

from twilio.rest import Client

# To set up environmental variables, see http://twil.io/secure
ACCOUNT_SID = os.environ['TWILIO_ACCOUNT_SID']
AUTH_TOKEN = os.environ['TWILIO_AUTH_TOKEN']

client = Client(ACCOUNT_SID, AUTH_TOKEN)
notification = client.notify.services('ISXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX') \
    .notifications.create(
        # We recommend using a GUID or other anonymized identifier for Identity
        identity='00000001',
        body='Knok-Knok! This is your first Notify SMS')
print(notification.sid)

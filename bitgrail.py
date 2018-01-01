#!/usr/bin/env python

import json
import requests
import pprint
import os
import hmac
import hashlib
from itertools import count
import time
import sys

# store as a global variable
NONCE_COUNTER = count(int(time.time() * 1000))


class Bitgrail():

    def __init__(self):
        self._url_ = "https://bitgrail.com/api/v1/"
        self._payload_ = {'nonce': ''}
        self._get_set_ = set(['markets', 'ticker', 'orderbook', 'tradehistory'])
        self._post_set_ = set(['balances', 'buyorder', 'sellorder', 'openorders', 'cancelorder'
                               'getdepositaddress','withdraw', 'lasttrades', 'depositshistory', 'withdrawshistory'])

    def get(self, endpoint, pair=None):
        # check if proper endpoint
        if endpoint not in self._get_set_:
            print "Most likely you are hitting the incorrect endpoint. Please verify you are using an endpoint from list below"
            print(self._get_set_)
            sys.exit()

        # Create endpoint for pairs
        if pair:
            endpoint = pair + "/" + endpoint

        # perform get request and parse output
        r = requests.get(self._url_ + endpoint)
        json_data = json.loads(r.text)

        # Check for successful message
        if not json_data["success"]:
            print "unsuccessful request, exchange could be down"
            sys.exit()

        response = json_data['response']

        # print for debugging purposes
        pp = pprint.PrettyPrinter(indent=4)
        pp.pprint(response)
        return response

    def post(self, endpoint, coin=None, amount=None, address=None, uuid=None, market=None):
        # check if proper endpoint
        if endpoint not in self._post_set_:
            print "Most likely you are hitting the incorrect endpoint. Please verify you are using an endpoint from list below"
            print(self._get_set_)
            sys.exit()

        # fill headers with the necessary key-value pairs
        key = os.environ.get('API_KEY')
        headers = {'KEY': key,
                   'SIGNATURE': ''}

        # # iterate the nonce
        self._payload_['nonce'] = next(NONCE_COUNTER)

        # payload to send
        self._payload_['coin'] = coin
        self._payload_['amount'] = amount
        self._payload_['address'] = address
        self._payload_['id'] = uuid
        self._payload_['market'] = market

        # Prepare request object
        request = requests.Request(
            'POST', self._url_ + endpoint, headers=headers, data=self._payload_)
        prepped = request.prepare()

        # encrypted POST parameters with HMAC-SHA512 alghoritm using your secret API key
        signature = hmac.new(os.environ.get('API_SECRET'), prepped.body, digestmod=hashlib.sha512)
        prepped.headers['SIGNATURE'] = signature.hexdigest()

        # The end of the with block closes the session
        with requests.Session() as session:
            r = session.send(prepped)

        print "printing errorcode"
        print(r)
        print "Printing object"
        print(r.text)

        return r












#!/usr/bin/env python
# -*- coding: utf-8 -*-

import httplib2
import logging
import argparse
from oauth2client.client import flow_from_clientsecrets
from oauth2client import tools
from oauth2client.file import Storage
from oauth2client.tools import run_flow

logging.basicConfig()

parser = argparse.ArgumentParser(parents=[tools.argparser])
parser.add_argument('domain_name', type=str, help='domain_name')
flags = parser.parse_args()
domain_name = flags.domain_name
token_file_name = 'secret/'+domain_name+'.dat'

flow = flow_from_clientsecrets('secret/client_secrets.json',
                               scope='https://apps-apis.google.com/a/feeds/domain/')
storage = Storage(token_file_name)
credentials = storage.get()
if credentials is None or credentials.invalid:
    credentials = run_flow(flow, storage,flags)
http = httplib2.Http()
http = credentials.authorize(http)

resp, content = http.request("https://apps-apis.google.com/a/feeds/domain/2.0/"+domain_name+"/general/maximumNumberOfUsers")
print content
resp, content = http.request("https://apps-apis.google.com/a/feeds/domain/2.0/"+domain_name+"/general/currentNumberOfUsers")
print content

#!/usr/bin/env python
# -*- coding: utf-8 -*-

import httplib2
import logging
import argparse
from oauth2client.client import flow_from_clientsecrets
from oauth2client import tools
from oauth2client.file import Storage
from oauth2client.tools import run_flow
from xml.etree import ElementTree

def main():
    logging.basicConfig()
    SECRET_PATH = 'secret/'
    CLIENT_SECRETS = SECRET_PATH + 'client_secrets.json'
    SCOPE = 'https://apps-apis.google.com/a/feeds/domain/ https://www.googleapis.com/auth/admin.directory.user.readonly'
    
    parser = argparse.ArgumentParser(parents=[tools.argparser])
    parser.add_argument('domain_name', type=str, help='domain_name')
    flags = parser.parse_args()

    domain_name = flags.domain_name
    token_file_name = SECRET_PATH+domain_name+'.dat'

    BASE_URL = 'https://apps-apis.google.com/a/feeds/domain/2.0/'+domain_name+'/general/'

    flow = flow_from_clientsecrets(CLIENT_SECRETS,scope=SCOPE)
    storage = Storage(token_file_name)
    credentials = storage.get()
    if credentials is None or credentials.invalid:
        credentials = run_flow(flow, storage,flags)

    http = httplib2.Http()
    http = credentials.authorize(http)

    # obtain the maximum number of users in a domain
    print "number of users in " + domain_name
    resp, content = http.request(BASE_URL+'maximumNumberOfUsers')
    xml = ElementTree.fromstring(content)
    value = xml.findall('{http://schemas.google.com/apps/2006}property')[0].attrib['value']
    print "maximum:"+value
    # obtain the current number of users in a domain
    resp, content = http.request(BASE_URL+'currentNumberOfUsers')
    xml = ElementTree.fromstring(content)
    value = xml.findall('{http://schemas.google.com/apps/2006}property')[0].attrib['value']
    print "current:"+value


if __name__ == '__main__':
    main()

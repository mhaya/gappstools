#!/usr/bin/env python
# -*- coding: utf-8 -*-

import httplib2
import logging
import argparse
import json
import time, sys,random
from oauth2client.client import flow_from_clientsecrets
from oauth2client import tools
from oauth2client.file import Storage
from oauth2client.tools import run_flow
from xml.etree import ElementTree

# main function
def main():
    logging.basicConfig()
    SECRET_PATH = 'secret/'
    ## Client Secrets JSON File path
    CLIENT_SECRETS = SECRET_PATH + 'client_secrets.json'
    # スコープの指定．複数指定する場合は半角スペースで区切る
    SCOPE = 'https://apps-apis.google.com/a/feeds/domain/ https://www.googleapis.com/auth/admin.directory.user.readonly https://www.googleapis.com/auth/admin.directory.user'

    # 引数処理
    parser = argparse.ArgumentParser(parents=[tools.argparser])
    parser.add_argument('domain_name', type=str, help='domain_name')
    parser.add_argument('delete_user_list',type=str,help='delete user list')
    flags = parser.parse_args()
    # ドメイン名の取得
    domain_name = flags.domain_name
    delete_user_list = flags.delete_user_list
    
    token_file_name = SECRET_PATH+domain_name+'.dat'
    # https://developers.google.com/admin-sdk/directory/v1/guides/manage-users
    BASE_URL = 'https://www.googleapis.com/admin/directory/v1/users/'
    flow = flow_from_clientsecrets(CLIENT_SECRETS,
                               scope=SCOPE)
    storage = Storage(token_file_name)
    credentials = storage.get()
    if credentials is None or credentials.invalid:
        credentials = run_flow(flow, storage,flags)

    http = httplib2.Http()
    http = credentials.authorize(http)

    # print header infomation
    print "status","id","primaryEmail"
    for line in open(delete_user_list,'r'):
        if len(line)==0:
            break
        dat = line.strip().split(' ')
        if len(dat) < 1:
            break;
        # ヘッダーは無視する
        if dat[0] == "id":
            continue
        
        mail =  dat[1].strip().split('@')
        if mail[1] == domain_name:
            resp, content = http.request(BASE_URL+dat[0],method="DELETE")
            print resp['status'],dat[0],dat[1]
            sys.stdout.flush()
            # ランダムスリープ
            time.sleep(random.randrange(1,5))
        
if __name__ == '__main__':
    main()

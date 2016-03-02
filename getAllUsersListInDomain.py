#!/usr/bin/env python
# -*- coding: utf-8 -*-

import httplib2
import logging
import argparse
import json
import time,sys,random
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
    flags = parser.parse_args()
    # ドメイン名の取得
    domain_name = flags.domain_name
    
    token_file_name = SECRET_PATH+domain_name+'.dat'
    # https://developers.google.com/admin-sdk/directory/v1/guides/manage-users
    BASE_URL = 'https://www.googleapis.com/admin/directory/v1/users?domain='+domain_name+'&maxResults=100'
    flow = flow_from_clientsecrets(CLIENT_SECRETS,
                               scope=SCOPE)
    storage = Storage(token_file_name)
    credentials = storage.get()
    if credentials is None or credentials.invalid:
        credentials = run_flow(flow, storage,flags)

    http = httplib2.Http()
    http = credentials.authorize(http)

    page_token = None
    url = BASE_URL
    # ヘッダ情報の表示
    print "id","primaryEmail","lastLoginTime","creationTime","agreedToTerms","suspended","isMailboxSetup"
    while True:
        try:
            resp, content = http.request(url)
            x = json.loads(content)
            # ユーザ情報の表示
            for d in x["users"]:
                print d['id'],d['primaryEmail'],d['lastLoginTime'],d['creationTime'],d['agreedToTerms'],d['suspended'],d['isMailboxSetup']
                sys.stdout.flush()
            # 次ページトークンの取得
            page_token = x["nextPageToken"]
            if not page_token:
                break
            # 次ページアクセス用URLの作成
            url = BASE_URL +"&pageToken="+page_token
        except KeyError:
            break

        
if __name__ == '__main__':
    main()

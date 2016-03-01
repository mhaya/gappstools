# gappstools

##インストール

1. python環境にhttplib2および[API Client Library for Python](https://developers.google.com/api-client-library/python/start/installation?hl=ja)をインストールする

```
pip install httplib2
pip install --upgrade google-api-python-client
```

2. [Google Developers Console](https://console.developers.google.com)
の認証情報でネイティブ アプリケーションのクライアントIDを作成し，クライアントシークレットをJSON形式でダウンロードする。

3. ダウンロードしたクライアントシークレットをsecret/client_secrets.jsonに保存する

4. スクリプト実行時にオプション --noauth_local_webserver  を付けて実行する

5. 画面に表示されたURLにアクセスし，適切なアカウントからAPIアクセスを許可する

6. 結果が表示されるのを待つ

## getNumberOfUsersInDomain.py

[Admin Settings API](https://developers.google.com/admin-sdk/admin-settings/)を使用して指定ドメインのユーザ数および最大ユーザ数を表示する。

###実行例
```
$ python getNumberOfUsersInDomain.py ex.sheepcloud.org
Your browser has been opened to visit:

    https://accounts.google.com/o/oauth2/auth?scope=https%3A%2F%2Fapps-apis.google.com%2Fa%2Ffeeds%2Fdomain%2F&redirect_uri=http%3A%2F%2Flocalhost%3A8080%2F&response_type=code&client_id={client_id}&access_type=offline

If your browser is on a different machine then exit and re-run this
application with the command-line parameter 

  --noauth_local_webserver

Authentication successful.
number of users in ex.sheepcloud.org
maximum:10
current:2
```

##getAllUsersListInDomain.py

###実行例

```
$ python getAllUsersListInDomain.py ex.sheepcloud.org
id primaryEmail lastLoginTime creationTime agreedToTerms suspended isMailboxSetup
xxxxx xxxx@ex.sheepcloud.org 2016-03-01T02:06:45.000Z 2011-10-13T04:59:40.000Z True False True
xxxxx yyyy@ex.sheepcloud.org 2015-08-20T07:57:54.000Z 2013-03-19T01:50:48.000Z True False True
```

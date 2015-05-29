# gappstools

##準備

1. [API Client Library for Python](https://developers.google.com/api-client-library/python/start/installation?hl=ja)をインストールする。
2. [Google Developers Console](console.developers.google.com)
の認証情報でネイティブ アプリケーションのクライアントIDを作成し、JSONファイルをダウンロードする。


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

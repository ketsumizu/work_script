# これはなに
gmail で特定のアドレスから特定のタイトルを含むメールが来たら何らかのアクションをする python スクリプト

# 必要なモジュール
requests
dotenv

先にインストールしておく
```bash
sudo pip3 install requests
sudo pip3 install python-dotenv
```

# 環境変数
スクリプトと同階層に .env というファイルを作成し下記の形式で記述
※ 先に gmail の設定画面からアプリパスワードを発行しておく
```bash
GMAIL_USERNAME='example@gmail.com'
APP_PASSWORD='hogehogehoge'
```

# 注意点
gmail の仕様で feed は最新の 20 件しか取れないので cron などでうまく回す必要あり

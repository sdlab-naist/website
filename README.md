# ソフトウェア設計学研究室ウェブサイト

## 環境設定

1. 静的サイトジェネレータ[Hugo](https://gohugo.io/)をインストールしてください．
   Hugo v0.64.1で動作確認をしています． 2. 本リポジトリをクローンしてください．
  ```
  git clone --recursive https://github.com/sdlab-naist/website
  ```
3. 開発用サーバを起動します．`localhost:1313`ブラウザで開くと，生成された
  ウェブサイトが表示されます．
  ```
  hugo server
  ```

詳細な設定方法やページの作成方法は，使用しているテーマAcademicの
[ドキュメント](https://sourcethemes.com/academic/docs/)を参照してください．

## ユーザの追加

1. 下記のコマンドを実行し，ユーザのディレクトリを作成してください．
  ```
  $ hugo new --kind authors authors/firstname-lastname
  ```
  `content/authors/firstname-lastname`というディレクトリが生成されます．

2. 生成されたディレクトリ内の`_index.md`を編集し，名前やプロフィール
  などを設定します．下記の項目は必ず設定してください:
  - `name`: 氏名 (姓と名の間には半角空白を1つ空ける)
  - `role`: `教授`や`博士後期課程学生`など
  - `group`: 教員の場合`Staff`，学生の場合`Student`

3. 同ディレクトリ内の`avatar.jpg`を自分の顔写真に置き換えてください．
  アスペクト比は正方形，かつ，サイズは500ピクセル四方程度にしてください．

トップページのメンバー一覧は自動的に更新されます．

## ブログ記事の追加

1. 下記のコマンドを実行し，記事のディレクトリを作成してください．
  ```
  $ hugo new  --kind post post/title-of-your-blog-post
  ```
  `content/post/title-of-your-blog-post`というディレクトリが生成されます．

2. 生成されたディレクトリ内の`index.md`を編集し，記事を執筆します．
  また，下記の項目を必ず設定してください．
  - `title`: 記事のタイトル
  - `authors`: 記事の著者 (ユーザ作成時に指定した，`firstname-lastname`という
      形式)

3. 記事に添付する写真があれば，同ディレクトリに`featued.jpeg/png`というファイ
   ル名で保存してください．自動的にアイキャッチ画像に設定されます．
   複数の写真を添付する場合は，同ディレクトリに写真を保存し，本文からfigure
   ショートコードを使って参照してください．

## 研究テーマの追加

1. 下記のコマンドを実行し，研究テーマのディレクトリを作成してください．
  ```
  $ hugo new  --kind project project/title-of-your-project
  ```
  `content/project/title-of-your-project`というディレクトリが生成されます．

2. 生成されたディレクトリ内の`index.md`を編集し，記事を執筆します．
  また，下記の項目を必ず設定してください．
  - `title`: 研究テーマのタイトル
  - `authors`: 研究テーマの著者 (ユーザ作成時に指定した，`firstname-lastname`という
      形式)

3. 記事に添付する写真があれば，同ディレクトリに`featued.jpeg/png`というファイ
   ル名で保存してください．自動的にアイキャッチ画像に設定されます．
   複数の写真を添付する場合は，同ディレクトリに写真を保存し，本文からfigure
   ショートコードを使って参照してください．

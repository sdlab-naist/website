# ソフトウェア設計学研究室ウェブサイト [![Netlify Status](https://api.netlify.com/api/v1/badges/3fbbab05-cf15-4ac2-854f-f2ac1ed81672/deploy-status)](https://app.netlify.com/sites/sdlab/deploys)

## 環境設定

1. 静的サイトジェネレータ[Hugo](https://gohugo.io/)をインストールしてください．
   extended version (with Sass/SCSS support)が必要です．
   使用するプラットフォームやバージョンによってはデフォルトでextended versionがインストールされないので確認してください．
2. 本リポジトリをクローンしてください．
    ```
    git clone https://github.com/sdlab-naist/website
    ```
3. 開発用サーバを起動します．`localhost:1313`をブラウザで開くと，生成された
  ウェブサイトが表示されます．
    ```
    hugo server
    ```

詳細な設定方法やページの作成方法は，使用しているテーマAcademicの
[ドキュメント](https://sourcethemes.com/academic/docs/)を参照してください．

## 作業フロー
Githubを用いたPullRequest駆動でWebコンテンツを更新しています．編集作業を始める前にかならずBranchを作り，それをGithub上のレポジトリにPushした上で，PullRequestを発行する必要があります．発行したPullRequestは1人以上のレビューを受けないとmasterにマージされません．以下が典型的な作業フローの例です．
1. masterを最新状態に更新してください．
```
git checkout master
git pull 
```

2. 作業用のBranch作成します．  
`name-of-branch`の部分に作業内容を表す適当な名前を指定してください．
```
git checkout -b name-of-branch
```

3. 何らかの編集作業を実施．  
`hugo server`を実行してサーバを起動しているのなら，`localhost:1313`をブラウザで開くことで，編集内容を逐次確認しながら編集できます．

4. コミットしてください．
```
git add .
git commit -m "コメント"
```

5. コミット内容をGithubにPushします．  
`name-of-branch`は先程のBranch名と同一のものを指定してください．
```
git push origin name-of-branch
```

6. Githubにアクセスして，自分が作成したBranchである`name-of-branch`を`master`ブランチへマージを要求するPullRequestを発行してください．レビューが完了しmasterにマージされたら，Webサイト上で公開されます．

7. ローカルのmasterの更新が済めば，作業用のBranchを削除してもいいです．
```
git checkout master
git pull
git branch -d name-of-branch
```

以下では，各コンテンツの追加方法を説明します．

## ユーザの追加

1. 下記のコマンドを実行し，ユーザのディレクトリを作成してください．
    ```
    $ hugo new --kind authors content/ja/authors/firstname-lastname
    ```
    `content/ja/authors/firstname-lastname`というディレクトリが生成されます．

2. 生成されたディレクトリ内の`_index.md`を編集し，名前やプロフィール
  などを設定します．下記の項目は必ず設定してください:
    - `name`: 氏名 (姓と名の間には半角空白を1つ空ける)
    - `role`: `教授`や`博士後期課程学生`など
    - `user_groups`: 教員の場合`Staff`，学生の場合`Student`，卒業生の場合は`Past Student`
    - `weight`: テンプレートには無いですが，`user_groups`の後に追記ください．  
    在学生の場合は入学年月を数字で`202004`のように入力．卒業生の場合は卒業年月を入力．

3. 同ディレクトリ内の`avatar.jpg`を自分の顔写真に置き換えてください．
  アスペクト比は正方形，かつ，サイズは500ピクセル四方程度にしてください．

メンバー一覧は自動的に更新されます．

## ブログ記事の追加

1. 下記のコマンドを実行し，記事のディレクトリを作成してください．
    ```
    $ hugo new  --kind post content/ja/post/title-of-your-blog-post
    ```
    `content/ja/post/title-of-your-blog-post`というディレクトリが生成されます．

2. 生成されたディレクトリ内の`index.md`を編集し，記事を執筆します．
  また，下記の項目を必ず設定してください．
    - `title`: 記事のタイトル
    - `authors`: 記事の著者 (ユーザ作成時に指定した，`firstname-lastname`という
        形式)

3. 記事に添付する写真があれば，同ディレクトリに`featured.jpg/png`というファイ
   ル名で保存してください．自動的にアイキャッチ画像に設定されます．
   複数の写真を添付する場合は，同ディレクトリに写真を保存し，本文からfigure
   ショートコードを使って参照してください．

## 研究テーマの追加

1. 下記のコマンドを実行し，研究テーマのディレクトリを作成してください．
    ```
    $ hugo new  --kind project content/ja/project/title-of-your-project
    ```
    `content/project/title-of-your-project`というディレクトリが生成されます．

2. 生成されたディレクトリ内の`index.md`を編集し，記事を執筆します．
  また，下記の項目を必ず設定してください．
    - `title`: 研究テーマのタイトル
    - `authors`: 研究テーマの著者 (ユーザ作成時に指定した，`firstname-lastname`という
        形式)
    - `tags`: 大分類のタグ("Software Process", "Repository Mining", "Software Analytics", "Cloud", "HPC")から最低一つを選び，必要に応じて適切なtag名を追加指定してください．（例：`tags: ["Cloud", "SDN"]`）

3. 記事に添付する写真があれば，同ディレクトリに`featured.jpg/png`というファイ
   ル名で保存してください．自動的にアイキャッチ画像に設定されます．
   複数の写真を添付する場合は，同ディレクトリに写真を保存し，本文からfigure
   ショートコードを使って参照してください．

## 業績リストの更新

1. NAIST業績管理システムから業績一覧を取得します:
    ```
    $ curl -o scripts/publications.json -X GET "https://api-research.naist.jp/api/search?chair=ソフトウェア設計学&output=json"
    ```
2. 取得した業績一覧から，業績ページのMarkdownファイルを生成します:
    ```
    $ python3 scripts/convert_publications.py scripts/publications.json content/ja/publications.md content/en/publications.md
    ```

## アルバムへの写真の追加

`content/ja/gallery/album`以下に画像ファイルを追加してください．

## 英語コンテンツ

英語コンテンツは，`content/en`以下に日本語と同様の構造で作成してください．
例えば，英語版にユーザを追加する場合，下記のコマンドを実行してください:

```
hugo new --kind authors content/en/authors/firstname-lastname
```

英語コンテンツのみを作成し，日本語コンテンツは英語コンテンツを単に再掲したい場合はシンボリックリンクを作成してください．
例えば，日本語版に英語版で作った研究テーマのコンテンツを追加する場合，下記のコマンドを実行してください:
```
cd content/ja/project/
ln -s ../../en/project/title-of-your-project
```

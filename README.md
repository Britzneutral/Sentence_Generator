プログラムの概要
　文章の続きを自動で生成するアプリである。近年、文章を自動で生成することができる言語処理モデルが次々に公開されている。言語処理モデルはテキストデータを学習データとして機械学習させたものであり、日本語のテキストデータを学習させたモデルもいくつか発表されている。このように日本語に対応した言語処理モデルをもっと気軽に多くの人に体験してもらうために、文章の続きを自動で生成するアプリの開発を試みた。3つの事前学習モデルの中から使いたいモデルを選択し、文章の生成に関わるパラメータを任意の値に設定して、いくつかの文を入力として与えることで、その続きの文章を言語処理モデルが自動生成してくれるものである。

プログラムの特徴
　今回のアプリにおいては、rinna社から提供されている「japanese-gpt2-small」「japanese-gpt2-medium」「japanese-gpt-1b」の3つの事前学習モデルの中から任意のモデルを選択することができるようにした。通常はこれらのモデルを使用するためにモデルのダウンロードや各設定等をプログラムとして書く必要があるが、アプリを開発するにあたってモデルの選択や各パラメータの設定などをボタン操作やスライダー入力で実現しているため、シンプルで直感的な操作が可能となっている。

ソフトの必要環境/インストール方法/設定方法
　Windowsを搭載したPCもしくはgoogle colaboratory上のいずれかでの実行環境を想定している。いずれにせよ、webアプリケーションであるため、インターネットへのアクセスが必要となる。また、アプリの作成にはstreamlitを使用し、各ライブラリ等のインストールが必要となる。

Windowsを搭載したPCで実行する場合
Pythonの3.6以降のバージョンをインストールする必要がある。
次に以下のコマンドでpipコマンドのアップグレードを行う。
python -m pip install --upgrade pip

次に以下のコマンドでstreamlitの最新バージョンをインストールする。
pip install --upgrade streamlit

次に、アプリのファイルが置かれているディレクトリに移動し、以下のコマンドで必要なライブラリのインストールを行う。
pip install -r requirements.txt
※上記のコマンドが上手く動作しない場合は以下のライブラリを個別にpipコマンドでインストールしてください。

ライブラリ名
sentencepiece==0.1.96
transformers==4.12.2
torch==1.10.0

ex)pip install sentencepiece==0.1.96

次にコマンドラインからapp.pyのあるディレクトリ下に移動し、以下のコマンドを実行する。
streamlit run --server.address localhost app.py
コマンドラインに表示されるURLにアクセスすると、アプリを起動することができる。

Colaboratory上で実行する場合
グーグルアカウントへの登録が必要になります。
※既にグーグルアカウントを登録している方は既存のアカウントで実行することが可能です。
Google colaboratoryにアクセスしノートブックを新規作成する。
ランタイムのタブからランタイプのタイプをGPUに変更する。

グーグルドライブをマウントするために以下のコードを実行する。
from google.colab import drive
drive.mount('/content/drive')

各ライブラリをインストールするために以下のコードを実行する。
!pip install sentencepiece==0.1.96 transformers==4.12.2 torch==1.10.0

Streamlitの最新バージョンをインストールする。
!pip install --upgrade streamlit


マウントしたグーグルドライブのcontentフォルダにアプリのapp.pyをアップロードする。

次に先程アップロードしたapp.pyのフォルダに移動するために以下のコードを実行する。
!cd /content

以下のコードを実行し、You can now view your Streamlit app in your browser.
が表示されるまで待つ。
!streamlit run app.py & sleep 3 && npx localtunnel --port 8501

You can now view your Streamlit app in your browser.が表示されたらyour url is に続くURLにアクセスする。

指定されたURLにアクセスすると上部に公開アドレスが記載されたページに遷移する。ページの中央部に位置するClick to Continueをクリックすることでアプリを起動することができる。

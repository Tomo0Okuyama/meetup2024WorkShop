# 第2回開発者コミュニティミートアップ ワークショップフォルダ

このリポジトリには、2024年11月8日開催InterSystems 開発者コミュニティミートアップワークショップ用のガイドやコード例などが含まれています。

ワークショップ開始の前の事前準備については[事前準備について](#事前準備について)をご参照ください。

各フォルダについては以下の通りです。フォルダ内部について詳細はそれぞれのREADME.mdをご参照ください。

フォルダ|含まれる内容
--|--|
[1.Python入門](1.Python/)|Pythonの基本操作を楽しく確認できる内容が含まれています。ワークショップ最初にお試しいただきます。|
[2.Embedded Python で IRIS データにアクセスしよう](/2.EmbeddedPython/)|Embedded Python は、IRIS に標準で備わっている「**Python コードで IRIS データにアクセスする**」ための製品機能です。このワークショップでは、Embedded Python で IRIS データやメソッドにアクセスする具体的なコードを体験いただけます。|
[3-a.WSGI-Flask](/3-a.WSGI-Flask/)|WSGIに準拠したWebフレームワークを利用して、簡単なWebアプリケーションの作成を体験します。（WSGIについては、開発者向けウェビナー[Embedded Pythonの新機能～2024.1～](https://www.youtube.com/watch?list=PLzSN_5VbNaxA8mOezO6Vcm126GXw_89oN&v=WrttoeW34Rw&feature=youtu.be)でもご紹介しています）|
[3-b.NiceGUI SQLAlchemy を使ってアプリケーションをつくってみよう](/3-b.sqlalchemy/)|[NiceGUI](https://nicegui.io/)と、[Open Exchange](https://openexchange.intersystems.com/)で公開されている[sqlalchemy-iris](https://openexchange.intersystems.com/package/sqlalchemy-iris)を使用してPythonプログラムでIRISデータベースにアクセスするWebアプリケーションを作成します。|
[3-c.機械学習で手書き数字の識別に挑戦](/3-c.ML101/)|MNISTが提供している手書き数字の画像データセットを使用し、手書きの数字を識別する分類器の作成を通して、機械学習の基本をハンズオン形式で学びます。|

## 事前準備について

ご持参いただくパソコンへの事前準備内容は以下の通りです。

- [(1) インストール](#1-インストール)

    ※お申し込み時のメールに記載していた内容です。

- [(2) 資料ダウンロード](#2-資料ダウンロード)

- [(3) pythonライブラリのimport確認](#3-pythonライブラリのimport確認)

### (1) インストール

ご持参いただくパソコンに以下インストールをお願いします。

- IRISコミュニティエディション

- VSCode

- ワークショップで使用するpythonライブラリ

インストール方法詳細は、[第2回 開発者コミュニティ・ミートアップ Python ワークショップの事前準備について](https://jp.community.intersystems.com/node/574686)をご参照ください。

**これからIRISコミュニティエディションをダウンロードされる方は、バージョン2024.2がダウンロードされます。2024.2のIRISインストールについては、[上記記事の下にあるコメント3つ目](https://jp.community.intersystems.com/node/574686#comment-273661)にインストール内容の記載がありますのでご参照ください。**

### (2) 資料ダウンロード

ご持参いただくパソコンに git がインストールされている場合は、git cloneしてください。

```
git clone https://github.com/Intersystems-jp/meetup2024WorkShop.git
```

git がインストールされていない方は、**Codeボタンクリック→「Download ZIP」クリック**でダウンロードできます。

![](/DownloadZip.png)

ワークショップ当日、ダウンロードファイルの中身をVSCodeから編集したいので、アクセスしやすい場所にZip展開後のフォルダを配置してください。

**ご参考：VSCodeでワークスペースを開く方法：VSCodeのメニュー：File→OpenFolderから、ダウンロードして展開したフォルダ（meetup2024WorkShop）を選択します。**
![](/OpenWorkspace.png)


### (3) pythonライブラリのimport確認

IRISコミュニティエディションのダウンロード時期により、ご利用いただくIRISのバージョンが異なるため、確認方法が2通りあります。

**インストールキットのファイル名先頭が IRIS-2024.1　から始まる場合は、2024.1、IRIS-2024.2 から始まる場合は、2024.2をご利用いただいています。**

事前準備でインストールされた以下ライブラリのインポートが正しく行えるかご確認ください。

- flask
- sqlalchemy-iris
- nicegui

バージョン別確認方法は以下の通りです。


#### バージョン2024.1の場合

コマンドプロンプトを開き、以下実行します。

実行するコマンドは以下の通りです。
```
from flask import Flask,render_template
from sqlalchemy import create_engine
from nicegui import ui
```

IRISインストール時に一緒にインストールされたpython.exeを使用します。

python.exeは以下にインストールされています。

＜IRISインストールディレクトリ＞\lib\python\

上記ディレクトリは環境変数PATHに登録がありませんので、ご登録いただくか、確認時ディレクトリを移動した状態でお試しください。

例では、c:\intersystems\iris にIRISをインストールした場合の表示です。

実行例全体は以下の通りです。

```
c:\>cd InterSystems\IRIS\lib\python

c:\InterSystems\IRIS\lib\python>python
Python 3.9.19 (main, Oct  3 2024, 15:08:04) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> from flask import Flask,render_template
>>> from sqlalchemy import create_engine
>>> from nicegui import ui
>>> quit()

c:\InterSystems\IRIS\lib\python>
```


#### バージョン2024.2の場合

コマンドプロンプトを開き、以下実行します。

実行するコマンドは以下の通りです。
```
from flask import Flask,render_template
from sqlalchemy import create_engine
from nicegui import ui
```

実行例全体は以下の通りです。
```
>python
Python 3.12.7 (tags/v3.12.7:0b05ead, Oct  1 2024, 03:06:41) [MSC v.1941 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> from flask import Flask,render_template
>>> from sqlalchemy import create_engine
>>> from nicegui import ui
>>> quit()

>
```

python.exeのあるディレクトリを環境変数PATHに設定していない場合は、pythonインストールディレクトリを調査し、設定を行ってください。

コマンドプロンプトを開き、以下実行してインストールディレクトリを調査します。

```
>where python
C:\Users\Administrator\AppData\Local\Programs\Python\Python312\python.exe
```

例のディレクトリの場合、以下2つを環境変数PATHに追加します。（~/Scripts/ は、pip用に必要です。）
- pythonインストールディレクトリ/Sciripts/

    例）C:\Users\Administrator\AppData\Local\Programs\Python\Python312\Scripts\


- pythonインストールディレクトリ

    例）C:\Users\Administrator\AppData\Local\Programs\Python\Python312\


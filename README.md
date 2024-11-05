# 第2回開発者コミュニティミートアップ ワークショップフォルダ

このリポジトリには、2024年11月8日開催InterSystems 開発者コミュニティミートアップワークショップ用のガイドやコード例などが含まれています。

ワークショップ開始の前の事前準備については[事前準備について](#事前準備について)をご参照ください。

各フォルダについては以下の通りです。フォルダ内部について詳細はそれぞれのREADME.mdをご参照ください。

フォルダ|含まれる内容
--|--|
[1.Python入門](1.Python/)|Pythonの基本操作を楽しく確認できる内容が含まれています。ワークショップ最初にお試しいただきます。|
[2.Embedded Python で IRIS データにアクセスしよう](/2.EmbeddedPython/)|Embedded Python は、IRIS に標準で備わっている「**Python コードで IRIS データにアクセスする**」ための製品機能です。このワークショップでは、Embedded Python で IRIS データやメソッドにアクセスする具体的なコードを体験いただけます。|
[3-a.WSGI-Flask](/3-a.WSGI-Flask/)|WSGIに準拠したWebフレームワーク・Flaskを利用して、シンプルなショッピングカート機能を持つWebアプリケーション作成を体験します。<br>（WSGIについては、開発者向けウェビナー[Embedded Pythonの新機能～2024.1～](https://www.youtube.com/watch?list=PLzSN_5VbNaxA8mOezO6Vcm126GXw_89oN&v=WrttoeW34Rw&feature=youtu.be)でもご紹介しています）|
[3-b.NiceGUI SQLAlchemy を使ってアプリケーションをつくってみよう](/3-b.sqlalchemy/)|[NiceGUI](https://nicegui.io/)と、[Open Exchange](https://openexchange.intersystems.com/)で公開されている[sqlalchemy-iris](https://openexchange.intersystems.com/package/sqlalchemy-iris)を使用してPythonプログラムでIRISデータベースにアクセスするWebアプリケーションを作成します。|
[3-c.機械学習で手書き数字の識別に挑戦](/3-c.ML101/)|MNISTが提供している手書き数字の画像データセットを使用し、手書きの数字を識別する分類器の作成を通して、機械学習の基本をハンズオン形式で学びます。<br>このワークショップでは、[Google Colaboratory](https://colab.research.google.com/?hl=ja)を使用するため、Googleアカウントが必要です。|


以下、参考情報です。

- [A-1: VSCodeでワークスペースを開く方法](#a-1-vscodeでワークスペースを開く方法)
- [A-2: READMEのプレビュー表示](#a-2-readmeのプレビュー表示)
- [A-3: VSCode内でPowershellを開く方法と環境変数設定方法](#a-3-vscode内でpowershellを開く方法と環境変数設定方法)
- [A-4: VSCodeからIRISに接続する方法](#a-4-vscodeからirisに接続する方法)
- [A-5: VSCodeから管理ポータルを開く方法](#a-5-vscodeから管理ポータルを開く方法)

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

git をインストールしていないパソコンでは、**Codeボタンクリック→「Download ZIP」クリック** で一式をダウンロードできます。

![](/images/DownloadZip.png)

ワークショップ当日、ダウンロードファイルの中身をVSCodeから編集したいので、アクセスしやすい場所にZip展開後のフォルダ（meetup2024WorkShop）を配置してください。


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


## 参考情報

### A-1: VSCodeでワークスペースを開く方法

VSCodeでワークスペースを開く方法は、以下の通りです。
VSCodeのメニュー File→OpenFolderから、ダウンロードして展開したフォルダ(meetup2024WorkShop)を選択し開きます。
![](/images/OpenWorkspace.png)


### A-2: READMEのプレビュー表示

VSCodeでワークスペースを開いたら、各ワークショップで使用するREADME.mdを開きプレビュー表示に切り替えます。

README.mdは各ワークショップ用フォルダ以下にもあります。すべて同じ方法でプレビュー表示をご覧いただけます。

- 1 VSCodeのExplorerアイコンをクリックし、開きたいREADME.mdファイルをクリックします。

- 2 プレビュー表示にする方法は2種類あります。

    その1：画面右上のアイコンを利用する方法
    ![](/images/PreviewOpen1.png)

    その2：README.mdファイルを右クリックして開く方法
    ![](/images/PreviewOpen2.png)

【ご参考】README.mdの内容はブラウザでも参照できます（Gitリポジトリにアクセスすると参照できます）

- [ワークショップ用フォルダトップにあるREADME.md](https://github.com/Intersystems-jp/meetup2024WorkShop/blob/main/README.md)

- [Python入門](https://github.com/Intersystems-jp/meetup2024WorkShop/blob/main/1.Python/README.md)

- [Embedded Python で IRIS データにアクセスしよう](https://github.com/Intersystems-jp/meetup2024WorkShop/blob/main/2.EmbeddedPython/README.md)

- [WSGI-FLASK](https://github.com/Intersystems-jp/meetup2024WorkShop/blob/main/3-a.WSGI-Flask/README.md)

- [NiceGUI SQLAlchemy を使ってアプリケーションをつくってみよう](https://github.com/Intersystems-jp/meetup2024WorkShop/blob/main/3-b.sqlalchemy/README.md)

- [機械学習で手書き数字の識別に挑戦](https://github.com/Intersystems-jp/meetup2024WorkShop/blob/main/3-c.ML101/README.md)

GitリポジトリのページでREADMEを参照する際、Outline表示を利用するとページ内ジャンプなどが簡単に行えます。
![](/images/README-Git-Outline.png)


### A-3: VSCode内でPowershellを開く方法と環境変数設定方法

VSCodeメニューバーから **Terminal→New Terminal** をクリックすると画面下側にPowershellが起動します。

![](/images/PowerShell.png)

画面例では、環境変数PATHにIRIS2024.1インストール時に一緒にインストールされるPythonへのパスの設定を行っています。

IRISインストール時デフォルト設定でインストールを行うと、以下ディレクトリにpythonがインストールされています。

`c:\InterSystems\IRIS\lib\python`

IRIS2024.1をお使いの場合は以下のコマンドを実行することで、開いたPowerShell内でpythonコマンドの操作が簡単に行えます。

実行コマンド
```
$ENV:PATH+=";C:\InterSystems\IRIS\lib\python"
```

コマンド実行全体（最初に設定前のPATHを確認しています）
```
PS C:\meetup2024WorkShop> $ENV:PATH
C:\Program Files\Eclipse Adoptium\jdk-8.0.422.5-hotspot\bin;C:\Windows\system32;C:\Windows;C:\Windows\System32\Wbem;
    《省略》
PS C:\meetup2024WorkShop> $ENV:PATH+=";C:\InterSystems\IRIS\lib\python"
PS C:\meetup2024WorkShop> python
Python 3.9.19 (main, Oct  3 2024, 15:08:04) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> import flask
>>>
``` 

IRIS2024.2をインストールされている方はOSにPython3.12.7をインストールいただいています。インストール時にPATHへの追加を忘れた方も、同様にPythonインストールディレクトリを調査した後、上記コマンドを実行してください。

Pythonインストールディレクトリ例：`C:\Users\{ユーザ名}\AppData\Local\Programs\Python\Python312`

### A-4: VSCodeからIRISに接続する方法

ワークショップの中でVSCodeからIRISへ接続する際、以下ファイルの接続設定をお使いのIRISに合わせて変更してください。

[.vscode/settings.json](.vscode/settings.json)

ダウンロード直後の接続情報は以下の通りです。
```
{
	"intersystems.servers": {
		"meetup": {
			"webServer": {
				"host": "127.0.0.1",
				"port": 52773,
				"pathPrefix": "/iris",
				"scheme": "http",
			},
			"username": "_system"
		}
	},
	"objectscript.conn": {
		"server": "meetup",
		"ns": "USER",
		"active": true
	}
}
```

"intersystems.server"以下の設定を環境に合わせてご変更ください。

- A：ポート番号80番以外（52773など）を使用してIRISにアクセスする環境の場合

    以下行を削除してください。
    ```
    "pathPrefix": "/iris",
    ```

- B：ポート番号52773番以外を使用してIRISにアクセスしている場合

    "port"を使用しているポート番号に合わせて修正します。

    80番の例
    ```
    "port": 80,
    ```

    52774番の例
    ```
    "port": 52774,
    ```
- C：IRISインストール前にIISを有効化していた場合

    IRISをインストールする前にIISを有効化しているとインストール時 **/インスタンス名**の仮想パスを設定しています。

    例は、インストール時に指定するインスタンス名（構成名）を**irisxx**とした場合の設定です。最初に(/)スラッシュが必要になりますのでご注意ください。

    ```
    "pathPrefix": "/irisxx",
    ```


接続情報の修正が終わったら、VSCodeの左バーにあるエクステンションアイコンから「InterSystems」のロゴをクリックし、接続します。
詳細は図をご覧ください。
![](/images/VSCode-IRISsettings.png)

接続できると、画面左下に「meetup[USER]」と表示されます。

![](/images/meetupUSERconnected.png)

以上で接続完了です。

### A-5: VSCodeから管理ポータルを開く方法

この操作の前に、IRISに接続が完了している必要があります。まだの場合は、[A-4: VSCodeからIRISに接続する方法](#a-4-vscodeからirisに接続する方法)をご参照下さい。

VSCodeの左下（青いバーのエリアの左付近）の **metup[USER]** をクリックすると、VSCodeの画面上・中央付近にメニューが表示されます。

![](/images/OpenManagementPortal.png)


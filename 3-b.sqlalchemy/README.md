
# NiceGUI SQLAlchemy を使ってアプリケーションをつくってみよう <!-- omit in toc -->

このワークショップでは[NiceGUI](https://nicegui.io/)ならびに[SQLAlchemy](https://www.sqlalchemy.org/)を使用し、
PythonプログラムでIRISデータベースにアクセスするWebアプリケーションを作成します。

# 目次 <!-- omit in toc -->

- [1. NiceGUI とは](#1-nicegui-とは)
  - [1.1. NiceGUIの特長](#11-niceguiの特長)
- [2. SQLAlchemy とは](#2-sqlalchemy-とは)
- [3. Hello world](#3-hello-world)
- [4. Controlを試してみる](#4-controlを試してみる)
  - [4.1. Button](#41-button)
  - [4.2. Text Input](#42-text-input)
  - [4.3. Dropdown button](#43-dropdown-button)
  - [4.4. date](#44-date)
  - [4.5. データ参照](#45-データ参照)
- [5. SQLAlchemy](#5-sqlalchemy)
  - [5.1. IRISでのクラス(テーブル)作成](#51-irisでのクラステーブル作成)
    - [5.1.1. Customer.cls (顧客テーブル)](#511-customercls-顧客テーブル)
    - [5.1.2. Product.cls (製品情報)](#512-productcls-製品情報)
    - [5.1.3. Transaction.cls (取引テーブル)](#513-transactioncls-取引テーブル)
    - [5.1.4. TransactionItem.cls (取引明細テーブル)](#514-transactionitemcls-取引明細テーブル)
  - [5.2. 接続設定](#52-接続設定)
  - [5.3. データモデルの作成](#53-データモデルの作成)
    - [5.3.1. 顧客情報クラスの追加](#531-顧客情報クラスの追加)
    - [5.3.2. 製品情報クラスの追加](#532-製品情報クラスの追加)
    - [5.3.3. 取引クラス、取引明細クラスの追加](#533-取引クラス取引明細クラスの追加)
      - [5.3.3.1. TransactionItem クラスの product プロパティ](#5331-transactionitem-クラスの-product-プロパティ)
      - [5.3.3.2. Transactionsクラスのcustomerプロパティ](#5332-transactionsクラスのcustomerプロパティ)
- [6. データ操作](#6-データ操作)
  - [6.1. 顧客情報の登録](#61-顧客情報の登録)
  - [6.2. 取引データの登録](#62-取引データの登録)
  - [6.3. データの削除](#63-データの削除)
- [7. 顧客情報メンテナンスの作成](#7-顧客情報メンテナンスの作成)
  - [7.1. 顧客一覧画面の作成](#71-顧客一覧画面の作成)
  - [7.2. 顧客編集ダイアログボックスの作成](#72-顧客編集ダイアログボックスの作成)
  - [7.3. データ保存機能の作成](#73-データ保存機能の作成)
  - [7.4. データ削除機能の作成](#74-データ削除機能の作成)
  - [7.5. データ作成機能の作成](#75-データ作成機能の作成)
  - [7.6. グリッドの更新](#76-グリッドの更新)
  - [7.7. 入力に便利なコントロールとバインド設定](#77-入力に便利なコントロールとバインド設定)
    - [7.7.1. 生年月日の入力](#771-生年月日の入力)
    - [7.7.2. 性別の入力](#772-性別の入力)
    - [7.7.3. 郵便番号検索機能の追加](#773-郵便番号検索機能の追加)
- [8. 製品情報メンテナンスの作成](#8-製品情報メンテナンスの作成)
  - [8.1. メインページの作成](#81-メインページの作成)
  - [8.2. 顧客情報メンテ、製品情報メンテの改造](#82-顧客情報メンテ製品情報メンテの改造)

## 1. NiceGUI とは

[NiceGUI](https://nicegui.io/) は、Pythonを使用し、Webインターフェイスを簡単に作成するためのツールです。
[Svelte](https://svelte.jp/) や WebSocket などの一般的な Web 開発ライブラリを使用して、スムーズで迅速なユーザー エクスペリエンスを提供します。
NiceGUI の最も優れた点は、シンプルで使いやすいことです。
NiceGUI を使用すると、開発者は HTML、CSS、または JavaScript コードを記述することなく、Python のみを使用して複雑な Web インターフェイスを作成できます。

### 1.1. NiceGUIの特長

NiceGUI にはいくつかの便利な機能があります

- **使いやすい**

  NiceGUI はシンプルに設計されているため、開発者は数行の Python コードで Web インターフェイスを作成できます。そのため、初心者にも経験豊富な開発者にも最適です。
- **リアルタイムのインタラクティブ性**

  NiceGUI はリアルタイムのインタラクティブ性をサポートしており、インターフェイスに加えられた変更は Web ブラウザーに即座に表示されます。そのため、動的な Web アプリケーションの作成に最適です。
- **カスタマイズ可能**

  NiceGUI は使い方が簡単であるにもかかわらず、カスタマイズが可能です。開発者は標準の CSS を使用して、インターフェイスの外観と操作性を変更できます。
- **インテグレーション**

  NiceGUI は、NumPy、Pandas、Flask などの他の Python ツールやフレームワークと併用できます。これにより、開発者は Web アプリケーションを作成するときにこれらのツールを活用できます。
- **簡単な導入**

  NiceGUI は、アプリケーションを導入するためのシンプルなコマンドライン インターフェイスを提供します。開発者は、コマンド 1 つだけで、アプリケーションをローカル サーバーまたはクラウドベースのプラットフォームに導入できます。

## 2. SQLAlchemy とは

Pythonで最もメジャーかつデファクトスタンダード的な存在となるSQL操作用ライブラリです。
OracleやMySQLなど様々なDBに対応しており、[sqlalchemy-iris](https://openexchange.intersystems.com/package/sqlalchemy-iris)
を導入すると、PythonからIRISにもアクセスできます。

## 3. Hello world

まずはHello worldを表示する画面を作成します。
test.py を作成し、以下の内容を入力します。

```Python
from nicegui import ui
ui.label('Hello NiceGUI!')
ui.run()
```

vscode のウインドウの下側にある、「ターミナル」をクリックすると、PowerShellが表示されます。
ここで以下のようにpythonを起動しtest.pyを実行しますと、表示するURLが表示され、webブラウザが起動し、webアプリケーションが実行できます。

```PowerShell
> python test.py
NiceGUI ready to go on http://localhost:8080, ...
```

ここで、Ctrl-C を入力すると、pythonが終了し、PowerShellに戻ります。

## 4. Controlを試してみる

ここでは、NiceGUIで定義されているコントロールを試してゆきます。

### 4.1. Button

ボタンのコントロールです。クリックすると処理を実行できます。
適当な.pyファイルを作成し、以下の内容を入力します。
この例ではクリックすると画面の下に「クリックしましたね！」と表示されます。

```Python
from nicegui import ui
ui.button('クリックしてください', on_click=lambda: ui.notify('クリックしましたね！'))
ui.run()
```

### 4.2. Text Input

文字列を入力するコントロールです。
以下のプログラムを実行し文字列を入力してみてください。
入力された文字は入力欄の下に表示されます。
20文字以上になると「入力文字列が長すぎます」と表示され、エラーとなります。

```Python
from nicegui import ui
ui.input('姓', placeholder='姓を入力してください',
    on_change=lambda e: result.set_text('入力値:' + e.value),
    validation={'入力文字列が長すぎます': lambda value: len(value) < 20}).props('size=80')
result = ui.label()
ui.run()
```

*label* 入力欄の名称
*placeholder* 入力時に背景として書かれる文字列
*props* 文字列入力欄の属性。size=80 で80キャラクター分の幅となる

### 4.3. Dropdown button

入力に選択肢を設けるためのコントロール。
以下のプログラムを実行し、選択するごとに通知が表示されることを確認します。

```Python
from nicegui import ui
with ui.dropdown_button(label='性別','選択してください', auto_close=True):
    ui.item('男性', on_click=lambda: ui.notify('男性が選択されました'))
    ui.item('女性', on_click=lambda: ui.notify('女性が選択されました'))
ui.run()
```

選択した際にボタンの名称を変更する場合

```Python
from nicegui import ui

dropdown = ui.dropdown_button('選択してください', auto_close=True)

#コールバック処理
def action(item):
    ui.notify(item + 'が選択されました')
    dropdown.text = item

with dropdown:
    ui.item('男性', on_click=lambda: action('男性'))
    ui.item('女性', on_click=lambda: action('女性'))
ui.run()
```

### 4.4. date

日付入力を行うコントロールです。

```Python
from nicegui import ui

ui.date(on_change=lambda e: result.set_text(e.value))
result = ui.label()

ui.run()
```

以下のように、入力フォームとメニューを組み合わせて、誕生日入力欄の右のアイコンをクリックすると日付入力コントロールを表示させることもできます。

```Python
from nicegui import ui

with ui.input('誕生日') as date:
    with ui.menu().props('no-parent-event') as menu:
        with ui.date().bind_value(date):
            with ui.row().classes('justify-end'):
                ui.button('閉じる', on_click=menu.close).props('flat')
    with date.add_slot('append'):
        ui.icon('edit_calendar').on('click', menu.open).classes('cursor-pointer')

ui.run()
```

余談になりますが、ui.row()やui.icon()等のコントロールの後に.classes()がありますが、この括弧内に指定するCSSクラスとして
[tailwindcss](https://tailwindcss.com/)を使用していますので、実際に使用するクラスを調べる場合は[こちらのページ](https://tailwindcss.com/)をご参照ください。

### 4.5. データ参照

郵便番号検索APIにアクセスし、得られた住所を住所欄に記入しています。
処理は以下のようにrun.io_bound()メソッドを使用しています。
郵便番号検索APIは以下のサービスを使用しています。
https://zipcloud.ibsnet.co.jp/doc/api

```Python
from nicegui import run, ui
import requests
import json

zipcode = ui.label('郵便番号')
ui.button('検索', on_click= lambda: invoke_zipcode(zipcode.value))
async def invoke_zipcode(zipcode):
    URL = 'https://zipcloud.ibsnet.co.jp/api/search?zipcode='+zipcode
    response = await run.io_bound(requests.get, URL, timeout=10)
    if response.status_code == 200:
        result = json.loads(response.content.decode('utf-8'))
        address = result["results"][0]
        address_input.value = address["address1"] + " " + address["address2"] +" " +  address["address3"]
    else:
        ui.notify(f'郵便番号検索時にエラーが発生しました StatusCode={response.status_code})',timeout=0,close_button="OK")
run()
```

## 5. SQLAlchemy

ここからはSQLAlchemyを使用してデータモデルを設定してゆきます。
まずは SQLAlchemyのライブラリをインストールします。

```PowerShell
pip install sqlalchemy-iris
```

### 5.1. IRISでのクラス(テーブル)作成

今回使用する以下のクラスを作成します。これらのクラスは src\User フォルダに作成します。

#### 5.1.1. Customer.cls (顧客テーブル)

src\User フォルダに顧客テーブル( Customer.cls ファイル ) を作成します。内容は以下の通りです。%Persistentクラスを継承しておりますが、このクラスを継承すると、各プロパティの情報をデータベースに保管することができます。

```ObjectScript
/// 顧客テーブル
Class User.Customer Extends %Persistent
{

/// 顧客ID
Property CustomerId As %String;

/// 氏名姓
Property LastName As %String;

/// 氏名名
Property FirstName As %String;

/// カナ性
Property LastNameKana As %String;

/// カナ名
Property FirstNameKana As %String;

/// 誕生日 
Property DOB As %Date;

/// 性別
Property Gender As %String;

/// 郵便番号
Property ZipCode As %String;

/// 住所
Property Address As %String(MAXLEN = 1000);

/// 電話番号
Property Phone As %String;

Index CustIdIdx On CustomerId [ IdKey, Unique ];

}
```

このクラスをコンパイルしますと以下のテーブルが作成されます。

テーブル名: Customer

|日本語名|フィールド名|データ型|
|-----|-----|----|
|顧客ID|CustomerId|文字列|
|姓|LastName|文字列|
|名|FirstName|文字列|
|カナ姓|LastNameKana|文字列|
|カナ名|FirstNameKana|文字列|
|誕生日|DOB|日付|
|性別|Gender|文字列|
|郵便番号|ZipCode|文字列|
|住所|Address|文字列|
|電話番号|Phone|文字列|

#### 5.1.2. Product.cls (製品情報)

顧客情報と同じフォルダに製品情報テーブル( Product.cls ファイル ) を作成します。内容は以下の通りです。

```ObjectScript
/// 製品テーブル
Class User.Product Extends %Persistent
{

/// 製品番号
Property ProductCode As %String;

/// 製品名
Property ProductName As %String;

/// 価格
Property Price As %Integer;

Index ProdCode On ProductCode [ IdKey, Unique ];

}
```

このクラスをコンパイルしますと以下のテーブルが作成されます。

テーブル名: Product

|日本語名|フィールド名|データ型|
|-----|-----|----|
|製品番号|ProductCode|文字列|
|製品名|ProductName|文字列|
|価格|Price|Integer|

#### 5.1.3. Transaction.cls (取引テーブル)

顧客情報と同じフォルダに取引テーブル( Transaction.cls ファイル ) を作成します。このクラスはTransactionItemクラスと親子関係を持っています。内容は以下の通りです。

```ObjectScript
/// 取引テーブル
Class User.Transactions Extends %Persistent
{

/// 取引時刻
Property TransactionDateTime As %PosixTime;

/// 顧客
Property Customer As Customer;

/// 合計金額
Property Total As %Numeric;

/// 取引明細
Relationship Items As TransactionItem [ Cardinality = children, Inverse = Transactions ];

}
```

このクラスをコンパイルしますと以下のテーブルが作成されます。

テーブル名: Transaction

|日本語名|フィールド名|データ型|
|-----|-----|----|
|ID|ID|数字|
|取引時刻|TransactionDateTime|Posix時刻|
|顧客|Customer|Customer参照|
|合計金額|Total|数字|

#### 5.1.4. TransactionItem.cls (取引明細テーブル)

顧客情報と同じフォルダに取引明細テーブル( TransactionItem.cls ファイル ) を作成します。内容は以下の通りです。このクラスはTransactionクラスと親子関係を持っています。

```ObjectScript
/// 取引明細テーブル
Class User.TransactionItem Extends %Persistent
{

/// 製品
Property Product As Product;

/// 単価
Property UnitPrice As %Numeric;

/// 個数
Property Quantity As %Numeric;

/// 取引
Relationship Transactions As Transactions [ Cardinality = parent, Inverse = Items ];

}
```

このクラスをコンパイルしますと以下のテーブルが作成されます。

テーブル名: TransactionItem

|日本語名|フィールド名|データ型|
|-----|-----|----|
|製品|Product|Product参照|
|単価|UnitPrice|数値|
|個数|Quantity|数値|
|取引|Transactions|Transactions参照|

### 5.2. 接続設定

まずは、setting.pyに接続設定を記述し、IRISへの接続を行います。

```Python
from sqlalchemy import *
from sqlalchemy.orm import *
from sqlalchemy.ext.declarative import declarative_base

# 接続先DBの設定
DATABASE = 'iris://_system:SYS@localhost:51773/USER'

# Engine の作成
Engine = create_engine(
  DATABASE,
  echo=False
)

# Sessionの作成
session = scoped_session(
  # ORM実行時の設定
  sessionmaker(
    autocommit = False,
    autoflush = False,
    bind = Engine
  )
)

# 基底クラスの設定
Base = declarative_base()
Base.query = session.query_property()
```

### 5.3. データモデルの作成

データモデルはmodel.pyに記述します。
まずはimportするクラスを記述します。

```Python
from sqlalchemy import Column, Integer, String, Date, DateTime,ForeignKey
from sqlalchemy.orm import relationship

from setting import Base
import datetime
```

#### 5.3.1. 顧客情報クラスの追加

IRISの顧客テーブルへの入出力を行う顧客情報(Customer) モデルを作成します。

```Python
from sqlalchemy import Column, Integer, String, Date, DateTime,ForeignKey
from sqlalchemy.orm import relationship

from setting import Base
import datetime

# 顧客情報
class Customer(Base):
    __tablename__ = 'Customer'
    __table_args__ = {
        'comment': '顧客情報'
    }
    customerId = Column('CustomerId', Integer, primary_key=True, index=True, autoincrement= False)
    firstName = Column('FirstName', String)
    lastName = Column('LastName', String)
    firstNameKana = Column('FirstNameKana', String)
    lastNameKana = Column('LastNameKana', String)
    dob = Column('DOB',Date)
    gender = Column('Gender',String)
```

\_\_tablename\_\_ にはテーブル名を指定します。今回、IRISのテーブル名はCustomerですので、以下のように指定しています。

```Python
__tablename__ = "Customer"
```

customerId,firstName等のプロパティにはColumn()クラスで、第１パラメータにカラム名、第２パラメータにデータ型を指定しています。テーブルのプライマリキーのプロパティには以下の指定を追加しています。また、customerId はユーザが指定しますので、autoincrement は False とします。

```Python
primary_key=True, index=True, autoincrement= False
```

#### 5.3.2. 製品情報クラスの追加

顧客情報の後ろに、顧客情報と同様にIRISの製品テーブルへの入出力を行う製品情報(Product) モデルを作成します。

```Python
from sqlalchemy import Column, Integer, String, Date, DateTime,ForeignKey

      :

# 顧客情報

      :
      :  (中略)
      :

# 製品情報
class Product(Base):
    __tablename__ = 'Product'
    __table_args__ = {
        'comment': '製品情報'
    }
    productCode = Column('ProductCode', String, primary_key=True, index=True)
    productName = Column('ProductName', String)
    price = Column('Price', Integer)
```

プライマリキーは ProductCode となっていますが、データ型がStringとなっているため、autoincrementを指定しなくても自動的にカウンタ値が代入されることはありません。

#### 5.3.3. 取引クラス、取引明細クラスの追加

製品情報の後に、親子関係になっている取引明細クラス( TransactionItem )、取引クラス( Transactions )を追加します。

```Python
# 取引明細データ
class TransactionItem(Base):
    __tablename__ = 'TransactionItem'
    transaction_id = Column('Transactions',Integer, ForeignKey("Transactions.ID"), primary_key=True, autoincrement=False)
    id = Column('childsub', Integer, primary_key=True, autoincrement=True)
    transaction = relationship('Transactions', foreign_keys=[transaction_id], back_populates="items")

    product_id = Column('Product', String, ForeignKey('Product.ProductCode'))
    product = relationship('Product',foreign_keys=[product_id])

    unitPrice = Column('UnitPrice', String)
    quantity = Column('Quantity', String)

# 取引データ
class Transactions(Base):
    __tablename__ = 'Transactions'
    id = Column('ID', Integer, primary_key=True, index=True)
    items = relationship('TransactionItem', back_populates="transaction", cascade="all,delete")

    customer_id = Column('Customer', String, ForeignKey('Customer.CustomerId'))
    customer = relationship('Customer',foreign_keys=[customer_id])

    dateTime = Column('TransactionDateTime', DateTime, default=datetime.datetime.now())
    total = Column('Total',Integer)
```

Transactions クラスはIDカラムで自動採番としています。そのため、id プロパティ
が　primary_key = True となります。id プロパティのデータ型はIntegerですので、指定していなくても autoincrement=True となっています。

```Python
    id = Column('ID', Integer, primary_key=True, index=True)
```

TransactionItemとのリレーションシップとなる items は以下のように指定します。
TransactionItemクラスのtransactionプロパティがTransactionsへの参照となりますので、
back_populates に transaction プロパティを指定しています。
また、Transactions が削除されると、関連する TransactionItem のオブジェクトは削除されますので、cascade="all,delete"を指定しています。

```Python
    items = relationship('TransactionItem', back_populates="transaction", cascade="all,delete")
```

一方 TransactionItem クラス側では親子関係から、プライマリキーは、Transactions クラスの ID パラメータ、childsub　フィールドの値となりますので、それぞれprimary_key = True
としています。
また、Transactionsクラスのオブジェクトにアクセスできるよう、transaction プロパティにrelationshipを指定しています。

```Python
    transaction_id = Column('Transactions',Integer, ForeignKey("Transactions.ID"), primary_key=True, autoincrement=False)
    id = Column('childsub', Integer, primary_key=True, autoincrement=True)
    transaction = relationship('Transactions', foreign_keys=[transaction_id], back_populates="items")
```

product や customer はそれぞれ製品情報クラスや顧客情報クラスのオブジェクトを参照していますので、これらにも、ForeignKeyを指定したidプロパティと、オブジェクトのプロパティにrelationshipを指定しています。

##### 5.3.3.1. TransactionItem クラスの product プロパティ

```Python
    product_id = Column('Product', String, ForeignKey('Product.ProductCode'))
    product = relationship('Product',foreign_keys=[product_id])
```

##### 5.3.3.2. Transactionsクラスのcustomerプロパティ

```Python
    customer_id = Column('Customer', String, ForeignKey('Customer.CustomerId'))
    customer = relationship('Customer',foreign_keys=[customer_id])
```

その他、Transactions クラスのdateTime プロパティは、IRISでのデータ型は%POSIXTIMEとなっており、内部的にはPosixのシリアル値で保存されています。しかし、ODBCでアクセスした場合はTimeStamp形式でデータを渡しますので、SQLAlchemy では DateTimeを指定しています。
また、以下のようにdefaultパラメータを指定することで、登録時刻が保存されます。

```Python
    dateTime = Column('TransactionDateTime', DateTime, default=datetime.datetime.now())
```

## 6. データ操作

Pythonを起動し、コマンドラインからデータを登録します。
ターミナルよりpythonを起動します。

```PowerShell
> python
Python 3.12.3 (tags/v3.12.3:...
Type "help", "copyright", "credits" or "license" for more information.
>>>
```

### 6.1. 顧客情報の登録

先ほど作成したsetting.py,model.pyをインポートします。

```Python
>>> from setting import *
>>> from model import Customer,Product,Transactions,TransactionItem
```

誕生日や取引日時を入力するため datetime パッケージをインポートします。

```Python
>>> import datetime
```

Customerオブジェクトを作成します。
以下のコマンドラインの2行目から4行目は必ずスペースを4個入れてからプログラムを記述します。
５行目はEnterキーのみ入力することで、一連の処理が実行されます。

```Python
>>> With Session(Engine) as session:
...     c = Customer(customerId = 1111, firstName='太郎', lastName='山田',
...     firstNameKana='タロウ', lastNameKana='ヤマダ', dob = datetime.date(1979,3,5),
...     gender = '男')
...
```

以下のコマンドでCustomerオブジェクトを登録し、コミットを実行することで、IRISにてデータが登録されコミットされます。

```Python
>>> session.add(c)
>>> session.commit()
```

システム管理ポータルを起動し、データが登録されたことを確認します。
Chromeなどのブラウザを起動し、以下のURLにアクセスします。

**https://locahost:52773/csp/sys/UtilHome.csp**

「システムエクスプローラ」メニューの「SQL」をクリック、「実行」をクリックします。
画面上方にある「ネームスペース」の右にある「%SYS」をクリック、「User」をクリックします。

「クエリ実行」タブをクリックし、その下の入力欄に以下のSQLを入力し「実行」ボタンをクリックします。

```SQL
SELECT * FROM Customer
```

SQL入力欄の下に表が表示され、先ほど登録したレコードが表示されることを確認してください。

### 6.2. 取引データの登録

顧客情報と同様に取引データを登録します。先ほど登録した顧客情報オブジェクト c を取得します。
製品情報にプロジェクター(p1) と設置台(p2) を登録し、取引明細データ(i1,i2)に各製品を3点として
登録します。
取引データを作成し顧客情報オブジェクト c を登録、作成した取引明細データを追加します。

```Python
>>> with Session(Engine) as session:                                                        
...     c = session.get(Customer,1111)
...     p1 = Product(productCode='AA-0001',prductName='プロジェクター',price=15000)
...     p2 = Product(productCode='AB-0001', productName='プロジェクター設置台',price=10000)
...     t = Transactions(customer=c)
...     i1 = TransactionItem(product=p1,unitPrice=12000,quantity=3)
...     i2 = TransactionItem(product=p2,unitPrice=8000,quantity=3)
...     t.total = i1.unitPrice * i1.quantity
...     t.total += i2.unitPrice * i2.quantity
...     t.items.append(i1)
...     t.items.append(i2)
```

ここで、session オブジェクトにadd()メソッドを実行すると、既に登録されている顧客情報を再度登録しようとしてエラーが発生しますので、ここはmerge()メソッドで登録されていない物のみ登録するようにします。

```Python
>>> session.merge(t)
```

merge が終わりましたら、commit()メソッドを実行し、これらのオブジェクトを登録、確定します。

```Python
>>> session.commit()
```

顧客情報の登録時と同様に管理ポータルにて Transactions クラスならびに TransactionItem にデータが登録されているかをご確認ください。
Transactions クラスの dateTimeプロパティには登録日時が入りますので、合わせてご確認ください。

### 6.3. データの削除

データを削除するには session オブジェクトのdelete()メソッドを使用します。

```Python
>>> t = session.get(Transactions,1)
>>> session.delete(t)
>>> session.commit(t)
```

## 7. 顧客情報メンテナンスの作成

ここからは、今まで作成したものを元に、顧客情報メンテナンス画面を作ってゆきます。

### 7.1. 顧客一覧画面の作成

まずは顧客情報を一覧表示する画面を作成します。
customer.py を作成し、以下の内容を入力します。

```Python
from nicegui import ui
from setting import *
from model import *

@ui.page('/')
def page():
    # 顧客情報の取得
    customers = session.query(Customer).all()
    customer_data = [{"customerId": c.customerId, "lastName": c.lastName, "firstName": c.firstName,
                  "lastNameKana": c.lastNameKana, "firstNameKana": c.firstNameKana, "dob": c.dob,
                  "gender": c.gender} for c in customers]

    # 画面の表示
    with ui.row():
        ui.button('新規顧客', on_click=lambda: add_customer())
    
    # グリッドの表示
    grid = ui.aggrid({
        'defaultColDef': {'flex': 1},
        'columnDefs': [
            {'headerName': '顧客ID', 'field': 'customerId', 'checkboxSelection': True},
            {'headerName': '姓', 'field': 'lastName'},
            {'headerName': '名', 'field': 'firstName'},
            {'headerName': 'カナ姓', 'field': 'lastNameKana'},
            {'headerName': 'カナ名', 'field': 'firstNameKana'},
            {'headerName': '生年月日', 'field': 'dob'},
            {'headerName': '性別', 'field': 'gender'},
        ],
        'rowData': customer_data,
    }).on('rowSelected', lambda msg: row_selected(msg))

# サーバの実行
ui.run()
```

このプログラムを起動すると、page()関数が実行されます。
この関数内の以下の部分で、顧客情報(Customerクラス)をすべて取得し customersに代入しています。
customers はオブジェクトのリストですので、次の行で customers のリストを1つずつ読み込み、Json形式に変換し、customer_data に格納しています。

```Python
    # データの読み込み
    customers = session.query(Customer).all()
    customer_data = [{"customerId": c.customerId, "lastName": c.lastName, "firstName": c.firstName,
                      "lastNameKana": c.lastNameKana, "firstNameKana": c.firstNameKana, "dob": c.dob,
                      "gender": c.gender} for c in customers]
```

以下の部分ではaggrid()という表形式で表示するコントロールを用いて、各フィールドの情報を表示しています。

```Python
    aggrid = ui.aggrid({
        'defaultColDef': {'flex': 1},
        'columnDefs': [
            {'headerName': '顧客ID', 'field': 'customerId', 'checkboxSelection': True},
            {'headerName': '姓', 'field': 'lastName'},
            {'headerName': '名', 'field': 'firstName'},
            {'headerName': 'カナ姓', 'field': 'lastNameKana'},
            {'headerName': 'カナ名', 'field': 'firstNameKana'},
            {'headerName': '生年月日', 'field': 'dob'},
            {'headerName': '性別', 'field': 'gender'},
        ],
        'rowData': customer_data,
    })
```

これで、一覧表示画面が作成できました。

### 7.2. 顧客編集ダイアログボックスの作成

続いて、顧客情報を入力するダイアログボックスを作成します。
page()関数のすぐ下に、以下の編集画面を追記します。
まずは比較的単純な形でダイアログボックスを作成し、キャンセルボタンをクリックするとダイアログボックスを閉じるようにします。

```Python
    :
    :
  @ui.page('/')
  def page():
    # ******* ここから追加します。*********************
    # 編集用ダイアログボックスを表示
    def edit_customer(customer: Customer,rowIndex: Integer):
        with ui.dialog() as dialog, ui.card():
            if customer.customerId == None:
                ui.input('顧客ID').bind_value(customer,'customerId')
            else:
                ui.input('顧客ID').bind_value(customer,'customerId').disable()
            with ui.row():
                ui.input('姓').bind_value(customer,'lastName')
                ui.input('名').bind_value(customer,'firstName')

            with ui.row():
                ui.input('カナ姓').bind_value(customer, 'lastNameKana')
                ui.input('カナ名').bind_value(customer,'firstNameKana')

            with ui.row():
                ui.input('生年月日').bind_value(customer,'dob')
                ui.input('性別').bind_value(customer,'gender')

            with ui.row(wrap=False):
                ui.input('郵便番号').bind_value(customer,'zipCode').props("size=30")
                ui.space()
                ui.input('住所').bind_value(customer,'address').props("size=120")
            
            ui.input('電話番号').bind_value(customer,'phone')

            with ui.row().classes('w-full justify-center'):
                ui.button('保存')
                ui.button('削除')
                ui.button('ｷｬﾝｾﾙ', on_click=lambda: close_dialog(dialog))

        dialog.open()

    # ダイアログを閉じる
    def close_dialog(dialog):
        dialog.close()

```

このダイアログボックスでは文字入力コントロール ui.input() を使用、bind_value プロパティで、入力フォームと顧客情報オブジェクトのプロパティとを連携させています。
住所や郵便番号はsizeプロパティを設定することで、入力エリアの幅を調整しています。
主キーとなる顧客IDを修正させないようにするため、コントロールに.disable()を指定しています。
dialog.open()でダイアログボックスを表示、dialog.close()で非表示としています。

さらに、グリッドにて行が選択されたときにrow_selected()メソッドを呼び出すよう、グリッドの記述の最後に以下の設定を追加しています。

```Python
        'rowData': customer_data,
    }).on('rowSelected', lambda msg: row_selected(msg))    # <===この部分[.on(...)]を追加
```

row_selected() メソッドは、以下のように特定のレコードが選択された際、顧客ＩＤの値を使用し、ＤＢからデータを取得、edit_customer()メソッドを呼び出します。
この処理はclose_dialog()メソッドと顧客情報取得処理の間に追加します。

```Python
    # グリッドにて行が選択されたときの処理
    def row_selected(event):
        if event.args["selected"] == True:
            obj = session.get(Customer,event.args["data"]["customerId"])
            if obj != None:
                edit_customer(obj,event.args["rowIndex"])
```

パラメータのeventにはargsプロパティがあり、Dict形式でイベントの詳細情報を保持しています。

- **event.args["selected"]**  True... 行を選択、False...行選択を解除
- **event.args["data"]** 選択した行の各項目値 (Dict形式)
- **event.args["rowIndex"]** 選択した行の位置 (先頭行は0)

これで、一覧表示から各行のチェックボックスをクリックしますと、ダイアログボックスが表示され、詳細なデータが表示されるようになりました。

### 7.3. データ保存機能の作成

ダイアログボックスにデータが表示され、編集できるようになりましたので、修正した内容を保存する機能を作成します。

```Python
    # 顧客情報の保存
    def save_customer(c: Customer, dialog: ui.dialog, rowIndex: Integer):
        # バリデーションチェック
        if c.customerId == None or c.customerId == '':
            ui.notify('顧客IDが入力されていません',timeout=0,close_button="OK")
            return
        if len(c.lastName) == 0 or len(c.firstName) == 0:
            ui.notify('氏名が入力されていません',timeout=0,close_button="OK")
            return
        if len(c.lastNameKana) == 0 or len(c.firstNameKana) == 0:
            ui.notify('カナが入力されていません',timeout=0,close_button="OK")
            return
        try:
            if type(c.dob) is str:
                c.dob = date.fromisoformat(c.dob)
        except Exception as err:
            ui.notify('生年月日の形式が誤っています',timeout=0,close_button="OK")
            return
        if len(c.gender) == 0:
            ui.notify('性別が入力されていません',timeout=0,close_button="OK")
            return

        # 顧客情報の保存
        session.merge(c)
        session.commit()

        dialog.close()
```

ここでは、編集した顧客情報オブジェクトのバリデーションチェックを行い、データが入力されているかをチェックしています。また、生年月日(dob)は文字列をdate形式に変換しdobに再登録しています。date形式に変換できなかった場合、Exceptionが発生するため、try構文でエラー時にメッセージを出して復旧するようにしています。

date形式を変換するにはdateクラスが必要ですので、インポート部分にdateを追加します。

```Python
from nicegui import ui
from setting import *
from model import *
from datetime import date    #<=== ここを追加
```

バリデーションチェックが終わると、以下の処理でデータベースを更新しています。

> session.merge(c)
> session.commit()

save_customer()メソッドは「保存」ボタンをクリックした際に実行するよう、以下のようにui.button('保存')にon_clickイベントを追加します。

```Python
  ui.button('保存', on_click=lambda: save_customer(customer, dialog, rowIndex))
```

### 7.4. データ削除機能の作成

データ保存機能と同様にデータ削除機能を追加します。以下のようにdelete_customer()メソッドを追加します。

```Python
  # 顧客情報の削除
  def delete_customer(customer: Customer,dialog: ui.dialog, rowIndex: Integer):
      if customer.customerId != None:
          session.delete(customer)
          session.commit()

      dialog.close()
```

このメソッドでは、顧客IDがNullでなかった時に

> session.delete(customer)
> session.commit()

を実行し、データベースから情報を削除しています。
この処理はダイアログボックスの「削除」ボタンをクリックすることで実行させますので、ui.button('削除') にon_click イベントを追加します。
ついでに分かりやすいよう、ボタンを赤に変更します。

```Python
  ui.button('削除', on_click=lambda: delete_customer(customer, dialog, rowIndex)).props(f'color="red"')
```

### 7.5. データ作成機能の作成

今度は新規にデータを作成する機能を追加します。グリッドの上にボタンを配置し、クリックすると
add_customer() メソッドが実行され、新規の顧客情報オブジェクトを作成し、edit_customer()メソッドを呼び出します。
add_customer()メソッドは以下のようになります。

```Python
  :
def page():
    # *********** ここから追加 ***********    
    # 新規顧客作成
    def add_customer():
        customer = Customer()
        edit_customer(customer,None)

    # 編集用ダイアログを表示
```

新規作成した場合、新たに顧客情報オブジェクトを作成しedit_customer()を呼び出します。
グリッドの行位置はありませんので、第２パラメータはNoneとしています。

「新規顧客」ボタンはグリッド表示の手前に記載することで、グリッドの上に配置されます。

```Python
    # 画面の表示
    with ui.row():
        ui.button('新規顧客', on_click=lambda: add_customer())
    
    # グリッドの表示
```

これで、顧客情報を追加、変更、削除できるようになりましたが、これらの操作を行ってもグリッドは更新されませんので、更新に必要な処理を追加します。

### 7.6. グリッドの更新

グリッドの情報を更新するにはグリッドの表示で指定している rowData の内容を変更し、グリッドのupdate()メソッドを実行する必要があります。

追加、変更、削除の際にrowDataの内容を更新するため、データを追加、変更するupdate_row()、データを削除する delete_row()メソッドを追加します。
これらはrow_selected()メソッドの前に挿入します。

```Python
  # グリッドの更新
  def update_row(c: Customer,rowIndex: Integer):
      cdata={"customerId": c.customerId, "lastName": c.lastName, "firstName": c.firstName,
                "lastNameKana": c.lastNameKana, "firstNameKana": c.firstNameKana, "dob": c.dob,
                "gender": c.gender}
      if rowIndex == None:
          # rowIndexが指定されていない場合、行を追加
          grid.options['rowData'].append(cdata)
      else:
          grid.options['rowData'][rowIndex] = cdata
      grid.update()

  # グリッドから行を削除
  def delete_row(rowIndex: Integer):
      ui.notify("rowIndex:" + str(rowIndex))
      del grid.options['rowData'][rowIndex]
      grid.update()
```

update_row() メソッドでは受け取った顧客情報オブジェクトからrowDataのレコード形式に変換し、rowIndex が None であれば、新規顧客なので、rowData のリストにappend()メソッドで追加しています。rowIndexが指定されている場合、そのレコードを変換したレコードで上書きしています。

delete_row()メソッドでは、del コマンドで指定されたrowIndexのレコードを削除しています。、

updat_row() はsave_customer()メソッドでダイアログボックスを閉じる直前に実行しています。

```Python
        # 顧客情報の保存
        session.merge(c)
        session.commit()

        update_row(c,rowIndex)  # <==== ここに追加

        dialog.close()
```

同様にdelete_row() はdelete_customer()メソッドでダイアログボックスを閉じる直前に実行しています。

```Python
        if customer.customerId != None:
            session.delete(customer)
            session.commit()
            delete_row(rowIndex)   # <======= ここに追加>

        dialog.close()

```

これで、変更が正しく反映されるようになりました。

### 7.7. 入力に便利なコントロールとバインド設定

ダイアログボックスを見ると、文字列入力のみとなっており、入力しやすいコントロールを使用したほうが使いやすくなるかと思います。
今回は、生年月日と性別を、入力しやすいコントロールに置き換えます。

#### 7.7.1. 生年月日の入力

こちらはDate pickerという文字列入力の右側にカレンダー表示ボタンがあり、それをクリックするとカレンダーが表示され、クリックするとその日付が入力されるというものです。

> ui.input('生年月日').bind_value(...)

の代わりに以下の処理を入力します。

```Python
    with ui.input('生年月日') as dob_input:
        dob_input.bind_value(customer,'dob')
        with ui.menu().props('no-parent-event') as dob_menu:
            with ui.date().bind_value(dob_input):
                with ui.row().classes('justify-end'):
                    ui.button('閉じる', on_click=dob_menu.close).props('flat')
        with dob_input.add_slot('append'):
            ui.icon('edit_calendar').on('click', dob_menu.open).classes('cursor-pointer')

    def select_gender(item):
        gender_input.text=item + '性'
    
    def set_gender(str):
        if str == '男性' or str == '女性':
            return str
        else:
            return None
    def get_gender(str):
        if str == '男性' or str == '女性':
            return str
        else:
            return '性別'
```

これを実行しますと、文字列表示の右に「カレンダー修正」のアイコンが表意jされ、
それをクリックすると、カレンダーが表示されるというものです。

#### 7.7.2. 性別の入力

性別の指定にはDropdown_buttonを使用します。
ui.input('性別') の代わりに以下の処理を記載します。

```Python
    def select_gender(item):
        gender_input.text=item

    def set_gender(str):
        if str == '男性' or str == '女性':
            return str
        else:
            return None
    def get_gender(str):
        if str == '男性' or str == '女性':
            return str
        else:
            return '性別'
    with ui.dropdown_button('性別', auto_close=True) as gender_input:
        gender_input.bind_text(customer,'gender',forward= lambda x: set_gender(x), backward= lambda x: get_gender(x))
        ui.item('男性', on_click=lambda: select_gender('男性'))
        ui.item('女性', on_click=lambda: select_gender('女性'))
```

ボタンのキャプションを顧客情報オブジェクトのgenderプロパティと連携させるため、

> .bind_text()

を使用しています。
性別が指定されていないときは、ボタンのキャプションを「性別」とするため、
bind_text()のパラメータにforward,backwardを指定しています。
forwardに指定しているset_gender()メソッドではdropdown_buttonのキャプション値をgenderプロパティ値に変換しています。
backwardにしている get_gender()メソッドではgenderプロパティの値をdropdown_buttonのキャプションに変換しています。

#### 7.7.3. 郵便番号検索機能の追加

以下のように、郵便番号に入力された値で検索APIにアクセスし、得られた住所を住所欄に表示します。
run.io_bound()を使用してRESTアクセスするには、以下のパッケージを読み込みます。
パッケージのインポート部分は以下のようになります。

```Python
from nicegui import ui,run  # <=== run を追加
from setting import \*
from model import \*
from datetime import date

import requests   #<=== http リクエスト用
import json       #<=== json 変換用
```

検索APIにアクセスする処理は以下のinvoke_zipcode()メソッドとなります。

```Python
    with ui.dialog() as dialog, ui.card():
        # ********* 以下の部分を追加 ***********************
        async def invoke_zipcode(zipcode):
            URL = 'https://zipcloud.ibsnet.co.jp/api/search?zipcode='+zipcode
            response = await run.io_bound(requests.get, URL, timeout=10)
            if response.status_code == 200:
                result = json.loads(response.content.decode('utf-8'))
                address = result["results"][0]
                address_input.value = address["address1"] + " " + address["address2"] +" " +  address["address3"]
            else:
                ui.notify(f'郵便番号検索時にエラーが発生しました StatusCode={response.status_code})',timeout=0,close_button="OK")
```

ダイアログボックスのui.input('郵便番号') と ui.input('住所')の間に検索ボタンを追加し、on_clickイベントにてinvoke_zipcode()メソッドを呼び出します。

```Python
    ui.input('郵便番号').bind_value(customer,'zipCode').props("size=30")
    ui.button('検索',on_click= lambda: invoke_zipcode(customer.zipCode)).classes("w-32")　# <=== この行を追加
    address_input = ui.input('住所').bind_value(customer,'address').props("size=120")
```

以上で、顧客情報のメンテナンスができるようになりました。

## 8. 製品情報メンテナンスの作成

顧客情報メンテナンスと同様に product.py に製品情報を追加、変更、削除できる画面を作成します。

```Python
from nicegui import ui
from setting import *
from model import *

@ui.page('/')
def page():
    # 新規製品作成
    def add_product():
        product = Product()
        edit_product(product,None)

    # 編集用ダイアログボックスを表示
    def edit_product(product: Product,rowIndex: Integer):
        with ui.dialog() as dialog, ui.card():
                    
            if product.productCode == None:
                ui.input('製品コード').bind_value(product,'productCode')
            else:
                ui.input('製品コード').bind_value(product,'productCode').disable()
            ui.input('製品名').bind_value(product,'productName')
            ui.number('標準価格').bind_value(product,'price')

            with ui.row().classes('w-full justify-center'):
                ui.button('保存', on_click=lambda: save_product(product, dialog, rowIndex))
                ui.button('削除', on_click=lambda: delete_product(product, dialog, rowIndex)).props(f'color="red"')
                ui.button('ｷｬﾝｾﾙ', on_click=lambda: close_dialog(dialog))

        dialog.open()

    # 製品情報の保存
    def save_product(p: Product, dialog: ui.dialog, rowIndex: Integer):
        # バリデーションチェック
        if p.productCode == None or p.productCode == '':
            ui.notify('製品コードが入力されていません',timeout=0,close_button="OK")
            return
        if len(p.productName) == 0:
            ui.notify('製品名が入力されていません',timeout=0,close_button="OK")
            return
        if p.price<= 0:
            ui.notify('標準価格が入力されていません',timeout=0,close_button="OK")
            return

        # 製品情報の保存
        session.merge(p)
        session.commit()

        update_row(p,rowIndex)

        dialog.close()

    # 製品情報の削除
    def delete_product(product: Product,dialog: ui.dialog, rowIndex: Integer):
        if product.productCode != None:
            session.delete(product)
            session.commit()
            delete_row(rowIndex)

        dialog.close()

    # ダイアログを閉じる
    def close_dialog(dialog):
        dialog.close()

    # グリッドの更新
    def update_row(p: Product,rowIndex: Integer):
        pdata={"productCode": p.productCode, "productName": p.productName, "price": p.price}
        if rowIndex == None:
            # rowIndexが指定されていない場合、行を追加
            grid.options['rowData'].append(pdata)
        else:
            grid.options['rowData'][rowIndex] = pdata
        grid.update()

    # グリッドから行を削除
    def delete_row(rowIndex: Integer):
        ui.notify("rowIndex:" + str(rowIndex))
        del grid.options['rowData'][rowIndex]
        grid.update()

    # グリッドにて行が選択されたときの処理
    def row_selected(event):
        if event.args["selected"] == True:
            obj = session.get(Product,event.args["data"]["productCode"])
            if obj != None:
                edit_product(obj,event.args["rowIndex"])

    # 製品情報の取得
    products = session.query(Product).all()
    product_data = [{"productCode": p.productCode, "productName": p.productName, "price": p.price} for p in products]

    # 画面の表示
    with ui.row():
        ui.button('新規', on_click=lambda: add_product())
    
    # グリッドの表示
    grid = ui.aggrid({
        'defaultColDef': {'flex': 1},
        'columnDefs': [
            {'headerName': '製品コード', 'field': 'productCode', 'checkboxSelection': True},
            {'headerName': '製品名', 'field': 'productName'},
            {'headerName': '標準価格', 'field': 'price'},
        ],
        'rowData': product_data,
    }).on('rowSelected', lambda event: row_selected(event))

# サーバの実行
ui.run()
```

### 8.1. メインページの作成

顧客情報メンテナンス、製品情報メンテナンスが動作することを確認しましたら、これらを１つのアプリとして動作するようメニューを追加したいと思います。
main.py に以下の処理を記入します。

```Python
from contextlib import contextmanager
from nicegui import ui

import customer
import product

@ui.page('/customer')
def customer_page() -> None:
    with frame('顧客情報メンテ'):
        customer.page()

@ui.page('/product')
def product_page() -> None:
    with frame('製品情報メンテ'):
        product.page()

@ui.page('/')
def page():
    with frame('メインページ'):
        ui.label('ようこそ')

# サーバの実行
ui.run()

@contextmanager
def frame(navigation_title: str):
    #ui.colors(primary='#6E93D6', secondary='#53B689', accent='#111B1E', positive='#53B689')
    with ui.header():
        with ui.row().classes('w-full items-center'):
            with ui.button(icon='menu'):
                with ui.menu() as menu:
                    ui.menu_item('トップページ', lambda: ui.navigate.to('/'))
                    ui.menu_item('顧客メンテ', lambda: ui.navigate.to('/customer'))
                    ui.menu_item('製品メンテ', lambda: ui.navigate.to('/product'))
                    ui.separator()
                    ui.menu_item('Close', menu.close)
            ui.label(navigation_title).tailwind.font_weight('extrabold').font_size('xl')
    yield
```

main.py には３つのページがあり、各ページのURLは以下の通りです。

| URL|ページ内容|呼出メソッド|コンテンツ処理ファイル|
|----|---|---|
| / | トップページ | page()|main.py |
| /customer | 顧客情報メンテページ | customer_page()| customer.py |
| /product | 製品情報メンテページ | product_page()| product.py |

顧客情報メンテ、製品情報メンテページは先ほど作成したcustomer.py、product.pyを使用するため、main.pyの以下の構文にてインポートしています。

> import customer
> import product

各ページを表示させるcustomer_page()、product_page()では frame()メソッドを呼び出し、共通のメニューを表示させます。

### 8.2. 顧客情報メンテ、製品情報メンテの改造

main.py　から呼び出せるよう、customer.py、product.py の以下の部分を削除します。

```Python

@pi.page('/')   #<=== この行を削除
def page():
    :
    :
# サーバ実行   # <=== この行を削除
ui.run()       # <=== この行を削除
```

以上でコマンドプロンプトから main.py を実行することで メインページが表示され、メニューアイコンをクリック、ページを指定することで
それらのページが表示されるようになります。

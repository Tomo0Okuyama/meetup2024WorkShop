# Embedded Python で IRIS データにアクセスしよう

Embedded Python は、IRIS に標準で備わっている「**Python コードで IRIS データにアクセスする**」ための製品機能です。

Embedded Python により Python ロジックが IRIS プロセスとして実行されます。これにより、さまざまな Python ライブラリと IRIS データを密接に組み合わせることができ、アプリケーションに大きなメリットをもたらします。

このワークショップを通じて、Embedded Python で IRIS データやメソッドにアクセスする具体的なコードを体験いただけます。

# 目次などなど

- [1. Embedded Python とは](#1-embedded-python-とは)
- [2. Embedded Python の実行手段](#2-embedded-python-の実行手段)
- [3. Embedded Python で IRIS リソースにアクセス](#3-embedded-python-で-iris-リソースにアクセス)
    - [3-0. 事前準備](#3-0-事前準備)   
    - [3-1. クラスメソッドを実行](#3-1-クラスメソッドを実行)
    - [3-2. SQL を実行](#3-2-sql-を実行)
    - [3-2. グローバルデータ](#3-2-グローバルデータ)
  

## 1. Embedded Python とは

「Embedded」という名前のとおり、IRIS 製品に「埋め込まれた」 Python です。IRIS プロセス上で Python ロジックを動作させることが出来ます。この「IRIS プロセスとして動作する」というのが大きな特徴で、IRIS のデータや IRIS ネイティブ言語である ObjectScript と Python とが密接かつシームレスに連携することが可能となります。

![1.png](./1.png "1.png")

IRIS 2024.1 for Windows では、一般的な Python モジュールではなく、IRIS 製品に同梱されている irispython.exe が内部的に利用されます。

## 2. Embedded Python の実行手段

Embedded Python を実行する方法は、以下の (A)(B)(C) の 3 種類あります。
上で説明しましたが、OS から見ると、どれも通常の IRIS プロセスとして起動します。

(A) クラスに **[Language = python]** を宣言したメソッドを登録して実行する。メソッド内部に Python 言語を記述する。**Embedded Python を利用したアプリ実装時にお勧め。**

        ClassMethod hello() [ Language = python ]
        {
            import datetime
            day1 = datetime.date(1976, 5, 22)
            print(day1.isoformat())
        }

(B) ObjectScript から %SYS.Python を指定して Python ライブラリをロードする。ObjectScript 言語で記述するため、通常のルーチンからも呼べる。

        set datetime = ##class(%SYS.Python).Import("datetime")
        set day1 = datetime.date(1976, 5, 22)
        write day1.isoformat()

(C) IRIS ターミナルから :py コマンドで Embedded Python 用のシェルを起動することで、（一般の Python Shell と同じように）インタラクティブに実行する。**Embedded Python の動きを簡単に確認するときにお勧め。**

        USER>:py
        >>> import datetime
        >>> day1 = datetime.date(1976, 5, 22)
        >>> print(day1.isoformat())
        1976-05-22

## 3. Embedded Python で IRIS リソースにアクセス

ここから、Embedded Python を使って、実際に IRIS のデータやクラスにアクセスしてみましょう。基本的に IRIS リソースにアクセスするときは、iris パッケージを利用します。Embedded Python には iris パッケージは標準で含まれており、 **import iris** で利用できます。

このワークショップでは、上記の **(C)**、IRIS ターミナルから :py コマンドで起動する Embedded Python 用のシェル上で行います。 **>>>** がプロンプトです。

        USER>:py
        >>>

### 3-0. 事前準備

IRIS に以下のクラス User.eptest を登録し、テストデータをセットしておきます (ソース eptest.cls 参照)

        Class User.eptest Extends %Persistent
        {        
        property name As %String;

        ClassMethod sum(x1 As %Integer, x2 As %Integer) As %Integer
        {
            quit $g(x1)+$g(x2)
        }
        
        ClassMethod init()
        {
            kill ^User.eptestD
            &sql( insert into eptest (name) values ('Naka') )
            &sql( insert into eptest (name) values ('Sato') )          
            kill ^a
            set ^a=55, ^a(1)=123, ^a(1,4)=999
        }

        }

データ登録（テーブルデータ と ^a を保存）

        USER>do ##class(User.eptest).init()

### 3-1. クラスメソッドを実行

IRIS クラスメソッドは、iris パッケージを使って、以下のように実行します。

        import iris
        ret = iris.cls('classname').methodname(arg)

ここで、User.eptest クラス sum メソッドを、Embedded Python Shell から呼んでみましょう。

        >>> import iris
        >>> a = 2
        >>> b = 1
        >>> ans = iris.cls('User.eptest').sum(a, b)
        >>> print(ans)
        3

### 3-2. SQL を実行

IRIS テーブルにたいして、iris パッケージを使って、以下のように SQL を実行します。

        import iris
        st = iris.sql.prepare('SQL statement')
        rs = st.execute(param)

ここで、User.eptest テーブルに対して、Embedded Python Shell から SQL をいくつか実行しましょう。

(1) select name from eptest [^1]

        >>> import iris
        >>> st = iris.sql.prepare('select name from eptest')
        >>> rs = st.execute()
        >>> for row in rs:
        ...   print(row[0])
        ...
        Naka
        Sato

(2) insert into eptest (name) values (xxx)

        >>> st2 = iris.sql.prepare('insert into eptest (name) values (?)')
        >>> rs2 = st2.execute('Yama')

(3) select name from test where ID = xxx  [^1]

        >>> st3 = iris.sql.prepare('select name from eptest where ID=?')
        >>> rs3 = st3.execute(3)
        >>> for row in rs3:
        ...   print(row[0])
        ...
        Yama

[^1]: "..."プロンプトと print コマンドの前に 空白 をおくこと。また、"..."プロンプトのあとに改行を入力すると結果が出力される。


### 3-2. グローバルデータ

        set ^a=55
        set ^a(1)=123
        set ^a(1,4)=999

に対して、Embedded Python からは、以下のように GET/SET できます。

        ClassMethod test1() [ Language = python ]
        {
           import iris
           g = iris.gref('a')
           
           # データを取得 (トップノードは [None])
           print( g[None] )
           print( g['1'] )
           print( g['1','4'] )
           
           # ^aを更新
           g[None] = 555
           g['test'] = 100
        }

実行例

        USER>do ##class(User.test).test1()
        55
        123
        999

        USER>zw ^a
        ^a=555
        ^a(1)=123
        ^a(1,4)=999
        ^a("test")=100        

ああ
   

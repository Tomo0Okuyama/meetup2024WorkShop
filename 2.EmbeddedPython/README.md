# Embedded Python で IRIS データにアクセスしよう

Embedded Python は、IRIS に標準で備わっている「**Python コードで IRIS データにアクセスする**」ための製品機能です。

Embedded Python により Python ロジックが IRIS プロセスとして実行されます。これにより、さまざまな Python ライブラリと IRIS データを密接に組み合わせることができ、アプリケーションに大きなメリットをもたらします。

このワークショップを通じて、Embedded Python で IRIS データやメソッドにアクセスする具体的なコードを体験いただけます。

# 目次などなど

- [1. Embedded Python とは](#1-embedded-python-とは)
- [2. Embedded Python の実行手段](#2-embedded-python-の実行手段)
- [3. Embedded Python で IRIS リソースにアクセス](#3-embedded-python-で-iris-リソースにアクセス)
    - [3-1. グローバル](#3-1-グローバル)
  

## 1. Embedded Python とは

「Embedded」という名前のとおり、IRIS 製品に「埋め込まれた」 Python です。IRIS プロセス上で Python ロジックを動作させることが出来ます。この「IRIS プロセスとして動作する」というのが大きな特徴で、IRIS のデータや IRIS ネイティブ言語である ObjectScript と Python とが密接かつシームレスに連携することが可能となります。

![1.png](./1.png "1.png")

IRIS 2024.1 for Windows では、一般的な Python モジュールではなく、IRIS 製品に同梱されている irispython.exe が内部的に利用されます。

## 2. Embedded Python の実行手段

Embedded Python を実行する方法は、以下の 3 種類あります。実際のアプリとしては **"1"** がお勧めです。3 種類とも、OS から見ると、通常の IRIS プロセスとして起動しています。

1. クラスに **[Language = python]** を宣言したメソッドを登録して実行する。メソッド内部に Python 言語を記述する。

        ClassMethod hello() [ Language = python ]
        {
            import datetime
            day1 = datetime.date(1976, 5, 22)
            print(day1.isoformat())
        }

2. ObjectScript から %SYS.Python を指定して Python ライブラリをロードする。ObjectScript 言語で記述するため、通常のルーチンからも呼べる。

        set datetime = ##class(%SYS.Python).Import("datetime")
        set day1 = datetime.date(1976, 5, 22)
        write day1.isoformat()

3. IRIS ターミナルから :py コマンドで Embedded Python 用のシェルを起動することで、（一般の Python Shell と同じように）インタラクティブに実行する。

        USER>:py
         
        Python 3.9.19 (main, Jul 18 2024, 18:05:27) [MSC v.1927 64 bit (AMD64)] on win32
        Type quit() or Ctrl-D to exit this shell.
        >>> import datetime
        >>> day1 = datetime.date(1976, 5, 22)
        >>> print(day1.isoformat())
        1976-05-22

## 3. Embedded Python で IRIS リソースにアクセス

ここから、Embedded Python を使って、IRIS のデータやクラスにアクセスしてみましょう。基本的に IRIS リソースにアクセスするときは、iris パッケージを利用します。Embedded Python では、iris パッケージは標準で含まれており、 **import iris** で利用できます。

### 3-1. グローバルデータ

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
   

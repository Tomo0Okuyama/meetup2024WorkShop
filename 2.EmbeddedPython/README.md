# Embedded Python で IRIS データにアクセスしよう

Embedded Python は、IRIS に標準で備わっている「**Python コードで IRIS データにアクセスする**」ための製品機能です。

Embedded Python により Python ロジックが IRIS プロセスとして実行されます。これにより、さまざまな Python ライブラリと IRIS データを密接に組み合わせることができ、アプリケーションに大きなメリットをもたらします。

このワークショップを通じて、Embedded Python で IRIS データやメソッドにアクセスする具体的なコードを体験いただけます。

# 目次などなど

- [1. Embedded Python とは](#1-embedded-python-とは)
- [2. Embedded Python を実行してみよう](#2-embedded-python-を実行してみよう)

## 1. Embedded Python とは

「Embedded」という名前のとおり、IRIS 製品に「埋め込まれた」 Python です。IRIS プロセス上で Python ロジックを動作させることが出来ます。この「IRIS プロセスとして動作する」というのが大きな特徴で、IRIS のデータや IRIS ネイティブ言語である ObjectScript と Python とが密接かつシームレスに連携することが可能となります。

![1.png](./1.png "1.png")


IRIS 2024.1 for Windows では、一般的な Python モジュールではなく、IRIS 製品に同梱されている irispython.exe が内部的に利用されます。

## 2. Embedded Python を実行してみよう

Embedded Python を実行する方法は、以下の 3種類あります。実際のアプリとしては **1** がお勧めです。
1. クラスに **[Language = python]** を宣言したメソッドを登録して実行する。メソッド内部に Python 言語を記述する。

        ClassMethod hello() [ Language = python ]
        {
            import datetime
            day1 = datetime.date(1976, 5, 22)
            print(day1.isoformat())
        }

3. ObjectScript からライブラリを利用するときに %SYS.Python を指定する。通常のルーチンからも呼べる。

        set datetime = ##class(%SYS.Python).Import("datetime")
        set day1 = datetime.date(1976, 5, 22)
        write day1.isoformat()

4. 

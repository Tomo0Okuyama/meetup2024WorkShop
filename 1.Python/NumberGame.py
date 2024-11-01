# モジュールrandomをインポート（使用前に必要）
import random

# 正解を変数answerに代入
answer = random.randint(1,100)
in_str = input("1から100までの数を当てましょう")
# ユーザーが入力したデータを整数型に変換して変換guessに代入
guess = int(in_str)

# ユーザー入力と正解が不一致の間ループ
while guess != answer:
    if guess < answer:
        print("もっと大きいです")
    elif guess > answer:
        print("もっと小さいです")
    else:
        print("ここに来る?")
    in_str = input("1から100までの数を当てましょう、もう一度")
    guess = int(in_str)

print("お疲れ様でした、正解は %d でした" % answer)

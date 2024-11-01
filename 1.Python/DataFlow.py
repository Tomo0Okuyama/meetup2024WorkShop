x=5
if x > 3:
    print("xは3より大きい")
elif x == 3:
    print("xは3")
else:
    print("xは2以下")

a, b = 0, 1
while a < 10:
    print(a, end=",")
    a, b = b, a+b
print()

for i in range(10):
    print(i, end=",")
print()


for i in range(10):
    if( i % 3 ) == 0:
        continue
    print(i, end=",")
    if i == 8:
        break

a=0
try:
    ans = 128/a
except ZeroDivisionError:
    print("ゼロでは割れません")
except Exception as e:
    print(f"その他エラー: {e}")
else:
    print("例外は発生しませんでした")
finally:
    print("ここで最終処理")

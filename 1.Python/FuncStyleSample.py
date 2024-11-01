def generate_ints(N):
    for i in range(N):
        yield i

print('ジェネレータサンプル')

gen=generate_ints(2)
while True:
    try:
        print(next(gen))
    except StopIteration as e:
        print(f'StopIteration検知')
        break


print('ジェネレータ式サンプル')

listSample = ['InterSystems', 'iris']
upIter = ( li.upper() for li in listSample )
for item in upIter:
    print(item)

print('リスト内包表記サンプル')

lgList = [ li.upper() for li in listSample if len(li) > 4 ]
print(lgList)

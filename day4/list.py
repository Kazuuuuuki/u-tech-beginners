100以下の三の倍数と五の倍数を小さい順番に並べたリストをまどろっこしく作る、list型関数の導入
list1 = []
list2 = []
for i in range(1,101):
    if i%3 == 0:
        list1.append(i)
for i in range(1,101):
    if i%5 == 0:
        list2.append(i)
print(list1)
print(list2)
list2.append(23)
print(list2)
list2.remove(23)
print(list2)
list2.insert(5,23)
print(list2)
list2.pop(5)
print(list2)
list1.append(list2)
print(list1)
list1.pop()
print(list1)
list1.extend(list2)
print(list1)
list2.reverse()
print(list2)
list2.clear()
print(list2)
print(list1.count(15))
for i in list1:
    if list1.count(i) == 2:
        list1.remove(i)
print(list1)
list1.sort()
print(list1)

listとsetの違い
list1 = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42, 45,
 48, 51, 54, 57, 60, 63, 66, 69, 72, 75, 78, 81, 84, 87, 90, 93, 96,
  99, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80,
  85, 90, 95, 100]

print(list1)

set1 ={3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42, 45,
  48, 51, 54, 57, 60, 63, 66, 69, 72, 75, 78, 81, 84, 87, 90, 93,
   96, 99, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70,
    75, 80, 85, 90, 95, 100}

print(set1)

辞書型
Deutsch = {'eins':1, 'zwei':2, 'drei':3}
print(Deutsch)
#普通の辞書型の定義
Deutsch['vier']=4
print(Deutsch)
#辞書型への要素の追加
print(Deutsch['zwei'])
#keyに対応するvalueを返す
Deutsch2 = dict([('Apfel','apple'),('Vater','father'),('Mutter','mother'),('Bruder','brother')])
#dict関数によるタプルを使った辞書の定義
print(Deutsch2)
print(Deutsch2['Mutter'])

Deutsch1 = dict(eins=1,null=0,zwei=2,drei=3,vier=4)
#dict関数によるキーワード引数を使った辞書の定義
print(Deutsch1)

l1=list(Deutsch1.keys())
print(l1)

l2=sorted(Deutsch1.keys())
print(l2)

for i,l in Deutsch.items():
    print(i,l)
#keyとvalueを同時に取り出すループ

行列、リストの内包
matrix = [[1,3],[2,-2],[-1,0]]
print (matrix)
#行列の第(2,1)成分を答えよ
print (matrix[1][0])
#行列の転置を求めよ
transposed = []
for l in range(0,2):
    transposed.append([matrix[i][l]  for i in range(0,3)])
print(transposed)

集合の演算
a = set('abracadabra')
b = set('alacazam')

print(a)
print(a-b)
print(a|b)
print(a&b)
print(a^b)

行列の積と転置の関数
a行、b列の行列xとb行、c列の行列y
def Product(x,y,a,b,c):
    [[sum(x[i][l]*y[m][i]for i in range(0,b)) for l in range(0,a)]for m in range(0,c)]

def Transposed(x,a,b):
    [[x[i][l]for i in range(0,b)]for l in range(0,a)]



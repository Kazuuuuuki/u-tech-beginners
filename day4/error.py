#構文エラー
import random
x = random.random()
y = random.random()
print(x,y)

if x == y:
    print("x is y")
else:
    print("x is not y")

#NameError
while k <= 100:
    a += k
    k += 1
print(a)

#ZeroDivisionError
print(4 / 0)
#TypeError
a = input("a = ;")
b = input("b = ;")

print(a * b)

#BMI測定(Try文)
h = float(input("Height(m) = "))
w = float(input("Weight(kg) = "))

x = w / (h ** 2)
y = int(x)

print("your BMI =", y)

'''
try:
    h = float(input("Height(m) = "))
    w = float(input("Weight(kg) = "))
    x = w / (h ** 2)
    y = int(x)
    print("your BMI =", y)

    raise NameError("funny")
except ValueError:
    print("Retry!")
finally:
    raise
'''
#Else文
try:
    h = float(input("Height(m) = "))
    w = float(input("Weight(kg) = "))
    x = int(w / (h ** 2))

except ValueError:
    print("Type numbers!")

else:
    print("your BMI =", x)

finally:
    print("fin end")

#with文(定義済みクリーンアップ処理)
f = open('date.txt','r')

for row in f:
    print(row)

f.close()

with open('date.txt') as f:
    for raw in f:
        print(raw, end = "")
#raise
try:
    h = float(input("Height(m) = "))
    w = float(input("Weight(kg) = "))
    x = w / (h ** 2)
    y = int(x)
    print("your BMI =", y)
    raise NameError("Hello")
except ValueError:
    print("Retry!")
finally:
    raise

#Импортируем функцию randint из библиотеки random и даем ей название sor
from random import randint as sor
a = []
for i in range ( 0, 100 ):
    a.append(sor( 0,  100_000 ))
print(a)
stop_flag = True
kolvo_sravneniy1 = 0
while stop_flag is True:
    stop_flag = False
    for i in range( 0, len(a) - 1):
        kolvo_sravneniy1 +=1
        if a[i] < a[i + 1]:
            swap = a[i]
            a[i] = a[i + 1]
            a[i + 1] = swap
            print(a)
            stop_flag = True
print(a)
b = a.copy() 
c = []
kolvo_sravneniy2 = 0
while len(b) > 0:
    print(b)
    max = b[0]
    for i in range(0, len(b)):
        kolvo_sravneniy2 += 1
        if b[i] < max:
         max = b[i]
    c.append(max)
    b.remove(max)
print(c)
print(f"Количество сравнений для пузырька {kolvo_sravneniy1}")
print(f"Количество сравнений для выборки {kolvo_sravneniy2}")


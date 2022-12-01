from random import randint
num = [0]*12
amm = 1000000
for i in range(amm):
    a = randint(1,6)
    b = randint(1,6)
    num[a+b-2] += 1
n = 0
for i in range(11):
    print('Вероятность, что в сумме ',n+2, ' : ', num[n]/amm*100)
    n+=1

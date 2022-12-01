from random import randint
k = 2
def genpassw2(b):
 print('Введите 1, чтобы получитть пароль типа ***-***-***')
 print('Введите 2, чтобы получитть пароль типа *****-*****-*****')
 print('Введите 3, чтобы получитть пароль типа ****-****-****')
 psw = ''
 b = int(input())
 if b == 1:
     c = 4
 elif b == 2:
     c = 6
 elif b == 3:
     c = 5
 for i in range(1,c*3):
  if i%c == 0 and i != 0:
   psw+='-'
  else:
   n = randint(33, 126)
   s = chr(n)
   if s == '-':
    i-=1
    continue
   psw+=s
 return(psw)

print(genpassw2(k))
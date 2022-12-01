from random import randint
k = 9
def genpassw(b):
 psw = ''
 for i in range(b):
  n = randint(33, 126)
  s = chr(n)
  psw+=s
 return(psw)

print(genpassw(k))

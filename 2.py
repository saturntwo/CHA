k = 'r56upYtr5694'
def password(a):
    s = 0
    x = 'qwertyuiopasdfghjklzxcvbnm'
    z = 'QWERTYUIOPASDFGHJKLZXCVBNM'
    y = '1234567890'
    for i in range(len(a)):
        if a[i] in x:
            s+=1
            break
    for i in range(len(a)):
        if a[i] in y:
            s+=1
            break
    for i in range(len(a)):
        if a[i] in z:
            s+=1
            break
    if len(a) >=8:
        s+=1
    return(s)
print(password(k))

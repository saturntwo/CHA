k = 'r56Yt'
def password(a):
    leng = False
    numb = False
    letb = False
    lets = False
    if len(a) >= 8:
        leng = True
    for i in range(len(a)):
        if 'A' <= a[i] <= 'Z':
            letb = True
        elif 'a' <= a[i] <= 'z':
            lets = True
        elif '0' <= a[i] <= '9':
            numb = True
    return int(leng) + int(numb) + int(letb) + int(lets)


print(password(k))

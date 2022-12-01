k = int(input())
def is_simple(a):
    s = 0
    n = 1
    if a==0 or a==1:
        return False
    for i in range(a//2):
        if a % n == 0:
            s+=n
        n+=1
    if s > 1:
        return False
    else:
        return True
if is_simple(k):
    print('Simple')
else:
    print('Not simple')

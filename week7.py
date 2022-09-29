def s(a,b,h):
    s=(h*(a+b))/2
    return s
A=[]
for i in range(1):
    a=int(input('a: '))
    b=int(input('b: '))
    h=int(input('h: '))
    A.append(s(a,b,h))
print(A[i])

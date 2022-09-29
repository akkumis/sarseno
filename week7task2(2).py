def s(a,b):
    s=a*b
    return s
A=[]
for i in range(3):
    print('enter the data  ', i, 'rectangle')
    a=int(input('a: '))
    b=int(input('b: '))
    A.append(s(a,b))
for i in range(3):
    print('the area of ', i, ' rectangle is ', A[i])

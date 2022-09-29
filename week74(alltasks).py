print("Task 4.1")
from fractions import Fraction
a,b = 5,8
c,d = 9,6
ir_fr = Fraction(Fraction(a,b), Fraction(c,d))
print("irreducible fraction: ", ir_fr)
def gcd(a, b):  
    if a > b: s = b  
    else: s = a  
    for i in range(1, s + 1):  
        if((a%i==0)and(b%i==0)):  
            gcd = i  
    print(gcd)
gcd(ir_fr.numerator, ir_fr.denominator)


print("Task 4.2")
x = 1;
y = 1;
p1,p2 = 1,2
f1,f2 = 3,4
n1,n2 = 1,2
radius = 3
def point_in(px, py, radius, x, y):
    if ((x-px)**2+(y-py)**2)<=radius**2:
        print("POINT IS INSIDE")
    else:
        print("POINT IS OUTSIDE")
point_in(p1,p2,radius,x,y)
point_in(f1,f2,radius,x,y)
point_in(n1,n2,radius,x,y)


print("Task 5.1")
from fractions import Fraction
a,b = 5,4
c,d = 7,8
ir_f = Fraction(Fraction(a,b) - Fraction(c,d))
print("irreducible fraction: ", ir_f)
def gcd(a, b):  
    if a > b: s = b  
    else: s = a  
    for i in range(1, s + 1):  
        if((a%i==0)and(b%i==0)):  
            gcd = i  
    print(gcd)
gcd(ir_f.numerator, ir_f.denominator)


print("Task 5.2")
def div(a):
    for i in range(1, a+1):
        if a%i==0:
            print(i, end=" ")
        else: continue
n = int(input("Enter the number: "))
div(n)

print("\nTask 6.1")
def gcd(a, b):  
    if a > b: s = b  
    else: s = a  
    for i in range(1, s + 1):  
        if((a%i==0)and(b%i==0)):  
            gcd = i  
    return gcd
def lcm(a, b):
    lcm = (a*b)/gcd(a,b)
    print(lcm)
a = int(input("Enter the 1st number: "))
b = int(input("Enter the 2nd number: "))
print(gcd(a,b))
lcm(a,b)
print("\nTask 6.2")
a = float(input("First side: "))
b = float(input("Second side: "))
c = float(input("Third side: "))
d = float(input("Fourth side: "))
dia = float(input("Diagonal: "))
def quadl(a,b,c,d,dia):
    def heron_f(a,b,c):
        p=0.5*(a+b+c)
        return (p*(p-a)*(p-b)*(p-c))**0.5
    return heron_f(a,b,dia) + heron_f(c,d,dia)
print("The area of a quadliteral : ", quadl(a,b,c,d,dia))

print("\n Task7.1")
a = int(input("long base: "))
b = int(input("short base: "))
h = int(input("height: "))
t = int(input("leg: "))

print("Area:", triangleArea(a-b,h) + rectangleArea(b,h))

print("\nTask7.2")
def decToOct(n):
    return '{:010o}'.format(n)

a = int(input())
print(decToOct(a))

print("\nTask8.1")
def divByTheirD(n):
    ans = []
    for i in range(1,n+1):
        s = str(i)
        temp = True
        for j in s:
            if int(j) == 0:
                temp = False
            elif i % int(j) != 0:
                temp = False
        if temp:
            ans.append(i)
    return ans

n = int(input("n: "))
print(divByTheirD(n))

print("\nTask8.2")
def swapFirstLast(a):
    a[0],a[len(a)-1] = a[len(a)-1],a[0]
    return a

m = int(input("length of array: "))
A = []
for i in range(m):
    n = int(input("element of array: "))
    A.append(n)

print(A)
print(swapFirstLast(A))

print("\ntask9.1")
def sumOfDigits(n):
    s = str(n)
    sum = 0
    for i in s:
        sum += int(i)
    return sum

n = int(input("N: "))
sub = sumOfDigits(n)
ans = 0
while n > 0:
    ans += 1
    n -= sub

print(ans)

print("n\Taskl9.2")
def prdArr(n):
    prd = 1
    for i in n:
        prd *= i
    return prd

for i in range(3):
    a = random.sample(range(100), 15)
    print(a)
    print(prdArr(a))
    print(meanArr(a,sumArr(a)))

print("\nTask11.1")
def Twins(n):
    print([[i, i+2] for i in range(n, 2*n - 1)])
    
Twins(int(input()))

print("\n Task11.2")
B = int(input())
C = [[random.randrange(10) for i in range(A)] for j in range(B)] 
for i, row in enumerate(C):
    max = min = 0
    for j, elem in enumerate(row):
        if elem > row[max]:
            max = j
        if elem < row[min]:
            min = j
    row[max], row[0] = row[0], row[max]
    row[min], row[-1] = row[-1], row[min]
print(C)

print("\n Task12.1")
def getSum(value):
    res = 1
    for i in range(2, int(value**0.5) + 1):
        if value % i == 0:
            res += i + value // i
    return res

for i in range(10, 10000):
    sum1 = getSum(i)
    sum2 = getSum(sum1)
    if sum2 == i and sum1 != sum2:
        print(i, sum1)

print("\n Task12.2")
def m(a, b, c):
    return 1/2(sqrt(2*b**2+2*c**2-a**2))

print("\nTask13.1")
num=int(input("enter number: "))
for num in range(num, 1000):
    sum1=0
    numcp=num
    if(num>=10 and num<100):
        while(num>0):
            digit=int(num%10)
            d2=digit*digit
            sum1=sum1+d2
            num=int(num/10)

    if(num>=100 and num<1000):
        while(num>0):
            digit=int(num%10)
            d2=digit*digit*digit
            sum1=sum1+d2
            num=int(num/10)
    if(numcp==sum1):
        print("angstrong number: ", sum1)
    

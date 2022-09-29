def sum1(a):
  if len(a) == 1:
        return a[0]
  else:
        return a[0] + sum1(a[1:])
def af(a):
    return sum(a)/len(a)
for i in range(3):
    n=int(input('enter number of elements: '))
    for i in range(n):
        print('enter  number ', n,  "of array")

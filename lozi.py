
n=int(input("enter number of row: "))

i=0
f = (n*2 + 1)//2
star = 1

while i<n :
    for j in range(f):
        print(" " , end='')
    for j in range(star):
        print('*', end='')
    print()
    star+=2
    f-=1
    i+=1    

star-=4
f+=2
x=0
while x<(n-1):
    for j in range(f):
        print(' ', end='')
    for j in range(star):
        print('*', end='')
    print()
    star-=2
    f+=1
    x+=1        
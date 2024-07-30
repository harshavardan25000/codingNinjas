
n=int(input())

i=1

while i<=n:
    spaces=1
    while spaces<=n-i:
        print(' ',end='')
        spaces+=1

    j=spaces
    while j<=n+i-1:
        print('*',end='')
        j+=1

    print()
    i+=1
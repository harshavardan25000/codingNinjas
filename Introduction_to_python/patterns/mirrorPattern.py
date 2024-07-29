n=int(input())

i=1
while i<=n:
    j=n
    while j>=1:
        if i>=j:
            print('*',end='')
        else:
            print(' ' ,end='')
        j-=1
    print()

    i+=1
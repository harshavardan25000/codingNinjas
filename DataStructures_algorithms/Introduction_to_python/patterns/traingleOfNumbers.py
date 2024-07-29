n=int(input())

i=1

while i<=n:
    spaces=1
    while spaces<=n-i:
        print(' ',end='')
        spaces+=1

    numbers,j=i,1

    while j<=i:
        print(numbers,end='')
        j+=1
        numbers+=1
    numbers-=1
    while numbers>i:
        print(numbers-1,end='')
        numbers-=1


    print()
    i+=1
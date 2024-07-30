n=int(input())

i=0

while i<n:
    
    j=i
    while j>=0:
        print(chr(ord('A')+n-j-1),end='')
        j-=1
    print()

    i+=1
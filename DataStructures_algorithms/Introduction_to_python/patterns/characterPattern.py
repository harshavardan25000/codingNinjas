n=int(input())

i=0

while i<n:
    
    j=0
    while j<=i:
        print(chr(ord('A')+i+j),end='')
        j+=1
    print()

    i+=1
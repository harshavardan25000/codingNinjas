n=int(input())

mid_line=(n//2)+1
i=1

while i<mid_line:
    spaces=1
    while spaces<=mid_line-i:
        print(" ",end='')
        spaces+=1
    
    j=spaces-1
    while j<=mid_line-1:
        print('*',end='')
        j+=1
    
    
        
    print()

    i+=1

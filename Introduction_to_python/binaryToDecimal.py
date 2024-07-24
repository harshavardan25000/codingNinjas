num=input()
if num=='0':
    print(0)
else:
    result,l=0,len(num)-1

    for i in num:
        if i=='1':
            result+=2**l
        l-=1

    print(result)
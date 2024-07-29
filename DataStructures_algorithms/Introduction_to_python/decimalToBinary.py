num=int(input())
if num==0: 
    print(0)
result=''
while num>0:
    if num%2==0:
        result+='0'
    else:
        result+='1'
    num//=2
print(result[::-1])
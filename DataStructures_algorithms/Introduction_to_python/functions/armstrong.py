# 1-1000

# for num in range(1,1000):
#     org_num,sum=num,0
#     while num>0:
#         digit=num%10
#         sum+=(digit**3)
#         num=num//10
#     #print(sum)
#     if sum==org_num:
#         print(f'{org_num} is armstrong')

n=1

while n<=1000:
    org_number=n
    x=n
    sum=0

    while x>0:
        r=x%10
        sum=sum+r**3
        x=x//10

    if sum==org_number:
        print(f'{org_number} is armstrong')
    n+=1

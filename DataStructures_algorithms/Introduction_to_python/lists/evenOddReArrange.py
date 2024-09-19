n=11
temp=[x+1 for x in range(n)]
print(temp)
odd_idx,even_idx=1,1

while odd_idx<n and even_idx<n:

    while temp[odd_idx]%2!=0:
        odd_idx+=1
    temp[even_idx],temp[odd_idx]=temp[odd_idx],temp[even_idx]
    even_idx+=1

    even_new_idx=odd_idx
    eve_last_ele=n-1
print(temp)
    




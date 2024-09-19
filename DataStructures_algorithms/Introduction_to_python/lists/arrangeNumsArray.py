def arrange(arr, n) :
    
    odd_idx,even_idx=0,n-1

    for num in range(1,n+1):
        if num%2!=0:
            arr[odd_idx]=num
            odd_idx+=1
        else:
            arr[even_idx]=num
            even_idx-=1


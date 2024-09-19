def sortZeroesAndOne(arr, n) :
    # write your code here 
    start_ptr,zero_ptr=0,0
    while start_ptr<n:
        while zero_ptr<n:
            if arr[zero_ptr]!=0:
                zero_ptr+=1
            else:
                arr[start_ptr]=0
                start_ptr+=1
                zero_ptr+=1
        arr[start_ptr]=1
        start_ptr+=1

        
    



arr=[1,0,1,1,0,1,0,1]
sortZeroesAndOne(arr, 8) 
print(arr)
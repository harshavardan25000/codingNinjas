def findTriplet(arr, n, x) :
        total=0
        for i in range(n):
            for j in range(i+1,n):
                for k in range(j+1,n):
                    print(i,j,k)
                    if arr[i]+arr[j]+arr[k]==x:
                        total+=1
        return total

findTriplet([1,2,3,4,5,6,7],7,12)
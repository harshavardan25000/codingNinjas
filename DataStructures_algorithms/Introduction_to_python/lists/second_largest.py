def secondLargestElement(arr, n):
    first_largest,second_largest=-2147483648,-2147483648
    for num in arr:
        if num>first_largest:
            first_largest,second_largest=num,first_largest
        elif num>second_largest:
            second_largest=num
    return second_largest
print(secondLargestElement([1,2,3,4,5,6,7], 7))
# creating an empty list
arr = []
  
# number of elements as input
n = int(input("Enter number of elements : "))
  
# iterating till the range
for i in range(0, n):
    ele = int(input())
  
    arr.append(ele) # adding the element
      
print(arr)
# function for removing duplicates
def removeDuplicate(arr, n):
    j = 0
    
    # traverse elements of arr
    for i in range(0, n-1): 
        # if ith element is not equal to (i+1)th element, then store ith value in arr[j]
        if (arr[i] != arr[i+1]):
            arr[j] = arr[i]
            j = j+1

    # store last value of arr in arr[j]
    arr[j] = arr[n-1]
    j = j+1
    
    # print first j elements of array arr
    for i in range(0, j):
        print("%d"%(arr[i]), end = " ")

n = len(arr)
# calling function when number of elements in array is greater than 1
if (n > 1):
    removeDuplicate(arr, n)

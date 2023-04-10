# Challenge Title
Write a function called BinarySearch which takes in 2 parameters: a sorted array and the search key. Without utilizing any of the built-in methods available to your language, return the index of the array’s element that is equal to the value of the search key, or -1 if the element is not in the array.

<br>

## Whiteboard Process
![CC-03](./CC-03.png)

<br>

## Approach & Efficiency
### Big O : Time -> O (n) , Space O (1) .

<br> 

## Solution

    def BinarySearch(arr, key):
        left = 0
        right = len(arr) - 1
    
    while left <= right:
        mid = (left + right) // 2
        
        if arr[mid] == key:
            return mid
        
        elif arr[mid] < key:
            left = mid + 1
        
        else:
            right = mid - 1
    
    return -1

<br>

## examples :

Given  : [1,2,3,4,5,6,8] ,5

Return : 4

<br>
<br>

Given  : [11,16,28,30,32] ,29

Return : -1

# Challenge Title
### Write a function called insertShiftArray which takes in an array and a value to be added. Without utilizing any of the built-in methods available to your language, return an array with the new value added at the middle index.
<br>

## Whiteboard Process
![CC-02](./CC-02.png)
<br>

## Approach & Efficiency
### This CC took me one hour to complete it .
### Big O : Time -> O (n) , Space O (1) .
<br> 

## Solution :
### let mid-index = array.length / 2
### let last-element = array-Last-Element

### for loop over the array that start from the end of the
### array to the mid-index and replace the current
### element in loop with the element before it

### then :
### assign the mid-index to the new value
### and add the last element to the array at the end

## examples :
### Given  : [1,2,3,4,5,6] ,7 
### Return : [1,2,3,7,4,5,6]
### Given  : [5,6,7,8,9] ,10 
### Return : [5,6,7,10,8,9]
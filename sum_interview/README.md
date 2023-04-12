# Challenge Title
Given a matrix, find the sum of each row,Without utilizing any of the built-in methods available to your language, return an array with the new value added at the middle index.

<br>

## Whiteboard Process
![CC-04](./CC-04.png)

<br>

## Approach & Efficiency
Time -> O(n^2)
<br>
Space -> O(1)

<br> 

## Solution
    def row_sums(matrix):
       row_sums = []
       for row in matrix:
        row_sum = sum(row)
        row_sums.append(row_sum)
    return row_sums



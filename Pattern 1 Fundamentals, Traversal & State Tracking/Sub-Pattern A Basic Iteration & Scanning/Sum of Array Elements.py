class Solution:
    def sum(self,arr, n): 
        s=0
        for i in arr:
            s+=i
        return s
"""Here is the breakdown of your approach:Time Complexity: $O(N)$, where $N$ is the number of
 elements in the array. Your code iterates through the array exactly once, which is theoretically
optimal since you must look at every element to calculate the total sum.Space Complexity: $O(1)$.
 You are only using a single variable (s) to store the running total, requiring constant
 extra memory regardless of the input size."""




#best one
#return sum(arr) because it is built-in function and it is optimized for performance.
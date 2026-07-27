class Solution:
    def countOdd(self, arr, n):
        # Your code goes here
        cnt=0
        for i in arr:
            if i%2!=0:
                cnt+=1
        return cnt

"""
Here is the breakdown of your approach:Time Complexity: $O(N)$, 
where $N$ is the number of elements in the array. You are iterating 
through the array exactly once to check each element.
Space Complexity: $O(1)$. You are only using a single variable (cnt)
 to keep track of the odd numbers, requiring constant extra memory.
"""



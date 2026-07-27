#brute force i thought is copying, sorting, and comparing would have been an 
# unnecessary $O(N \log N)$ time and $O(N)$ space



class Solution:
    def arraySortedOrNot(self, arr, n):
        if len(arr)==1:
            return True
        for i in range(1,len(arr)):
            if arr[i-1]>arr[i]:
                return False
        return True
        
"""Time Complexity: $O(N)$ where $N$ is the number of elements in the array. You only need a single pass through the data, which is the theoretical best case since you must inspect every element at least once to guarantee it is sorted.Space Complexity: $O(1)$. You are only tracking an index variable i, using no additional scaling memory."""
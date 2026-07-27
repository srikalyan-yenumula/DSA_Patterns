class Solution:
    def findMaxConsecutiveOnes(self, nums):
        cnt=m=0
        for i in nums:
            if i==1:
                cnt+=1
            else:
                cnt=0
            m=max(m,cnt)
        return m
"""Time Complexity: $O(N)$ where $N$ is the number of elements in the array. You perform a single pass through the list.Space Complexity: $O(1)$. You are only using two scalar variables (cnt and m) to track the state, requiring no additional scaling memory."""
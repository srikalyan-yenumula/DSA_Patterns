class Solution:
    def linearSearch(self, nums, target):
        for ind,val in enumerate(nums):
            if val==target:
                return ind
        return -1
"""Time Complexity: $O(N)$, where $N$ is the number of elements in the array. In the worst-case scenario (the target is at the very end or not in the list at all), you will have to iterate through every single element.Space Complexity: $O(1)$. You are only storing the current index and value during the iteration, which requires constant extra memory regardless of the size of the input list."""

"""Interview Follow-ups


How would you modify the function to return all indices of the target instead of just the smallest?
i take a list and store the index of all targets and return the list. If the list is empty, return -1.
"""
class Solution:
    def linearSearch(self, nums, target):
        l=[]
        for i,v in enumerate(nums):
            if v==target:
                l.append(i)
        if not l:
            return -1
        else:
            return l

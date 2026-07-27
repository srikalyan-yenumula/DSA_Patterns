class Solution:
    def linearSearch(self, nums, target):
        for ind,val in enumerate(nums):
            if val==target:
                return ind
        return -1
"""Time Complexity: O(N), where N is the number of elements in the array. 
In the worst-case scenario (the target is at the very end or not in the list at all),
 you will have to iterate through every single element.
 Space Complexity: O(1). You are only storing the current index and value during the iteration, 
 which requires constant extra memory regardless of the size of the input list."""
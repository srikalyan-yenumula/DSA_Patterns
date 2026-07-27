#i dont thought but brute force is using sort and return last element.
from typing import List

class Solution:
    def largestElement(self, nums):
        # Sort the list 
        nums.sort()

        # Largest element will be 
        # at the last index of the list
        largest = nums[-1]

        # Return the largest element
        return largest

# Main function
if __name__ == "__main__":
    nums = [3, 2, 1, 5, 2]

# Create an instance of the Solution class
    sol = Solution()
    
    largest = sol.largestElement(nums)

    # Print the largest element
    print(largest)


"""Time Complexity: O(N * logN), as we are sorting the array, where N is the length of the array.

Space Complexity: O(n) for sort() method."""


class Solution:
    def largestElement(self, nums):
        lar=float("-inf")
        for val in nums:
            lar=max(lar,val)
        return lar


"""Time Complexity: O(N), where N is the number of elements in the array. 
You are iterating through the array exactly once.Space Complexity: O(1). 
You are only using a single variable (lar) to track the maximum value, 
requiring constant extra memory."""

class Solution:
    def largestElement(self, nums):
        return max(nums)
"""Optimal Complexity: It still runs in O(N) time and uses O(1) space,
 which is theoretically the best you can do.Standard Built-ins: Just like sum(), 
 Python's max() is written in highly optimized C code under the hood. 
 """
#i dont thought but brute force is using sort and return last element.


class Solution:
    def largestElement(self, nums):
        lar=float("-inf")
        for val in nums:
            lar=max(lar,val)
        return lar


"""Time Complexity: $O(N)$, where $N$ is the number of elements in the array. You are iterating through the array exactly once.Space Complexity: $O(1)$. You are only using a single variable (lar) to track the maximum value, requiring constant extra memory."""

class Solution:
    def largestElement(self, nums):
        return max(nums)
"""Optimal Complexity: It still runs in $O(N)$ time and uses $O(1)$ space, which is theoretically the best you can do.Standard Built-ins: Just like sum(), Python's max() is written in highly optimized C code under the hood. It executes significantly faster than a manual for loop with float("-inf") because it avoids the overhead of the Python interpreter running line-by-line."""
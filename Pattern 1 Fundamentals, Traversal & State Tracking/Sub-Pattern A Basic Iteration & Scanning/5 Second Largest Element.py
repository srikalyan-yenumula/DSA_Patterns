#i dont thought about it
class Solution:
    
    # Function to find the second largest element
    def secondLargestElement(self, nums):
        n = len(nums)
        
        # Check if the array has less than 2 elements
        if n < 2:
            # Indicating no second largest element is possible
            return -1
        
        # Sort the list in ascending order
        nums.sort()

        # Largest element will be at last index
        largest = nums[-1]

        secondLargest = -1

        # Traverse the sorted list from right to left
        for i in range(n-2, -1, -1):

            ''' If the current element is not
            equal to the largest element'''
            if nums[i] != largest:

                ''' Assign the current element 
                as the second largest and break'''
                secondLargest = nums[i]
                break

        # Return the second largest element
        return secondLargest
"""Time Complexity: $O(N \log N)$ where $N$ is the number of elements in the array. This is due to the nums.sort() operation. The subsequent for loop takes $O(N)$ in the worst case, but the sorting dominates the time complexity.Space Complexity: $O(N)$. Python's built-in sort() uses the Timsort algorithm, which requires up to $O(N)$ memory in the worst case to perform its operations."""


#i thought it but i dont code it and move to optimal one directly
class Solution:

    def secondLargestElement(self, nums):
        # Get the length of the array
        n = len(nums)

        # Check if the array has less than 2 elements
        if n < 2:
            # If true, return -1 indicating there is no second largest element
            return -1 

        # Initialize variables to store the largest and second largest elements
        largest = float('-inf')
        secondLargest = float('-inf')

        # First traversal to find the largest element
        for i in range(n):
            largest = max(largest, nums[i])

        # Second traversal to find second largest element
        for i in range(n):
            if nums[i] > secondLargest and nums[i] != largest:
                secondLargest = nums[i]

        # Return the second largest element
        return -1 if secondLargest == float('-inf') else secondLargest


nums = [1, 2, 4, 6, 7, 5]

# Create an instance of the Solution class
sol = Solution()

"""Call the method to find the second 
largest element and store the result"""
result = sol.getSecondLargest(nums)

print("Second largest is", result)

# Example usage
nums = [1, 2, 4, 6, 7, 5]

# Create an instance of the Solution class
sol = Solution()

''' Call the method to find 
the second largest element'''
ans = sol.secondLargestElement(nums)

print("The second largest element is:", ans)

"""Complexity Analysis 
Time Complexity: O(N) + O(N) = O(2N), due to two linear traversals, where N is the length of the array.

Space Complexity: O(1), as no additional space is required."""




class Solution:
    def secondLargestElement(self, nums):
        m=sm=float("-inf")
        for val in nums:
            if val>m:
                sm=m
                m=val
            elif val<m and val>sm:
                sm=val
        if sm==float("-inf"):
            return -1
        return sm
"""Time Complexity: $O(N)$, where $N$ is the number of elements in the array. You process every element in a single pass.Space Complexity: $O(1)$. You only use two variables (m and sm), requiring constant extra memory."""
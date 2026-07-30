# i directly though about hashing
#brute.


"""
Intuition 
Naive way is to count the occurrences of each element. The element which will have count greater than half the array size will be the majority element."""

from typing import List

class Solution:
    # Function to find the majority element in an array
    def majorityElement(self, nums: List[int]) -> int:
        
        # Size of the given array
        n = len(nums)
        
        # Iterate through each element of the array
        for i in range(n):
            
            # Counter to count occurrences of nums[i]
            cnt = 0 
            
            # Count the frequency of nums[i] in the array
            for j in range(n):
                if nums[j] == nums[i]:
                    cnt += 1
            
            # Check if frequency of nums[i] is greater than n/2
            if cnt > (n // 2):
                # Return the majority element
                return nums[i]
        
        # Return -1 if no majority element is found
        return -1

if __name__ == "__main__":
    arr = [2, 2, 1, 1, 1, 2, 2]
    
    # Create an instance of Solution class
    sol = Solution()
 
    ans = sol.majorityElement(arr)
    
    # Print the majority element found
    print("The majority element is:", ans)




"""
Complexity Analysis 
Time Complexity: O(N2), for nested for loops used, where N is the size of the array

Space Complexity: O(1) as no extra space is used.
"""

#better
class Solution:
    def majorityElement(self, nums):
        nums.sort()
        return nums[len(nums)//2]
"""
Complexity Analysis
Time Complexity
O(n log n) because the sorting algorithm (Timsort) dominates the complexity, where n is the length of the input array.
Space Complexity
O(n) because Timsort requires auxiliary space proportional to n in the worst case to store the elements being sorted."""




#mine better
from collections import Counter
class Solution:
    def majorityElement(self, nums):
        freq=Counter(nums)
        for k in freq.keys():
            if freq[k]>len(nums)//2:
                return k
"""

Time Complexity: $O(N)$Where $N$ is the total number of elements in the nums array.Counter(nums):
 Python iterates through the entire nums array exactly once to count the occurrences and build the dictionary.
   This takes $O(N)$ time.for k in freq.keys():: This loops through the unique numbers in your array
   . Let's call the number of unique elements $U$. Since $U$ can never be larger than $N$, 
   this loop takes at most $O(N)$ time.freq[k] > len(nums)//2: Hash map lookups and basic math take $O(1)$ time.
   Combining the building phase and the looping phase gives you $O(N) + O(N)$, which simplifies directly 
   to $O(N)$ Time.
   Space Complexity: $O(N)$Where $N$ is the total number of elements.
   The freq dictionary: You are storing every unique number and its count in a Hash Map.
   In the absolute worst-case scenario, if almost every number in the array is different 
   (e.g., [1, 2, 3, 4, 5, 5, 5, 5, 5]), your dictionary will store roughly $N/2$ elements.
   Because $N/2$ scales linearly with the size of the array, we drop the fraction and call it $O(N)$ Space."""
#i dont get brute . i directly done below one.[go dirctly to optimal]
"""
The brute force way to solve this problem will be to count the frequency of each element in the array, and once found, this frequency can be compared with the highest and the lowest frequency. Accordingly, the highest and the lowest frequency can be set.
"""
class Solution:
    """ Function to get the sum of highest
    and lowest frequency in array """
    def sumHighestAndLowestFrequency(self, nums):
        
        # Variable to store the size of array
        n = len(nums)
        
        """ Variable to store maximum 
        and minimum frequency """
        max_freq = 0
        min_freq = n

        # Visited array
        visited = [False] * n
        
        # First loop
        for i in range(n):
            # Skip second loop if already visited
            if visited[i]:
                continue
            
            """ Variable to store frequency
            of current element """
            freq = 0
            
            # Second loop
            for j in range(i, n):
                if nums[i] == nums[j]:
                    freq += 1
                    visited[j] = True
            
            """ Update maximum and 
            minimum frequencies """
            max_freq = max(max_freq, freq)
            min_freq = min(min_freq, freq)
            
        # Return the required sum
        return max_freq + min_freq

# Example usage
nums = [1, 2, 2, 3, 3, 3]

""" Creating an instance of 
Solution class """
sol = Solution()

""" Function call to get the sum of highest
and lowest frequency in array """
ans = sol.sumHighestAndLowestFrequency(nums)

print("The sum of highest and lowest frequency in the array is:", ans)


#Complexity Analysis:
#Time Complexity: O(N2) (where N is the size of the array given) – Using two nested loops.

#Space Complexity: O(N) – Using a visited array of size N and a couple of variables.





from collections import Counter
class Solution:
    def sumHighestAndLowestFrequency(self, nums):
        freq=Counter(nums)
        max_freq=float("-inf")
        min_freq=float("inf")
        for f in freq.values():
            if f>max_freq:
                max_freq=f
            if f<min_freq:
                min_freq=f
        return max_freq+min_freq


"""
Time Complexity: $O(N)$ where $N$ is the number of elements in the array. 
Building the Counter takes $O(N)$, and your loop iterates over the unique keys, 
taking $O(U)$ time (where $U$ is the number of unique elements).
$O(N + U)$ simplifies to $O(N)$.
Space Complexity: $O(U)$ where $U$ is the number of unique elements. 
This is the memory used to store the frequencies in the Counter dictionary.
"""
#i dont get brute . i directly done below one.[go dirctly to optimal]
"""A brute-force way to solve this problem will be to use two loops:

First loop to iterate on the array, selecting an element.
Second loop to traverse the remaining array to find the occurrences of the selected element in the first loop.

Maintain a visited array to mark the elements to keep track of duplicate elements that were already taken into account."""

class Solution:
    # Function to get the highest 
    # occurring element in array nums
    def mostFrequentElement(self, nums):
        
        # Variable to store the size of array
        n = len(nums)
        
        # Variable to store maximum frequency
        maxFreq = 0 
        
        # Variable to store element 
        # with maximum frequency
        maxEle = 0
        
        # Visited array
        visited = [False] * n
        
        # First loop
        for i in range(n):
            # Skip second loop if already visited
            if visited[i]:
                continue
            
            # Variable to store frequency
            # of current element 
            freq = 0
            
            # Second loop
            for j in range(i, n):
                if nums[i] == nums[j]:
                    freq += 1
                    visited[j] = True
            
            # Update variables if new element having 
            # highest frequency is found
            if freq > maxFreq:
                maxFreq = freq
                maxEle = nums[i]
            elif freq == maxFreq:
                maxEle = min(maxEle, nums[i])
        
        # Return the result
        return maxEle

if __name__ == "__main__":
    nums = [4, 4, 5, 5, 6]
    
    # Creating an instance of Solution class
    sol = Solution()
    
    # Function call to get the
    # highest occurring element in array nums
    ans = sol.mostFrequentElement(nums)
    
    print("The highest occurring element in the array is:", ans)

#Time Complexity: O(N2) (where N is the size of the array given) – Using two nested loops.

#Space Complexity: O(N) – Using a visited array of size N and a couple of variables.



from collections import defaultdict
class Solution:
    def mostFreqEle(self, arr):
        # code here
        freq=defaultdict(int)
        for i in arr:
            freq[i]+=1
        max_freq=float("-inf")
        max_key=float("-inf")
        for key in freq.keys():
            if freq[key]>max_freq:
                max_freq=freq[key]
                max_key=key
            elif freq[key]==max_freq:
                max_key=max(max_key,key)
        return max_key
            
"""
Time Complexity: $O(N)$ where $N$ is the number of elements in the array. Building the dictionary
takes $O(N)$ time, and iterating through the unique keys takes $O(U)$ time (where $U$ is the 
number of unique elements). Since $U \le N$, it simplifies to $O(N)$.
Space Complexity: $O(U)$ where $U$ is the number of unique elements in the array. 
In the worst case (all elements are unique), this takes $O(N)$ space to store the keys and values
in the defaultdict.
"""


#using the built-in Counter class from the collections module is a more concise and efficient way to count the frequency of elements in an array. The Counter class automatically handles the counting and provides a dictionary-like object that maps elements to their counts. This simplifies the code and improves readability.

from collections import Counter
class Solution:
    def mostFreqEle(self, arr):
        # code here
        freq=Counter(arr)
        max_freq=float("-inf")
        max_key=float("-inf")
        for key in freq.keys():
            if freq[key]>max_freq:
                max_freq=freq[key]
                max_key=key
            elif freq[key]==max_freq:
                max_key=max(max_key,key)
        return max_key
            
#normal dictionary implementation
class Solution:
    def mostFreqEle(self, arr):
        # code here
        freq={}
        for i in arr:
            if i in freq:
                freq[i]+=1
            else:
                freq[i]=1
        max_freq=float("-inf")
        max_key=float("-inf")
        for key in freq.keys():
            if freq[key]>max_freq:
                max_freq=freq[key]
                max_key=key
            elif freq[key]==max_freq:
                max_key=max(max_key,key)
        return max_key
#overall time for all are same O(N) and space is O(U) where U is the number of unique elements in the array.
# worst case space complexity is O(N) when all elements are unique. u=N
            
            
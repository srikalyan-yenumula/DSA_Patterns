#i dont get brute . i directly done below one.[go dirctly to optimal]
"""Intuition:
Imagine you have a bag full of marbles, each with a different number. Your task is to find the marble that appears the second most number of times in the bag. To solve this, we need to keep track of the number of times each marble appears. We should identify the marble with the highest occurrence first and then look for the marble that comes next in terms of frequency. This way, we ensure that we correctly find the second highest occurring marble in the bag."""
class Solution:
    """Function to get the second highest 
    occurring element in array"""
    def secondMostFrequentElement(self, nums):
        
        # Variable to store the size of array
        n = len(nums)
        
        """Variable to store maximum frequency
        and second Max frequency"""
        maxFreq = 0
        secMaxFreq = 0
        
        """Variable to store elements with most 
        and second most frequency"""
        maxEle = -1
        secEle = -1
        
        # Visited array
        visited = [False] * n
        
        # First loop
        for i in range(n):
            # Skip second loop if already visited
            if visited[i]:
                continue
            
            """Variable to store frequency
            of current element"""
            freq = 0
            
            # Second loop
            for j in range(i, n):
                if nums[i] == nums[j]:
                    freq += 1
                    visited[j] = True
            
            """Update variables if new element  
            having highest frequency or second
            highest frequency is found"""
            if freq > maxFreq:
                secMaxFreq = maxFreq
                maxFreq = freq
                secEle = maxEle
                maxEle = nums[i]
            elif freq == maxFreq:
                maxEle = min(maxEle, nums[i])
            elif freq > secMaxFreq:
                secMaxFreq = freq
                secEle = nums[i]
            elif freq == secMaxFreq:
                secEle = min(secEle, nums[i])
        
        # Return the result
        return secEle

if __name__ == "__main__":
    nums = [4, 4, 5, 5, 6, 7]
    
    """Creating an instance of 
    Solution class"""
    sol = Solution()
    
    """Function call to get the second
    highest occurring element in array"""
    ans = sol.secondMostFrequentElement(nums)
    
    print(f"The second highest occurring element in the array is: {ans}")

# Complexity Analysis:
#Time Complexity: O(N2) (where N is the size of the array given) – Using two nested loops.

#Space Complexity: O(N) – Using a visited array of size N and a couple of variables.








#i thought about lets do in two loop later compress into single.
from collections import Counter
class Solution:
    def secondMostFrequentElement(self, nums):
        freq=Counter(nums)
        if len(nums)<=1:
            return -1
        max_key=max_freq=float("-inf")
        for k,f in freq.items():
            if f>max_freq:
                max_freq=f
                max_key=k
            elif f==max_freq:
                max_key=min(max_key,k)
        print(max_key,max_freq)
        sec_key=sec_freq=float("-inf")
        for k,f in freq.items():
            if f>sec_freq and f<max_freq:
                sec_freq=f
                sec_key=k
            elif f==sec_freq:
                sec_key=min(sec_key,k)
        if sec_key==float("-inf"): 
            return -1
        return sec_key


"""

Time Complexity: $O(N)$ where $N$ is the number of elements in the array. Building the Counter takes $O(N)$. 
Then, you loop through the unique keys in the dictionary twice. If $U$ is the number of unique elements, 
the loops take $O(2U)$ time, which drops the constant to become $O(U)$. Since $U \le N$, the overall time 
complexity is $O(N)$.
Space Complexity: $O(U)$ where $U$ is the number of unique elements. 
This is the memory required to store the frequencies in the Counter dictionary.
"""

#single pass
from collections import Counter
class Solution:
    def secondMostFrequentElement(self, nums):
        freq=Counter(nums)
        if len(nums)<=1:
            return -1
        max_key=max_freq=float("-inf")
        sec_key=sec_freq=float("-inf")
        for k,f in freq.items():
            if f>max_freq:
                sec_freq=max_freq
                sec_key=max_key
                max_freq=f
                max_key=k
            elif f==max_freq:
                max_key=min(max_key,k)
            elif f>sec_freq and f<max_freq:
                sec_freq=f
                sec_key=k
            elif f==sec_freq:
                sec_key=min(sec_key,k)
        print(max_key,max_freq)
        if sec_key==float("-inf"): 
            return -1
        return sec_key
"""
Time Complexity: $O(N)$ where $N$ is the number of elements. 
Building the Counter takes $O(N)$. Your single for loop now only iterates through the dictionary once, 
which takes $O(U)$ time (where $U$ is the number of unique elements). $O(N + U)$ simplifies to $O(N)$.
Space Complexity: $O(U)$ where $U$ is the number of unique elements, which is the memory required for the
Counter dictionary.

"""

#in worst case that U will be N when all elements are unique.


#using dict
from collections import defaultdict
class Solution:
    def secondMostFrequentElement(self, nums):
        freq=defaultdict(int)
        for i in nums:
            freq[i]+=1
        if len(nums)<=1:
            return -1
        max_key=max_freq=float("-inf")
        sec_key=sec_freq=float("-inf")
        for k,f in freq.items():
            if f>max_freq:
                sec_freq=max_freq
                sec_key=max_key
                max_freq=f
                max_key=k
            elif f==max_freq:
                max_key=min(max_key,k)
            elif f>sec_freq and f<max_freq:
                sec_freq=f
                sec_key=k
            elif f==sec_freq:
                sec_key=min(sec_key,k)
        print(max_key,max_freq)
        if sec_key==float("-inf"): 
            return -1
        return sec_key

        
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
Time Complexity: $O(N)$ where $N$ is the number of elements. Building the Counter takes $O(N)$. Your single for loop now only iterates through the dictionary once, which takes $O(U)$ time (where $U$ is the number of unique elements). $O(N + U)$ simplifies to $O(N)$.Space Complexity: $O(U)$ where $U$ is the number of unique elements, which is the memory required for the Counter dictionary.

"""

#in worst case that U will be N when all elements are unique.
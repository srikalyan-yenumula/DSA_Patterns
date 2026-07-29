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
            
            
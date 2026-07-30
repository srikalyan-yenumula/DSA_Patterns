# i directly done using hashing

#brute
"""
Intuition 
The naive way is to use nested loops to count the occurrences of each of the elements and if the count is greater than one third of the size of array, include the element in the answer."""
from typing import List

class Solution:
    # Function to find majority elements in an array
    def majorityElementTwo(self, nums: List[int]) -> List[int]:
        
        # Size of the array
        n = len(nums)
        
        # List of answers
        result = []
        
        for i in range(n):
            """ Checking if nums[i] is not 
            already part of the answer """
            if len(result) == 0 or result[0] != nums[i]:
                
                cnt = 0
                
                for j in range(n):
                    # counting the frequency of nums[i]
                    if nums[j] == nums[i]:
                        cnt += 1
                
                # check if frequency is greater than n/3
                if cnt > (n // 3):
                    result.append(nums[i])
                
            # if result size is equal to 2 break out of loop
            if len(result) == 2:
                break
        
        # return the majority elements
        return result

if __name__ == "__main__":
    arr = [11, 33, 33, 11, 33, 11]
    
    # Create an instance of Solution class
    sol = Solution()
    
    ans = sol.majorityElementTwo(arr)
    
    # Print the majority elements found
    print("The majority elements are:", end=" ")
    for it in ans:
        print(it, end=" ")
    print()

"""
Complexity Analysis 
Time Complexity: O(N2), where N is the size of the array. As for every element of the array the inner loop runs for N times.

Space Complexity: O(1) the space used is so small that it can be considered constant.

"""


#better ione is sort
#ele must be in 2 parts of array that is 1/3 ,2/3.
class Solution:
    def majorityElementTwo(self, nums):
        nums.sort()
        first=nums[len(nums)//3]
        second=nums[(2*len(nums))//3]
        res=[]
        if nums.count(first)>len(nums)//3:
            res.append(first)
        if first!=second and nums.count(second)>len(nums)//3:
            res.append(second)
        return res
        






from collections import Counter
class Solution:
    def majorityElementTwo(self, nums):
        freq=Counter(nums)
        res=[]
        for k in freq.keys():
            if freq[k]>len(nums)//3:
                res.append(k)
        return res



"""Time Complexity: $O(N)$Where $N$ is the total number of elements in the nums array.
Counter(nums): Python iterates through the array once to build the frequency dictionary.
 This takes $O(N)$ time.for k in freq.keys():: You loop through the unique numbers. 
 In the worst-case scenario (where every number in the array is different), this loop runs $N$ times.\
 So this takes $O(N)$ time.freq[k] > len(nums)//3: Dictionary lookups and appending to the list take $O(1)$ time.
 Combined, $O(N) + O(N)$ simplifies directly to $O(N)$ Time.
 Space Complexity: $O(N)$Where $N$ is the total number of elements.The freq dictionary: 
 In the worst-case scenario (e.g., [1, 2, 3, 4, 5, 6]), every single number is unique. 
 Your dictionary will have to store $N$ key-value pairs, taking up $O(N)$ Space.The res array
   (The Cool Mathematical Fact): How big can your result array get? Mathematically, it is impossible for 
   more than two elements to appear strictly more than $33.3\%$ ($N/3$) of the time! Because of this math rule,
your res array will never contain more than 2 elements. Therefore, the space for the result array is 
strictly $O(1)$.Overall, because the dictionary dictates the memory, your total space complexity is $O(N)$."""
#counting numbers/frequency of number using array
#only positive works
#SKIP IT
a=[2,1,4,3,2,1,3]
m=max(a) # o(N)
freq=[0]*(m+1) #o(M+1) When you do [0] * (m + 1), Python loops through and places a zero in M + 1 memory positions.
for i in a: # o(N)
    freq[i]+=1
print(freq)
"""Time: O(N+M)
    space: O(M)"""



#it works for both + & - . just learn this enough.

a=[1,2,2,9,-1,0,-4]
small=min(a)
big=max(a)
freq=[0]*(big-small+1)
for i in a:
    freq[i-small]+=1
print(freq)
for i in range(len(freq)):
    print(small+i,freq[i]) 

#only small alphabets.you do same way for big alphabets.
#SKIP IT
a=['a','z','g','s','s']
small=ord('a')
big=ord('z')
print(small,big)
freq=[0]*(big-small+1)
for i in a:
    freq[ord(i)-small]+=1
for i in range(len(freq)):
    print(chr(small+i),freq[i])


#together case. just learn this.
a=['a','n','J','O','l']
small=ord(min(a))
big=ord(max(a))
freq=[0]*(big-small+1)
for i in a:
    freq[ord(i)-small]+=1
print("together")
for i in range(len(freq)):
    print(chr(i+small),freq[i])

"""
Why You Can't Completely Ignore the Array Method
You need to keep the "Array Offset" technique in your back pocket for two specific scenarios:

1. The "No Hash Map" Constraint
Interviewers love to test if you rely too heavily on Python's built-in features. After you solve it with a dictionary, a classic follow-up question is:

"Good. Now, how would you solve this if you were writing in C and didn't have a hash map, or if I explicitly asked you to only use arrays?"

If you skipped learning the array method, you will freeze here.

2. Bounded Ranges (Counting Sort)
Sometimes the interviewer will give you a specific constraint:

"You have an array of 1 million integers, but you know the values only range from -50 to 50."

In this specific case, the Array Method is actually better than a Dictionary.

A Dictionary has to calculate a "hash" for every single number to figure out where to store it, which adds a tiny bit of processing time.

An Array lookup (freq[index]) is instant, raw memory access. Because the range is tiny (101 possible numbers), the memory waste is zero, making the array mathematically faster."""




#hahsing
"""
dict, defaultdict, and Counter each have specific scenarios where they shine. Since Counter is actually just a specialized version of a dictionary, it helps to understand exactly what it adds.

Here is the breakdown of when to use which.

1. collections.Counter
When to use: Whenever you have a complete list of items upfront, or you need to do math on frequencies.

Counter is heavily optimized in C under the hood, making it the fastest and cleanest way to count an existing list. It also has "superpowers" that standard dictionaries lack.

Bulk Counting: You don't need a for loop. Just pass the array.

Finding the "Top N": It has a built-in .most_common() method.

Math Operations: You can add or subtract two Counters together.

Python"""
from collections import Counter

a = [1, 2, 2, 9, -1, 0, -4, 2, 1]

# 1. Count everything instantly
freq = Counter(a) 

# 2. Get the top 2 most frequent numbers
print(freq.most_common(2)) 
# Output: [(2, 3), (1, 2)]
"""
2. Standard Dictionary (dict)
When to use: General data mapping (e.g., pairing a user ID to a name), or when you are strictly forbidden from importing modules in an interview.

Standard dictionaries are not built specifically for counting. If you try to add 1 to a key that doesn't exist yet, Python throws a KeyError. This is why you always have to write that clunky if/else check.

Python"""
freq = {}
for i in a:
    if i in freq:
        freq[i] += 1
    else:
        freq[i] = 1 # Handling the KeyError
"""
3. collections.defaultdict(int) (The Middle Ground)
When to use: When you are building frequencies dynamically inside a complex loop (like traversing a tree or graph) and you don't have the whole list upfront to pass to Counter.

A defaultdict solves the KeyError problem of a standard dictionary. If you ask for a key that doesn't exist, it automatically creates it and assigns it a default value of 0 (because of the int).

Python"""
from collections import defaultdict

freq = defaultdict(int)

# No if/else needed. If 'i' doesn't exist, it starts at 0 automatically.
for i in a:
    freq[i] += 1
#Sort by frequency 
freq = {'a': 5, 'b': 2, 'c': 2}

# Sort descending by frequency (values)
sorted_items = sorted(freq.items(), key=lambda x: x[1], reverse=True)
print(sorted_items, "reverse is used")

"""Why it works (The Intuition)
freq.items(): This converts the dictionary into a list of tuples: [('a', 5), ('b', 2), ('c', 8)].

key=lambda x:: Think of x as a single tuple passing through a conveyor belt. x is ('a', 5).

x[1]: You are telling Python, "Look at index 1 of the tuple." Index 0 is the key ('a'), and index 1 is the value (5). This tells Python to sort by the frequencies.

reverse=True: This puts the biggest numbers at the front (descending order), which is exactly what you want for "most frequent" problems.

#simply use x[i] for small to big and -x[i] for bug to small and remove the reverse totally.
#like """

sorted_items = sorted(freq.items(), key=lambda x: x[1])

print(sorted_items,"no reversed")
sorted_items = sorted(freq.items(), key=lambda x: -x[1],)

print(sorted_items,"no reversed but used -")



#Sort by frequency descending, but if there's a tie, sort alphabetically ascending
freq = {'a': 5, 'c': 5, 'b': 8}

# Sort highest frequency first, but ties go alphabetically (a -> z)
sorted_items = sorted(freq.items(), key=lambda x: (-x[1], x[0]))

print(sorted_items) 
# Output: [('b', 8), ('a', 5), ('c', 5)]



#see this table
"""
Here is your ultimate reference guide for every possible sorting combination.

Because we use the minus sign (`-`) to flip sorting directions on the fly, **Numbers** and **Characters** require slightly different strategies.

## 1. When Keys are Numbers

Numbers are easy because you can use the minus sign on both the frequency (`x[1]`) and the key (`x[0]`).

**The Rule:** Add a `-` to whatever you want to sort **Descending (Big to Small)**.

| Goal | Syntax |
| --- | --- |
| **Freq ASC, Key ASC** | `key=lambda x: (x[1], x[0])` |
| **Freq ASC, Key DESC** | `key=lambda x: (x[1], -x[0])` |
| **Freq DESC, Key ASC** | `key=lambda x: (-x[1], x[0])` |
| **Freq DESC, Key DESC** | `key=lambda x: (-x[1], -x[0])` |

---

## 2. When Keys are Characters / Strings

You cannot put a minus sign in front of a string. To sort strings **Descending (Z to A)**, you must use `reverse=True`.

**The Rule:** If you need the string to be Descending, use `reverse=True` at the end. Because `reverse=True` flips the *entire* list, it will also accidentally flip your frequencies. To fix this, put a minus sign on the frequency to "cancel out" the reverse!

| Goal | Syntax | How the trick works |
| --- | --- | --- |
| **Freq ASC, Key ASC** | `key=lambda x: (x[1], x[0])` | Standard sorting. No tricks needed. |
| **Freq ASC, Key DESC** | `key=lambda x: (-x[1], x[0]), reverse=True` | `reverse` flips both. `-x[1]` cancels the frequency flip so it stays ASC. |
| **Freq DESC, Key ASC** | `key=lambda x: (-x[1], x[0])` | The minus sign safely flips only the frequencies. |
| **Freq DESC, Key DESC** | `key=lambda x: (x[1], x[0]), reverse=True` | `reverse` flips both exactly the way you want. |

---

### A Quick Code Example to Prove the Trickiest One

The hardest combo to wrap your head around is **Freq ASC, String Key DESC** (Smallest frequencies first, but ties go Z to A). Here is proof of the double-negative trick at work:

```python
freq = {'a': 5, 'z': 5, 'b': 10}

# We want Freq ASC (5, then 10), but Key DESC ('z' before 'a')
# We use the double-negative trick: minus sign on freq + reverse=True
sorted_items = sorted(freq.items(), key=lambda x: (-x[1], x[0]), reverse=True)

print(sorted_items)
# Output: [('z', 5), ('a', 5), ('b', 10)]

```"""


#my solution is this one. i dont thought any other then this
from collections import Counter
class Solution:
    def frequencySort(self, s):
        #your code goes here
        freq=Counter(s)
        freq=sorted(freq.items(),key=lambda x:(-x[1],x[0]))
        print(freq)
        return "".join(i for i,_ in freq)
"""


Here is the exact breakdown of your Time and Space complexities.

### Time Complexity: $O(N + U \log U)$

Where $N$ is the length of the string `s`, and $U$ is the number of **unique** characters in the string.

Here is the line-by-line breakdown:

1. **`Counter(s)`:** Scans every character in the string once. This takes **$O(N)$** time.
2. **`sorted(...)`:** You are sorting the unique characters (not the whole string). Sorting a list of size $U$ takes **$O(U \log U)$** time.
3. **`"".join(...)`:** Iterating through the sorted tuples to build the final result takes **$O(U)$** time.

Combined, that gives $O(N + U \log U + U)$, which simplifies to **$O(N + U \log U)$**.

### Space Complexity: $O(U)$

1. **`Counter(s)`:** The dictionary stores up to $U$ unique characters and their counts.
2. **`sorted(...)`:** Python’s `sorted()` creates a new list in memory containing the $U$ tuples.
3. **`"".join(...)`:** The final string (or list) you return contains exactly $U$ characters.

Everything scales with the number of unique characters, so the total extra space required is **$O(U)$**.

---

### The "Interview Secret" for String Problems

If an interviewer asks you for the complexities of this specific code, you should give them the answers above first. But then, you can drop a major knowledge flex:

Because the problem uses **characters** (not infinitely large numbers), $U$ has a hard limit.

* If the string only contains lowercase English letters, $U$ can never be larger than 26.
* Even if it includes every standard ASCII character, $U$ is capped at 128 (or 256).

Because $U$ is technically a constant bounded by the alphabet size:

* **$U \log U$ becomes $128 \log 128$, which is just a constant $O(1)$.**
* **The space $O(U)$ becomes $O(128)$, which is also $O(1)$.**

**What you say in the interview:**

> *"The time complexity is $O(N + U \log U)$ and space is $O(U)$ based on the unique characters. However, if our character set is fixed (like standard ASCII), $U$ maxes out at 128. In that real-world scenario, the time complexity simplifies to $O(N)$ and the space complexity simplifies to $O(1)$ because the dictionary and sorting operations have a strict, constant upper limit."*"""



#no hashmap
class Solution:
    def frequencySort(self, s):
        #your code goes here
        max_val=ord(max(s))
        min_val=ord(min(s))
        print(max_val,min_val)
        freq=[0]*(max_val-min_val+1)
        for v in s:
            freq[ord(v)-min_val]+=1
        res=[]
        for i in range(len(freq)):
            if freq[i]>0:
                char=chr(i+min_val)
                f=freq[i]
                res.append((char,f))
        sort=sorted(res,key=lambda x:(-x[1],x[0]))
        return "".join(i for i,_ in sort)
""""


Here is the exact Time and Space complexity breakdown for **your specific array version** (the memory-optimized one using `min` and `max`).

To be incredibly precise, we need to define three variables:

* **$N$** = The length of the string `s`.
* **$K$** = The range between your min and max characters (`max_val - min_val + 1`).
* **$U$** = The number of unique characters in the string.

### Time Complexity: $O(N + K + U \log U)$

Here is the line-by-line breakdown of where your CPU spends its time:

1. **`min(s)` and `max(s)`:** Two passes through the string. **$O(N)$**
2. **`[0] * (max_val - min_val + 1)`:** Python creates an array of size $K$. **$O(K)$**
3. **`for v in s:`:** One pass to count frequencies. **$O(N)$**
4. **`for i in range(len(freq)):`:** One pass through your custom array. **$O(K)$**
5. **`sorted(res, ...)`:** Sorting the unique characters. **$O(U \log U)$**
6. **`"".join(...)`:** Reconstructing the result. **$O(U)$**

When you add it all up and drop the smaller constants, you get **$O(N + K + U \log U)$**.

### Space Complexity: $O(K)$

Here is where your code allocates memory:

1. **`freq = [0] * K`:** Your perfectly sized array takes **$O(K)$** space.
2. **`res = []`:** This stores tuples for the unique characters, taking **$O(U)$** space.
3. **`sort = sorted(...)`:** Python creates a new sorted list of size **$O(U)$**.

Since $K$ (the range of characters) will always be greater than or equal to $U$ (the number of unique characters), the $U$ gets absorbed. Your total space complexity is **$O(K)$**.

---

### The Real-World "Interview" Simplification

In a real interview, if they ask for the complexities of your code, you should give them the exact formulas above, but then apply the **"Real World Bounding"** rule.

Because characters are mapped to ASCII values, $K$ and $U$ have strict limits. If the string contains standard characters (uppercase, lowercase, numbers, symbols), $K$ will never exceed 128, and $U$ will never exceed 128.

**Because 128 is a constant number, your complexities simplify beautifully:**

* **Time Complexity simplifies to $O(N)$** (Because $K$ and $U \log U$ become fixed, tiny constants that don't grow as the string gets infinitely long).
* **Space Complexity simplifies to $O(1)$** (Because your array will never grow larger than 128 items, even if the string has a billion characters).

**Your solution achieves the holy grail:** $O(N)$ Time and $O(1)$ Space."""
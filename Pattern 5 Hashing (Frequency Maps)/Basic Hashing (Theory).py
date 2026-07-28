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
    space: O(M)
    
    You might want to add a note that if the array is [1, 1000000], 
    $M$ is one million, meaning you allocate 1,000,000 memory slots for just two numbers. 
    This perfectly sets up your later argument for why dictionaries are better for sparse, unpredictable data.
    """



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
#space is constant. because we are using only 52 alphabets. so space is O(1)
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


#mixied
"""
If an interviewer gives you a list like a = [1, 'Z', -4, 'a', 2], it is actually a trap. They are testing to see if you know when to abandon the array method.

Here is why the array method breaks down here, and what you should do instead.

Why the Array Method Fails Here
1. Python will crash on min() and max()
In Python 3, you cannot use greater-than or less-than operators between integers and strings. If you try to run min([1, 'a']), Python instantly throws a TypeError. You can't find the range to build your array.

2. Memory Mapping is a Nightmare
Even if you converted the numbers to strings, how do you map the number -4 and the letter a into the same continuous array of zeros? You would have to write massive, complicated if/else statements to separate the integers from the characters, calculate two different offsets, and manage two different arrays. It defeats the entire purpose of the technique.

The Solution: This is Dictionary Territory
When data types are mixed, or when the distance between values is totally unpredictable, you must use a Hash Map (a Dictionary or Counter).

Dictionaries don't use a continuous block of memory like arrays do. They use a hashing algorithm. Python can instantly hash an integer (-4) and a string ('a') and store them side-by-side with zero issues and zero wasted memory.

"""










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

#time for add and remove in dict,defaultdict and counter
""" Python (dict, defaultdict, Counter)Worst Case: $O(N)$ for both Add and Remove. Python uses a 
strategy called Open Addressing. When you add a key, Python computes a hash to find a memory slot.
If that slot is already taken by a different key (a collision), Python uses a mathematical formula
 to "probe" (jump) to the next available empty slot.The Worst Case: If you insert a key, and a 
 massive number of keys have already collided and filled up the probed slots, Python might have to
   scan through the entire dictionary linearly to find an empty space to add the new key, or to 
   find the key you want to remove. This scanning takes $O(N)$ time."""

#hashtable working in python
"""Here is a complete, interview-ready cheat sheet on how Python dictionaries (Hash Tables) calculate indexes,
 resolve collisions, and manage memory.

---

## 1. The Core Architecture (Python vs. Textbooks)

Most textbooks teach Hash Tables using prime numbers and Linked Lists. Python does **not** do this.

* **No Linked Lists:** Python uses **Open Addressing** (arrays only).
* **No Prime Numbers:** Python sizes its arrays in **powers of 2** (8, 16, 32, 64...).
* **No Modulo (`%`):** Python uses **Bitwise AND (`&`)** for speed.

---

## 2. Step-by-Step: How Python Calculates the Index

When you write `my_dict["apple"] = 10`, here is the exact math Python executes:

**Step 1: Hash Generation**
Python generates a massive integer hash using an algorithm (currently SipHash for strings).

* *Example Hash:* `8123984712984124`

**Step 2: Bitwise Masking (Finding the index)**
Because division (`%`) is slow on CPUs, Python uses the dictionary's size to create a bitwise mask.
 The formula is `hash & (size - 1)`.

* If the dict size is 8, the mask is 7 (binary `111`).
* `8123984712984124 & 7 = 4`
* The key "apple" attempts to go to **Index 4**.

---

## 3. Resolving Collisions: Open Addressing

If Index 4 is already taken by a different key, a collision occurs. Python does not create a Linked List (like Java does). Instead, it uses **Probing** to jump to a new slot.

Python's jumping formula is not a simple linear step (e.g., just checking index 5, then 6). 
It uses a mathematical equation called a **Perturbation Sequence**:

`next_index = (5 * current_index + 1 + perturb) & (size - 1)`

* `perturb` is derived from the remaining bits of the original hash.
* This creates a pseudo-random jumping pattern that scatters keys evenly across the array,
 preventing "clustering" (where a bunch of keys get stuck next to each other).

---

## 4. Time and Space Complexity

| Operation | Average Case | Worst Case | Why? |
| --- | --- | --- | --- |
| **Search / Lookup** | $O(1)$ | $O(N)$ | $O(N)$ only happens if massive collisions force Python to probe the entire array. |
| **Insert / Add** | $O(1)$ | $O(N)$ | Same as above. |
| **Delete / Remove** | $O(1)$ | $O(N)$ | Deletion leaves a "dummy" flag so probing chains aren't broken. |
| **Space** | $O(N)$ | $O(N)$ | Uses contiguous array memory. |

---

## 5. Resizing Memory (The Load Factor)

To prevent the dictionary from filling up (which would guarantee $O(N)$ worst cases), Python resizes the array *before* it gets full.

* **The Threshold:** Python resizes when the dictionary is **2/3 full (66%)**.
* **The Resize Event:** It allocates a new block of memory that is **twice the size** (maintaining the power of 2 rule) and recalculates the index for every single key to move them over.
* **The Complexity:** The resize event itself takes **$O(N)$ time**, but because it happens so rarely, the *amortized* (average) insertion time remains **$O(1)$**.

---

## 6. Security: The DoS Protection (Python 3.3+)

If a hacker knows how Python calculates hashes, they could intentionally send your server millions of keys 
that all hash to Index 4. This would force your Python server into a permanent $O(N)$ worst-case loop,
 freezing the server (a Denial of Service attack).

**The Fix:** Python adds a random "salt" (a secret random number) to the hash algorithm every time you 
start Python. This means the hash for `"apple"` is completely different every single time you run your script, 
making collision attacks impossible."""



#"How does a Hash Table resolve collisions?"
"""Step 1: Give the Textbook Answer (Passes the basic test)
Start by giving them exactly what they expect from their rubric.

"In theory, the standard way to build a hash table is to use an array sized to a large prime number. You find the index using modulo division (hash % prime). If a collision happens, the textbook approach is Separate Chaining, where you store a Linked List at that index to hold multiple values."

Step 2: Give the Python/Real-World Answer (Gets you the job)
Immediately follow up with this to show you are a senior-level thinker.

"However, since my primary language is Python, I know that under the hood, Python completely abandons that textbook method for performance reasons.

Modulo division is too slow on the CPU, so Python sizes the array in powers of 2 [size-1 inplace of primes]
and uses a bitwise AND mask to find the index. Also, jumping around Linked Lists ruins CPU caching, 
so Python doesn't use chaining. Instead, it uses Open Addressing with a mathematical probing sequence 
to find the next empty slot in the array. it use seed for DoS Protection.{normally we use prime to avoid hack but we not use them for speed. so seed take care of it.} 
The ALGO is SIPHASH. It is a cryptographic hash function that is designed to be fast and secure. It is used in Python to generate hash values for strings and other data types. The use of a cryptographic hash function makes it difficult for an attacker to predict the hash values of different inputs, which helps to prevent hash collision attacks."""




"""
#SIPHASH: The Secret Weapon Against HashDoS Attacks



To truly understand SipHash and the HashDoS vulnerability, we have to look at the exact mechanics of how a hash table collapses under pressure, and how SipHash was specifically engineered to stop it.

Here is the detailed breakdown of the attack, the algorithm, and its industry adoption.

## 1. Anatomy of a HashDoS Attack

Before 2012, most programming languages used fast, predictable algorithms (like MurmurHash or CityHash) for their internal hash tables. These algorithms were "un-keyed" — meaning the word "apple" would generate the exact same hash on every computer in the world.

Because the math was public, hackers could write a script on their laptop to reverse-engineer the math. They would generate hundreds of thousands of random, bizarre strings (like `"EzG2"`, `"FzF1"`, `"GyE2"`) that mathematically guaranteed a **collision** at the exact same array index.

Here is what happens when a web server receives a JSON payload containing 100,000 of these malicious keys:

1. **The First Key:** The server hashes the first key, gets Index 4, and inserts it. Takes $O(1)$ time (about 10 nanoseconds).
2. **The Second Key:** The server hashes the second key, gets Index 4. It's full. The server has to probe (jump) to find the next empty slot. Takes slightly longer.
3. **The 10,000th Key:** The server hashes the key, gets Index 4. It then has to jump through 9,999 already-filled slots just to find an empty space.
4. **The 100,000th Key:** The server has to jump 99,999 times to insert a single item.

Because every single insertion requires scanning through all previous insertions, the time complexity degrades from linear to **quadratic ($O(N^2)$)**.

A 1-Megabyte JSON payload that normally takes 0.001 seconds to parse suddenly forces the CPU to perform **5 billion probing operations**. The server's CPU spikes to 100%, it stops responding to legitimate traffic, and the application goes offline.

---

## 2. The Fix: How SipHash Works

In 2012, cryptographers Jean-Philippe Aumasson and Daniel J. Bernstein invented **SipHash** to solve this exact problem.

They needed an algorithm that was cryptographically strong (so hackers couldn't predict the collisions) but incredibly fast (so dictionaries wouldn't slow down the language).

Here is how SipHash achieves both:

### The Secret Seed (The Key)

SipHash is a **Pseudo-Random Function (PRF)**. Unlike older algorithms, SipHash requires a 128-bit secret key. When a Python (or Rust/Ruby) process starts, the operating system gives it a random chunk of memory to act as this secret seed. Every hash calculated during that session is mixed with this secret key. Because the attacker doesn't know the key, they cannot pre-calculate collisions.

### The ARX Architecture

Cryptographic algorithms like SHA-256 are slow because they do complex, heavy math. SipHash gets its speed by using an **ARX architecture**, which stands for:

* **Addition** (`+`)
* **Rotation** (shifting bits left or right)
* **XOR** (`^` - exclusive OR)

These three operations are physically built into the silicon of modern CPUs. They execute in a single clock cycle. SipHash takes your string (like "apple"), breaks it into chunks, mixes it with the secret 128-bit key, and then rapidly Adds, Rotates, and XORs the bits together.

### "SipHash-2-4"

You will often see it written as SipHash-2-4. This refers to the number of "mixing rounds" it performs.

* It does **2 compression rounds** for every chunk of the string you feed it.
* It does **4 finalization rounds** at the very end to scramble the final integer.
This provides the perfect balance: it is mathematically complex enough to prevent patterns, but short enough to execute in nanoseconds.

---

## 3. Where SipHash is Used Today

SipHash was so successful that it fundamentally changed how systems programming is done. It is now the invisible backbone of the internet.

### Programming Languages (Hash Tables)

* **Python:** Uses SipHash for all string keys in dictionaries `dict()` and `set()`.
* **Rust:** Uses SipHash-1-3 (a slightly faster variant) as the default algorithm for `std::collections::HashMap`.
* **Ruby:** Uses SipHash internally for all `Hash` objects to prevent HashDoS on Ruby on Rails web servers.

### In-Memory Databases

* **Redis:** The world's most widely used caching database relies on hash tables. Redis switched to SipHash to ensure that an attacker couldn't freeze a Redis cluster by flooding it with predictable keys.

### Operating Systems & Networking

This is perhaps its most critical use case. Operating systems use hash tables to track network traffic (e.g., routing tables, TCP connections).

* **Linux and FreeBSD:** Use SipHash inside their networking kernels. If they didn't, an attacker could send millions of "spoofed" IP packets designed to collide in the OS's routing table, crashing the entire server at the operating system level before your application even sees the traffic.
* **WireGuard:** The modern VPN protocol uses SipHash extensively for securely and rapidly mapping network addresses to encryption keys.

> **Key takeaway:** If you are building an application where a user can supply arbitrary strings that end up as keys in a dictionary or database, you must use a randomized, keyed algorithm like SipHash. If you use a fast, predictable algorithm, you are leaving your servers wide open to a single-laptop takedown."""

#realworld examples
"""To give you a real sense of its footprint, SipHash is quietly powering the backbone of modern computing. It is the invisible shield protecting everything from your web browser to the global Bitcoin network.

Here are some of the most critical, real-world technologies that rely on SipHash right now, and exactly *why* they use it.

---

## 1. Google Chrome & Node.js (V8 Engine)

**The Tech:** The V8 JavaScript engine powers both the Google Chrome web browser and the Node.js backend framework.
**How it uses SipHash:** V8 uses it to hash keys for JavaScript objects and `Map` data structures.
**Why it needs it:**
If you build a backend API using Node.js/Express, your server is constantly parsing incoming JSON payloads from users. If Node.js used a weak hash function, a hacker could send a 1MB JSON file filled with colliding keys. Your Node.js server would freeze, bringing down your entire web application. By using SipHash, Node.js guarantees that bad actors cannot predictably crash your servers just by sending a crafted JSON payload.

## 2. Apple's iOS & macOS (Swift)

**The Tech:** Swift is the primary programming language used to build apps for iPhones, iPads, and Mac computers.
**How it uses SipHash:** Swift uses SipHash-1-3 as the default algorithm for its standard `Hasher` API. Every time an iOS developer uses a `Dictionary` or a `Set`, SipHash is running under the hood.
**Why it needs it:**
Mobile devices have limited battery and CPU power. If an iOS app fetches a malicious JSON feed from the internet, a HashDoS attack could cause the app to freeze, spike the iPhone's CPU to 100%, and drain the battery in minutes. SipHash prevents this while being fast enough not to drain battery life during normal operations.

## 3. Bitcoin Core

**The Tech:** The foundational software that runs the Bitcoin network.
**How it uses SipHash:** While Bitcoin famously uses SHA-256 for *mining* and verifying the blockchain, it uses SipHash to manage its internal network of peers and short transaction IDs.
**Why it needs it:**
Bitcoin operates on a Peer-to-Peer (P2P) network. Nodes (servers running Bitcoin) constantly share information about new transactions with each other. A hacker might try to flood a Bitcoin node with thousands of fake, unconfirmed transactions. If Bitcoin used a weak hash function to store these in its memory cache, the node's memory would lock up, and it would drop off the network. SipHash prevents attackers from blinding individual Bitcoin nodes.

## 4. WireGuard VPN

**The Tech:** WireGuard is the modern, ultra-fast VPN protocol built directly into the Linux kernel, used by millions of privacy-conscious users and companies.
**How it uses SipHash:** It uses it to map incoming network packets and IP addresses to active encrypted connections.
**Why it needs it:**
A VPN server sits on the open internet, getting bombarded by billions of packets. WireGuard needs to instantly know, "Does this packet belong to User A or User B?" It uses hash tables to route this traffic instantly. If an attacker sent millions of spoofed, specifically-crafted IP packets to the VPN server, they could cause collisions in the routing table. SipHash ensures the VPN server can route traffic at blazing speeds without being vulnerable to a packet-based HashDoS attack.

## 5. Systemd (Linux OS)

**The Tech:** Systemd is the core initialization system for almost all modern Linux servers (Ubuntu, Debian, CentOS). It manages how the OS boots up and how services (like web servers and databases) run.
**How it uses SipHash:** Systemd uses it for internal state tracking and for `systemd-journald` (the Linux logging system).
**Why it needs it:**
Imagine you run a massive cloud server. If a malicious local user, or an infected application, starts spamming the system logs with millions of perfectly crafted, colliding log entries, they could crash the entire operating system's logging daemon. SipHash ensures the OS kernel remains stable no matter what data is thrown at it.

## 6. Cisco's OpenDNS

**The Tech:** OpenDNS resolves domain names (like `google.com`) into IP addresses. It handles over 100 billion DNS requests daily.
**How it uses SipHash:** They use it to safely map requested domain names to their cached IP addresses.
**Why it needs it:**
DNS providers are the #1 target for DDoS attacks. If an attacker figures out how OpenDNS's internal cache works, they could ask to resolve millions of bizarre, randomly generated subdomains that mathematically collide in OpenDNS's servers. By using SipHash, Cisco ensures that no matter what domains an attacker requests, the DNS servers will always process them in instant $O(1)$ time.

---

### The Big Picture

The rule is simple: **If a system accepts unpredictable data from the open internet, 
and puts that data into a hash table in its RAM, it uses SipHash.**

Before SipHash was invented in 2012, all of these systems were theoretically vulnerable. Today, it is the unsung hero keeping the internet's memory safe from collapse."""




"""If you are building an API in Node.js, Python, Ruby, or Rust, the language's core engine 
(like Google's V8 engine for Node.js/Chrome) does this heavy lifting for you automatically. 
When you simply type const user = {} or new Map() in JavaScript, V8 is already generating the
random seed and running the collision protection under the hood.You get the armor for free.
However,you cannot just say, "V8 handles it, so my server is 100% safe." There are three critical reasons
why you, as the developer, still need to be deeply aware of how this works.

1. The Engines Still Make Mistakes (The 2026 Vulnerability)Even the brightest engineers at Google and Node.js 
make mistakes with hash tables. In fact, earlier this year, a massive HashDoS vulnerability (CVE-2026-21717)
was discovered right inside the V8 engine.V8's SipHash protection was working perfectly for normal words. 
But to speed things up, V8 tried a shortcut: if a string looked like an integer (e.g., "1000", "42"),
V8 skipped the randomized hash and just used the number itself as the hash index.Hackers realized this
and started sending massive JSON payloads full of integer-like strings that completely bypassed V8's 
security, recreating the exact $O(N^2)$ HashDoS attack we talked about.Your takeaway: You must constantly 
keep your Node.js runtime updated. If you are running an outdated, End-of-Life version of Node.js, 
V8's internal armor might have a known crack."""
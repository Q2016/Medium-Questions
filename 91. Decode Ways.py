Question:
A message containing letters from A-Z can be encoded into numbers using the following mapping:
'A' -> "1"
'B' -> "2"
...
'Z' -> "26"
To decode an encoded message, all the digits must be grouped then mapped back into letters using the reverse of the mapping above 
(there may be multiple ways). For example, "11106" can be mapped into:
"AAJF" with the grouping (1 1 10 6)
"KJF" with the grouping (11 10 6)
Note that the grouping (1 11 06) is invalid because "06" cannot be mapped into 'F' since "6" is different from "06".
Given a string s containing only digits, return the number of ways to decode it.
The test cases are generated so that the answer fits in a 32-bit integer.

Example 1:
Input: s = "12"
Output: 2
Explanation: "12" could be decoded as "AB" (1 2) or "L" (12).	

	
	
	
	
	
	
	
	
	
	
Solution: DFS

Method 1: (with figures in the link)

https://leetcode.com/problems/decode-ways/discuss/608268/Python-Thinking-process-diagram-(DP-%2B-DFS)
	
First, I build a tree of possible decodings I can do from a random string.

The number of leaves in the tree essentially is the number of ways the string can be decoded.
We are going to build our tree with DFS from our original string, trying to decode either as:
	-A single digit (and call dfs again with remaining string)
	-Both single digit and double digit, when the double digits are less than or equal to 26 (and call dfs again with remaining strings).
Our base case is when we have only a single digit left in our string or when we have nothing left in the string. In that case, we return 1 
back up the recursion stack.

Growing a tree
<image>

Dyanmic Programming

We can see that this type of tree has a lot of redundant sub-trees. Dynamic Programming to the rescue!! (In my code, I use lru_cache 
decorator which essentially memoizes the function calls with argument-returned value pairs. So, when I call the same function with same arguements, 
and if that recursive call has been made before, it is just retrieved from memoized pair).

<image>

After you have got a hang of the thinking process, we will have to handle issues with zeros.
Zeros can be in the middle or at the start.
	If it is at the start, there is no way to decode the string.
	If it is in the middle:
		If it can be paired with the digit before zero (and is less than or equal to 26, then we can keep on growing our subtrees)
		If it cannot be paired with the digit before zero, we have to destory that subtree. This might even render the whole string undecodable.

		
class Solution:
    def numDecodings(self, s:str) -> int:
        if len(s) == 0 or s is None:
            return 0

        @lru_cache(maxsize=None) # decorator which essentially memoizes the function calls with argument-returned value pairs (explained above)
        def dfs(string):
            if len(string)>0:
                if string[0] == '0':
                    return 0
            if string == "" or len(string) == 1:
                return 1
            if int(string[0:2]) <= 26:
                first = dfs(string[1:])
                second = dfs(string[2:])
                return first+second
            else:
                return dfs(string[1:])

        result_sum = dfs(s)

        return result_sum	


Complexity

Time: O(N), where N <= 100 is length of string s.
Space: O(N)


Second method:

Problem Reduction: variation of n-th staircase with n = [1, 2] steps.
Approach: We generate a bottom up DP table.
The tricky part is handling the corner cases (e.g. s = "30").
Most elegant way to deal with those error/corner cases, is to allocate an extra space, dp[0].
Let dp[ i ] = the number of ways to parse the string s[1: i + 1]

For example:
s = "231"
index 0: extra base offset. dp[0] = 1
index 1: # of ways to parse "2" => dp[1] = 1
index 2: # of ways to parse "23" => "2" and "23", dp[2] = 2
index 3: # of ways to parse "231" => "2 3 1" and "23 1" => dp[3] = 2

def numDecodings(s): 
	if not s:
		return 0

	dp = [0 for x in range(len(s) + 1)] 
	
	# base case initialization
	dp[0] = 1 
	dp[1] = 0 if s[0] == "0" else 1   #(1)

	for i in range(2, len(s) + 1): 
		# One step jump
		if 0 < int(s[i-1:i]) <= 9:    #(2)
			dp[i] += dp[i - 1]
		# Two step jump
		if 10 <= int(s[i-2:i]) <= 26: #(3)
			dp[i] += dp[i - 2]
	return dp[len(s)]


Notes of Wisdom:
(1): Handling s starting with '0'. Alternative: I would recommend treating as an error condition and immediately returning 0. It's easier to 
keep track and it's an optimization.
(2) (3): Pay close attention to your comparators. For (1) you want 0 <, not 0 <= . For (2) you want 10 <=, not 10 <


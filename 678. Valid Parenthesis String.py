Question:
Given a string s containing only three types of characters: '(', ')' and '*', return true if s is valid.
The following rules define a valid string:
Any left parenthesis '(' must have a corresponding right parenthesis ')'.
Any right parenthesis ')' must have a corresponding left parenthesis '('.
Left parenthesis '(' must go before the corresponding right parenthesis ')'.
'*' could be treated as a single right parenthesis ')' or a single left parenthesis '(' or an empty string "".
 
Example 1:
Input: s = "(*))", Output: true  

  
  
  
  
  
  
The link is not good but it points out some interesting examples like s=(*)(  
  
Solution: Greedy
 
 https://www.youtube.com/watch?v=QhPdNS143Qg

When checking whether the string is valid, we only cared about the "balance": the number of extra, open left brackets as we parsed through 
the string. For example, when checking whether '(()())' is valid, we had a balance of 1, 2, 1, 2, 1, 0 as we parse through the string: 
'(' has 1 left bracket, '((' has 2, '(()' has 1, and so on. This means that after parsing the first i symbols, (which may include asterisks,) 
we only need to keep track of what the balance could be. For example, if we have string '(***)', then as we parse each symbol, the set of possible 
values for the balance is [1] for '('; [0, 1, 2] for '(*'; [0, 1, 2, 3] for '(**'; [0, 1, 2, 3, 4] for '(***', and [0, 1, 2, 3] for '(***)'.
Furthermore, we can prove these states always form a contiguous interval. Thus, we only need to know the left and right bounds of this interval. 
That is, we would keep those intermediate states described above as [lo, hi] = [1, 1], [0, 2], [0, 3], [0, 4], [0, 3].
Let lo, hi respectively be the smallest and largest possible number of open left brackets after processing the current character in the string.
If we encounter a left bracket (c == '('), then lo++, otherwise we could write a right bracket, so lo--. If we encounter what can be a left bracket 
(c != ')'), then hi++, otherwise we must write a right bracket, so hi--. If hi < 0, then the current prefix can't be made valid no matter 
what our choices are. Also, we can never have less than 0 open left brackets. At the end, we should check that we can have exactly 0 open left brackets.

    def checkValidString(self, s):
        lo = hi = 0
        for c in s:
            lo += 1 if c == '(' else -1
            hi += 1 if c != ')' else -1
            if hi < 0: break
            lo = max(lo, 0)

        return lo == 0

 Example:
 s=(*)(  
 lo=1 hi=-1, lo=0 hi=-2, lo=-1 hi=-1, lo=0 hi=-2 
       
Complexity Analysis
Time Complexity: O(N), where NN is the length of the string. We iterate through the string once.
Space Complexity: O(1), the space used by our lo and hi pointers. However, creating a new character array will take O(N) space.      

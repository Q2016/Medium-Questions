Question:
Given two strings s and t, determine if they are both one edit distance apart. 
There are 3 possiblities to satisify one edit distance apart:
-Insert a character into s to get t -Delete a character from s to get t -Replace a character of s to get t

Example 1:
Input: s = "ab", t = "acb"
Output: true
Explanation: We can insert 'c' into s to get t.


Solution: ---
     
First We need to confirm that if case senstive matters, if blank space included. Then if two strings are equal or both empty 
we return false; if one string’s length is more than 1 unit longer than the other one’s length we return false. At last, 
Compare two strings (s, t) have three conditions. -Two strings length are equal. We only need to focus on the replacement edit. 
Since order matters, we can iterate both string based on same index, if the different character are more than 1 then 
return false else return true. -Two strings length are not equal. We only focus on add or delete. We iterate the shorter length string, 
if the current characters in same index of both string are different then we kown the current character should be the one need to add or
delete. So we just have to make sure the rest characters of both strings have to be same, otherwise there are more than 1 edit. 
In fact, since order matters, we do not have to compare the whole rest string, we only need to confirm if next character of longer string 
is equal to the current character of short string. If they are different then we return false.


def isOneEditDistance(self, s: str, t: str) -> bool:
     s_size = len(s)
     t_size = len(t)
     count = 0
     if s == t or abs(s_size - t_size)>1: return False
     if s_size == t_size:
         for i in range(s_size):
             if s[i]!=t[i]:
                 count+=1
             if count>1: return False
         return True
     elif s_size > t_size:
         for i in range(t_size):
             if t[i]!=s[i] and t[i]!=s[i+1]:
                 return False
     else:
         for i in range(s_size):
             if s[i]!=t[i] and s[i]!=t[i+1]:
                 return False
     return True


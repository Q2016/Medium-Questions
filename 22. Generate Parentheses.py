Question:
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

Example 1:
Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]        

    
    
    
    
    
    
    
    
    
one not optimum way is to use all substrings of the first exmaple above and check if each backtracked is valid or not and go on.    

Solution: Backtrack
    
Instead of adding '(' or ')' every time, let's only add them when we know it will remain a valid sequence. 
We can do this by keeping track of the number of opening and closing brackets we have placed so far.
We can start an opening bracket if we still have one (of n) left to place. And we can start a closing 
bracket if it would not exceed the number of opening brackets.        


    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        def backtrack(S = [], left = 0, right = 0):
            if len(S) == 2 * n:
                ans.append("".join(S))
                return
            if left < n:
                S.append("(")
                backtrack(S, left+1, right)
                S.pop()
            if right < left:
                S.append(")")
                backtrack(S, left, right+1)
                S.pop()
        backtrack()
        return ans

    
Complexity Analysis

Our complexity analysis rests on understanding how many elements there are in generateParenthesis(n). 
This analysis is outside the scope of this article, but it turns out this is the n-th Catalan number \dfrac{1}{n+1}\binom{2n}{n}, 
which is bounded asymptotically by frac{4^n}{n\sqrt{n}}.


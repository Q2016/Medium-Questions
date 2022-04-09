Question:
Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number 
could represent. Return the answer in any order. A mapping of digit to letters (just like on the telephone buttons) 
is given below. Note that 1 does not map to any letters.
 1    2     3
     abc   def   
4     5     6
ghi  jkl   mno   
7     8     9
pqrs tuv   wxyz 
      0	
Example 1:
Input: digits = "23"
Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]	
	
	
Solution: Iterative (educational)

78. Subsets: Runtime: 16 ms, faster than 96.05%

class Solution(object):
    def subsets(self, nums):

        res = []
        self.dfs(nums, [], res)
        return res
    
    def dfs(self, nums, path, res):
        res.append(path)
        for i in range(len(nums)):
            self.dfs(nums[i+1:], path + [nums[i]], res)
	
90. Subsets II: Runtime: 20 ms, faster than 96.23%

class Solution(object):
    def subsetsWithDup(self, nums):

        res = []
        nums.sort()
        self.dfs(nums, [], res)
        return res
    
    def dfs(self, nums, path, res):
        res.append(path)
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            self.dfs(nums[i+1:], path + [nums[i]], res)
	
77. Combinations: Runtime: 676 ms, faster than 42.96%

class Solution(object):
    def combine(self, n, k):

        res=[]
        self.dfs(range(1, n+1), k, [], res)
        return res
    
    def dfs(self, nums, k, path, res):
        if len(path) == k:
            res.append(path)
            return
        for i in range(len(nums)):
            self.dfs(nums[i+1:], k, path+ [nums[i]], res)
	
39. Combination Sum: Runtime: 124 ms, faster than 30.77%

class Solution(object):
    def combinationSum(self, candidates, target):

        res = []
        candidates.sort()
        self.dfs(candidates, target, [], res)
        return res
    
    def dfs(self, candidates, target, path, res):
        if target < 0:
            return   #backtracking
        if target == 0:
            res.append(path)
            return
        for i in range(len(candidates)):
            self.dfs(candidates[i:], target - candidates[i], path + [candidates[i]], res)  
	
40. Combination Sum II: Runtime: 36 ms, faster than 91.77%

class Solution(object):
    def combinationSum2(self, candidates, target):

        res = []
        candidates.sort()
        self.dfs(candidates, target, [], res)
        return res
    
    def dfs(self, candidates, target, path, res):
        if target < 0:
            return
        
        if target == 0:
            res.append(path)
        for i in range(len(candidates)):
            if i > 0 and candidates[i] == candidates[i-1]:
                continue
                
            if candidates[i]> target:
                break
                
            self.dfs(candidates[i+1:], target - candidates[i], path + [candidates[i]], res)
	
	
	
216. Combination Sum III	
		
def combinationSum3(self, k, n):
        ret = []
        self.dfs(list(range(1, 10)), k, n, [], ret)
        return ret
    
    def dfs(self, nums, k, n, path, ret):
        if k < 0 or n < 0:
            return 
        if k == 0 and n == 0:
            ret.append(path)
        for i in range(len(nums)):
            self.dfs(nums[i+1:], k-1, n-nums[i], path+[nums[i]], ret)  	
	
		
	
46. Permutations: Runtime: 28 ms, faster than 79.64%

class Solution(object):
    def permute(self, nums):

        res = []
        self.dfs(nums, [], res)
        return res
    
    def dfs(self, nums, path, res):
        if len(nums) == 0:
            res.append(path)
            return
        for i in range(len(nums)):
            self.dfs(nums[:i] + nums[i+1:], path + [nums[i]], res)   
	
47. Permutations II: Runtime: 40 ms, faster than 92.96%

class Solution(object):
    def permuteUnique(self, nums):

        res = []
        nums.sort()
        self.dfs(nums, [], res)
        return res
    
    def dfs(self, nums, path, res):
        if len(nums) == 0:
            res.append(path)
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            self.dfs(nums[:i] + nums[i+1:], path + [nums[i]], res)
	
17. Letter combination of a Phone Number::Runtime: 24 ms, faster than 43.40%

class Solution(object):
    def letterCombinations(self, digits):

        dic = { "2": "abc", "3": "def", "4":"ghi", "5":"jkl", "6":"mno", "7":"pqrs", "8":"tuv", "9":"wxyz"}
        
        res=[]
        if len(digits) ==0:
            return res
            
        self.dfs(digits, 0, dic, '', res)
        return res
    
    def dfs(self, nums, index, dic, path, res):
        if index >=len(nums):
            res.append(path)
            return
        string1 =dic[nums[index]]
        for i in string1:
            self.dfs(nums, index+1, dic, path + i, res)

Question:
Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] inclusive.
There is only one repeated number in nums, return this repeated number.
You must solve the problem without modifying the array nums and uses only constant extra space.    
    

    
    
    
    
    
    
    
    
    
    
    
Solution: Finding cycle
    
bit manipulation
A so-called O(1) space but essencially O(N) space algorithm using bit manipulation: use each bit of number seen as the seen array in solution 1.

def findDuplicate(self, nums: List[int]) -> int:
        seen = 0
        for num in nums:
            if seen & (1 << num):
                return num
            seen |= 1 << num
            
            
            
Finding cycle: Floyd's Algo

https://www.youtube.com/watch?v=wjYnzkAhcNk

fast pointer's speed is twice the slow pointer    
    
Complexity: Time complexity is O(n), because we potentially can traverse all list. Space complexity is O(1), because we actually do 
not use any extra space: our linked list is virtual.

class Solution:
    def findDuplicate(self, nums):
        slow, fast = 0,0
        while True:
            slow = nums[slow] 
            fast= nums[nums[fast]] # this means speed 2*x
            
            if slow == fast: break
           
        slow2 = 0;
        while True:
            slow = nums[slow] 
            slow2 = nums[slow2]
            if slow==slow2:
                return slow

Question:
Given an integer array of size n, find all elements that appear more than ⌊ n/3 ⌋ times.

Example 1:
Input: nums = [3,2,3]
Output: [3]   

    
Solution: (look at 169. repeatetive)
    
For those who aren't familiar with Boyer-Moore Majority Vote algorithm,
I found a great article (http://goo.gl/64Nams) that helps me to understand this fantastic algorithm!!
The essential concepts is you keep a counter for the majority number X. If you find a number Y that is not X, 
the current counter should deduce 1. The reason is that if there is 5 X and 4 Y, there would be one (5-4) more X than Y. 
This could be explained as "4 X being paired out by 4 Y".
And since the requirement is finding the majority for more than ceiling of [n/3], the answer would be less than or equal to two numbers.
So we can modify the algorithm to maintain two counters for two majorities.

Solution: Boyer-Moore Majority Vote algorithm

def majorityElement(self, nums):
    if not nums:
        return []
    count1, count2, candidate1, candidate2 = 0, 0, 0, 1
    for n in nums:
        if n == candidate1:
            count1 += 1
        elif n == candidate2:
            count2 += 1
        elif count1 == 0:
            candidate1, count1 = n, 1
        elif count2 == 0:
            candidate2, count2 = n, 1
        else:
            count1, count2 = count1 - 1, count2 - 1
    return [n for n in (candidate1, candidate2) if nums.count(n) > len(nums) // 3]

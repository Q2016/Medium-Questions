Solution
This problem is a follow-up of 3Sum, so take a look at that problem first if you haven't. 
4Sum and 3Sum are very similar; the difference is that we are looking for unique quadruplets instead of triplets.

As you see, 3Sum just wraps Two Sum in an outer loop. As it iterates through each value v, it 
finds all pairs whose sum is equal to target - v using one of these approaches:

Two Sum uses a hash set to check for a matching value.
Two Sum II uses the two pointers pattern in a sorted array.
Following a similar logic, we can implement 4Sum by wrapping 3Sum in another loop. But wait - 
there is a catch. If an interviewer asks you to solve 4Sum, they can follow-up with 5Sum, 6Sum, 
and so on. What they are really expecting at this point is a kSum solution. Therefore, 
we will focus on a generalized implementation here.

Approach 1: Two Pointers
Intuition

The two pointers pattern requires the array to be sorted, so we do that first. Also, it's 
easier to deal with duplicates if the array is sorted: repeated values are next to each other and easy to skip.

For 3Sum, we enumerate each value in a single loop, and use the two pointers pattern for 
the rest of the array. For kSum, we will have k - 2 nested loops to enumerate all combinations of k - 2 values.

Algorithm

We can implement k - 2 loops using a recursion. We will pass the starting point and k as 
the parameters. When k == 2, we will call twoSum, terminating the recursion.

For the main function:

Sort the input array nums.
Call kSum with start = 0, k = 4, and target, and return the result.
For kSum function:

At the start of the kSum function, we will check three conditions:
Have we run out of numbers to choose from?
Is the smallest number remaining greater than target / k?
If so, then any k numbers we choose will be too large.
Is the largest number remaining smaller than target / k?
If so, then any k numbers we choose will be too small.
If any of these conditions is true, there is no need to continue as no combination of the remaining elements can sum to target.
If k equals 2, call twoSum and return the result.
Iterate i through the array from start:
If the current value is the same as the one before, skip it.
Recursively call kSum with start = i + 1, k = k - 1, and target - nums[i].
For each returned subset of values:
Include the current value nums[i] into subset.
Add subset to the result res.
Return the result res.
For twoSum function:

Set the low pointer lo to start, and high pointer hi to the last index.
While low pointer is smaller than high:
If the sum of nums[lo] and nums[hi] is less than target, increment lo.
Also increment lo if the value is the same as for lo - 1.
If the sum is greater than target, decrement hi.
Also decrement hi if the value is the same as for hi + 1.
Otherwise, we found a pair:
Add it to the result res.
Decrement hi and increment lo.
Return the result res.
Implementation


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
	
        def kSum(nums: List[int], target: int, k: int) -> List[List[int]]:
            res = []
            
            # If we have run out of numbers to add, return res.
            if not nums:
                return res
            
            # There are k remaining values to add to the sum. The 
            # average of these values is at least target // k.
            average_value = target // k
            
            # We cannot obtain a sum of target if the smallest value
            # in nums is greater than target // k or if the largest 
            # value in nums is smaller than target // k.
            if average_value < nums[0] or nums[-1] < average_value:
                return res
            
            if k == 2:
                return twoSum(nums, target)
    
            for i in range(len(nums)):
                if i == 0 or nums[i - 1] != nums[i]:
                    for subset in kSum(nums[i + 1:], target - nums[i], k - 1):
                        res.append([nums[i]] + subset)
    
            return res

        def twoSum(nums: List[int], target: int) -> List[List[int]]:
            res = []
            lo, hi = 0, len(nums) - 1
    
            while (lo < hi):
                curr_sum = nums[lo] + nums[hi]
                if curr_sum < target or (lo > 0 and nums[lo] == nums[lo - 1]):
                    lo += 1
                elif curr_sum > target or (hi < len(nums) - 1 and nums[hi] == nums[hi + 1]):
                    hi -= 1
                else:
                    res.append([nums[lo], nums[hi]])
                    lo += 1
                    hi -= 1
                                                         
            return res

        nums.sort()
        return kSum(nums, target, 4)
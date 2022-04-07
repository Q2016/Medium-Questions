Question:
Suppose an array of length n sorted in ascending order is rotated between 1 and n times. For example, 
the array nums = [0,1,2,4,5,6,7] might become:
[4,5,6,7,0,1,2] if it was rotated 4 times.
[0,1,2,4,5,6,7] if it was rotated 7 times.
Notice that rotating an array [a[0], a[1], a[2], ..., a[n-1]] 1 time results in the array [a[n-1], a[0], a[1], a[2], ..., a[n-2]].
Given the sorted rotated array nums of unique elements, return the minimum element of this array.
You must write an algorithm that runs in O(log n) time.

Example 1:
Input: nums = [3,4,5,1,2]
Output: 1
Explanation: The original array was [1,2,3,4,5] rotated 3 times.  
  
  
  
  
Solution: BST
In this question we would essentially apply a modified version of binary search where the condition that decides the search 
direction would be different than in a standard binary search.
We want to find the smallest element in a rotated sorted array. What if the array is not rotated? How do we check that?
If the array is not rotated and the array is in ascending order, then last element > first element.
In this modified version of binary search algorithm, we are looking for this point. In the above example notice the Inflection Point .
All the elements to the left of inflection point > first element of the array.
All the elements to the right of inflection point < first element of the array.


    def findMin(self, nums):

        # If the list has just one element then return that element.
        if len(nums) == 1:
            return nums[0]
        # left pointer
        left = 0
        # right pointer
        right = len(nums) - 1
        # if the last element is greater than the first element then there is no rotation.
        # e.g. 1 < 2 < 3 < 4 < 5 < 7. Already sorted array.
        # Hence the smallest element is first element. A[0]
        if nums[right] > nums[0]:
            return nums[0]
        # Binary search way
        while right >= left:
            # Find the mid element
            mid = left + (right - left) / 2
            # if the mid element is greater than its next element then mid+1 element is the smallest
            # This point would be the point of change. From higher to lower value.
            if nums[mid] > nums[mid + 1]:
                return nums[mid + 1]
            # if the mid element is lesser than its previous element then mid element is the smallest
            if nums[mid - 1] > nums[mid]:
                return nums[mid]
            # if the mid elements value is greater than the 0th element this means
            # the least value is still somewhere to the right as we are still dealing with elements greater than nums[0]
            if nums[mid] > nums[0]:
                left = mid + 1
            # if nums[0] is greater than the mid value then this means the smallest value is somewhere to the left
            else:
                right = mid - 1



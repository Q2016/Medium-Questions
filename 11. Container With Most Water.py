Question:
There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).
Find two lines that together with the x-axis form a container, such that the container contains the most water.
Return the maximum amount of water a container can store.    

Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of 
water (blue section) the container can contain is 49.










If we could sort and keep the index of each hight, we can do it, would be NlogN
Oh crap, actually two point works because the left and right pointers start from maximum distances already!

Solution: Two pointers & Greedy

Idea / Proof:

The widest container (using first and last line) is a good candidate, because of its width. Its water 
level is the height of the smaller one of first and last line.
All other containers are less wide and thus would need a higher water level in order to hold more water.
The smaller one of first and last line doesn't support a higher water level and can thus be safely removed from further consideration.
Implementation: (Python)

class Solution:
    def maxArea(self, height):
        i, j = 0, len(height) - 1
        water = 0
        while i < j:
            water = max(water, (j - i) * min(height[i], height[j]))
            if height[i] < height[j]:
                i += 1
            else:
                j -= 1
        return water
      
Further explanation:

Variables i and j define the container under consideration. We initialize them to first and last line, 
meaning the widest container. Variable water will keep track of the highest amount of water we managed 
so far. We compute j - i, the width of the current container, and min(height[i], height[j]), the water 
level that this container can support. Multiply them to get how much water this container can hold, and 
update water accordingly. Next remove the smaller one of the two lines from consideration, as justified 
above in "Idea / Proof". Continue until there is nothing left to consider, then return the result.

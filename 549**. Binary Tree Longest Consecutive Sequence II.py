Question:
Given a binary tree, you need to find the length of Longest Consecutive Path in Binary Tree.
Especially, this path can be either increasing or decreasing. For example, [1,2,3,4] and 
[4,3,2,1] are both considered valid, but the path [1,2,4,3] is not valid. On the other hand, 
the path can be in the child-Parent-child order, where not necessarily be parent-child order.

Example 1:
Input:
        1
       / \
      2   3
Output: 2, Explanation: The longest consecutive path is [1, 2] or [2, 1].
Example 2:
Input:
        2
       / \
      1   3
Output: 3, Explanation: The longest consecutive path is [1, 2, 3] or [3, 2, 1].


                
                
                
No link                
                
Solution: Recursive
class Solution:
    def longestConsecutive(self, root: TreeNode) -> int:
        if not root:
            return 0
        
        # Path including root
        res = 1 + self.findPath(root, 1) + self.findPath(root, -1)        
        # Compare with path excluding root
        return max(res, max(self.longestConsecutive(root.left), self.longestConsecutive(root.right)))
    
    # longest consecutive subtree containing root
    def findPath(self, node: TreeNode, diff: int) -> int:
        if not node:
            return 0
        
        left, right = 0, 0
        if node.left and node.val + diff == node.left.val:
            left = self.longestSubtree(node.left, diff) + 1
        if node.right and node.val + diff == node.right.val:
            right = self.longestSubtree(node.right, diff) + 1
        return max(left, right)
        
        
Time: O(N²), 
Space: avg O(logN) worst O(N)

    
        
        

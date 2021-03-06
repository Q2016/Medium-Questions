Question:
Given a binary tree, return the values of its boundary in anti-clockwise direction starting from root. 
Boundary includes left boundary, leaves, and right boundary in order without duplicate nodes.
Left boundary is defined as the path from root to the left-most node. Right boundary is defined as 
the path from root to the right-most node. If the root doesn't have left subtree or right subtree, 
then the root itself is left boundary or right boundary. Note this definition only applies to the 
input binary tree, and not applies to any subtrees.
The left-most node is defined as a leaf node you could reach when you always firstly travel to the left 
subtree if exists. If not, travel to the right subtree. Repeat until you reach a leaf node.
The right-most node is also defined by the same way with left and right exchanged.

Example 1
Input:
  1
   \
    2
   / \
  3   4
Ouput:
[1, 3, 4, 2]

Explanation:
The root doesn't have left subtree, so the root itself is left boundary.
The leaves are node 3 and 4.
The right boundary are node 1,2,4. Note the anti-clockwise direction means you should output reversed right boundary.
So order them in anti-clockwise without duplicates and we have [1,3,4,2].
Example 2

Input:
    ____1_____
   /          \
  2            3
 / \          / 
4   5        6   
   / \      / \
  7   8    9  10  

Ouput:
[1,2,4,7,8,9,10,6,3]
Explanation:
The left boundary are node 1,2,4. (4 is the left-most node according to definition)
The leaves are node 4,7,8,9,10.
The right boundary are node 1,3,6,10. (10 is the right-most node).
So order them in anti-clockwise without duplicate nodes we have [1,2,4,7,8,9,10,6,3].






Sounds like a BFS and adding elements from left and right to both ends of an output array but I coudnt find the 
solution not even in the link

Solution: Preorder+DFS+Postorder
  
  https://www.youtube.com/watch?v=F76LIKzluKE
  
 
This question applied various of knowledge of tree. To solve this question, we first use preorder 
to get the left boundary node value, then we use dfs to find the leaves node value and append to 
the left boundary node value. At last, we use postorder to find the right boundary and append to 
the previous node values.


def boundaryOfBinaryTree(self, root: TreeNode) -> List[int]:
        if root is None: return []
        res=[root.val]
        def leftBoundary(root):
            if root is None or root.left is None and root.right is None: return
            res.append(root.val)
            if root.left:
                leftBoundary(root.left)
            else:
                leftBoundary(root.right)
            
        def rightBoundary(root):
            if root is None or root.left is None and root.right is None: return
            if root.right:
                rightBoundary(root.right)
            else:
                rightBoundary(root.left)
            res.append(root.val)
            
        def leaves(node):
            if node is None: return
            if node.left is None and node.right is None and node != root:
                res.append(node.val)
            leaves(node.left)
            leaves(node.right)
        
        leftBoundary(root.left)
        leaves(root)
        rightBoundary(root.right)
        return res

BigO
We traversal left subtree which takes O(n/2), right subtree which is O(n/2) and 
taversal all nodes for leaves and it takes O(n). In total is O(2n)

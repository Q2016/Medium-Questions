Question:
Given a binary tree where every node has a unique value, and a target key k, find the value of the nearest leaf node to target k in the tree.
Here,nearest to a leaf means the least number of edges travelled on the binary tree to reach any leaf of the tree.

Example 1:
Input: root = [1,2,3,4,null,null,null,5,null,6], k = 2
Diagram of binary tree:
             1
            / \
           2   3
          /
         4
        /
       5
      /
     6
Output: 3
Explanation:
The leaf node with value 3 (and not the leaf node with value 6) is nearest to the node with value 2.







No linnk

Solution: Graph BFS
Tree is a special kind of graph. And this is actually a problem of graph. We could use defination of leaf to mark the leaves and then do 
a BFS starting from the target node to find the closest leaf. To build a graph from this tree, we could create a new class GraphNode which has 
link to all its neighbours (both child and parent in the original tree). But in this problem, every node has a unique value, so we could simply 
use an additional dict to mark each node's parent, to avoid to build the full graph.

from collections import deque
class Solution:
    def findClosestLeaf(self, root: TreeNode, k: int) -> int:
        # Find the target node and build the graph
        target = self._get_target(root, k)
        parents = {}
        self._get_parents(root, None, parents)

        # BFS find the closest leaf
        visited = set()
        queue = deque([target])
        while queue:
            node = queue.popleft()
            if node is None or node.val in visited:
                continue
            if node.left is None and node.right is None:
                return node.val
            visited.add(node.val)
            queue.append(node.left)
            queue.append(node.right)
            queue.append(parents[node.val])

    def _get_target(self, node, k):
        if node is None:
            return None
        if node.val == k:
            return node
        return self._get_target(node.left, k) or self._get_target(node.right, k)

    def _get_parents(self, node, parent, parents):
        if node is None:
            return
        parents[node.val] = parent
        self._get_parents(node.left, node, parents)
        self._get_parents(node.right, node, parents)

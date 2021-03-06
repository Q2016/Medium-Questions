Question:
One way to serialize a binary tree is to use preorder traversal. When we encounter a non-null node, we record the 
node's value. If it is a null node, we record using a sentinel value such as '#'. For example, the above binary tree 
can be serialized to the string "9,3,4,#,#,1,#,#,2,#,6,#,#", where '#' represents a null node.
Given a string of comma-separated values preorder, return true if it is a correct preorder traversal serialization of 
a binary tree.              9
                          /   \              
                        3       2
                      /   \      \
                    4       1      6
Note: You are not allowed to reconstruct the tree.        

Example 1:
Input: preorder = "9,3,4,#,#,1,#,#,2,#,6,#,#"
Output: true

  
  
  
Solution:

Some used stack. Some used the depth of a stack. Here I use a different perspective. In a binary tree, if we consider null as leaves, then

-all non-null node provides 2 outdegree and 1 indegree (2 children and 1 parent), except root
-all null node provides 0 outdegree and 1 indegree (0 child and 1 parent).
Suppose we try to build this tree. During building, we record the difference between out degree and in degree diff = outdegree - indegree. 
When the next node comes, we then decrease diff by 1, because the node provides an in degree. If the node is not null, we increase diff by 2, 
because it provides two out degrees. If a serialization is correct, diff should never be negative and diff will be zero when finished.

public boolean isValidSerialization(String preorder) {
    String[] nodes = preorder.split(",");
    int diff = 1;
    for (String node: nodes) {
        if (--diff < 0) return false;
        if (!node.equals("#")) diff += 2;
    }
    return diff == 0;
}






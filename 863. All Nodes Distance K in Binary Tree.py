//Using recursion to find all of the son=>parent pair into a map.
//Using dfs to find K distance node, visited nodes will be recorded.
    
class Solution {
public:
    vector<int> ans;   
    map<TreeNode*, TreeNode*> parent;  // son=>parent  
    set<TreeNode*> visit;    //record visied node
    
    void findParent(TreeNode* node){
        if(!node ) return;
        if( node->left ){
            parent[node->left] = node;
            findParent(node->left);
        }
        if( node->right){
            parent[node->right] = node;
            findParent(node->right);
        }
    }
    
    vector<int> distanceK(TreeNode* root, TreeNode* target, int K) {
        if( !root ) return {};
        
        findParent(root);
        dfs(target, K );
        return ans;
    }
    void dfs( TreeNode* node, int K){
        if( visit.find(node) != visit.end() )
            return;
        visit.insert(node);
        if( K == 0 ){
            ans.push_back(node->val);
            return;
        }
        if( node->left ){
            dfs(node->left, K-1);
        }
        if( node->right){
            dfs(node->right, K-1);
        }
        TreeNode* p = parent[node];// you cant go up, that's why for findParent
        if( p )
            dfs(p, K-1);
    }
};
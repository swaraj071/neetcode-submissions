class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        # if there is left node move to left 
        # if there is right node move to right 
        # what will be the condition to stop ? 
        # When do I return 
        def dfs(root):
            if not root: 
                return [True,0]
            
            left,right = dfs(root.left) , dfs(root.right)

            balanced = left[0] and right[0] and abs(left[1]-right[1]) <= 1
            return [balanced, 1 + max(left[1],right[1])]
        return dfs(root)[0]
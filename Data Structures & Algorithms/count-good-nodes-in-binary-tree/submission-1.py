# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    # O(n) time
    # O(h) space
    def goodNodes(self, root: TreeNode) -> int:
        def recursive(node, maxValue):
            if not node:
                return 0

            curr = 1 if node.val >= maxValue else 0

            newMaxValue = max(maxValue, node.val)
            leftGoodNodes = recursive(node.left, newMaxValue)
            rightGoodNodes = recursive(node.right, newMaxValue)

            return curr + leftGoodNodes + rightGoodNodes
        
        return recursive(root, float("-inf"))

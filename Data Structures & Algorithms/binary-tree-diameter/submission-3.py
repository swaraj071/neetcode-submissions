class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        stack = [root]
        mp = {None: (0, 0)}   # (height, diameter)

        while stack:
            node = stack[-1]

            if node.left and node.left not in mp:
                stack.append(node.left)
            elif node.right and node.right not in mp:
                stack.append(node.right)
            else:
                node = stack.pop()

                leftHeight, leftDiameter = mp[node.left]
                rightHeight, rightDiameter = mp[node.right]

                height = 1 + max(leftHeight, rightHeight)
                diameter = max(
                    leftDiameter,
                    rightDiameter,
                    leftHeight + rightHeight
                )

                mp[node] = (height, diameter)

        return mp[root][1]
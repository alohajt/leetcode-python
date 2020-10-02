# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0

        ans = 0
        if not root.left and not root.right:
            ans = 1
        elif root.left and root.right:
            ans = min(self.minDepth(root.left), self.minDepth(root.right)) + 1
        elif root.left:
            ans = self.minDepth(root.left) + 1
        else:
            ans = self.minDepth(root.right) + 1
        return ans

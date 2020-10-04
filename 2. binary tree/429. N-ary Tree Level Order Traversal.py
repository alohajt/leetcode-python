"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""


class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        """
        :type root: Node
        :rtype: List[List[int]]
        """
        if not root:
            return []

        queue = [(root, 0)]
        res = [[]]

        while queue:
            node, level = queue.pop(0)
            if level >= len(res):
                res.append([])
            res[level].append(node.val)
            for child in node.children:
                queue.append((child, level + 1))
        return res

# BFS 模板
# class Solution(object):
#     def levelOrder(self, root):
#         """
#         :type root: Node
#         :rtype: List[List[int]]
#         """
#         res = []
#         que = collections.deque()
#         que.append(root)
#         while que:
#             level = []
#             size = len(que)
#             for _ in range(size):
#                 node = que.popleft()
#                 if not node:
#                     continue
#                 level.append(node.val)
#                 for child in node.children:
#                     que.append(child)
#             if level:
#                 res.append(level)
#         return res

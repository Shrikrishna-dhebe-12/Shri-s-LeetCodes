# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def minCameraCover(self, root):
        self.cameras = 0

        # States:
        # 0 -> Not Covered
        # 1 -> Has Camera
        # 2 -> Covered

        def dfs(node):
            if not node:
                return 2 

            left = dfs(node.left)
            right = dfs(node.right)

            if left == 0 or right == 0:
                self.cameras += 1
                return 1 

            if left == 1 or right == 1:
                return 2  

            return 0 

        if dfs(root) == 0:
            self.cameras += 1

        return self.cameras
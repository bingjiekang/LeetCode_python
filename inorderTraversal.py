"""给定一个二叉树的根节点 root ，返回 它的 中序 遍历 。
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
"""
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# 方法:中序遍历是先遍历左子树,再遍历根节点,再遍历右子树.递归若无左子树则加入根节点再遍历右子树.
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> list[int]:
        lt = []
        def Intar(root):
            if root == None:
                return
            Intar(root.left)
            lt.append(root.val)
            Intar(root.right)
        Intar(root)
        return lt
#
# @lc app=leetcode id=98 lang=python3
#
# [98] Validate Binary Search Tree
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        def valid(node, min=float('-inf'), max=float('inf')):
            if not node:
                return True
            if (node.val <= min) or (node.val >= max):
                return False
            if not valid(node.left, min=min, max=node.val):
                return False
            if not valid(node.right, min=node.val, max=max):
                return False
            return True
        return valid(root)




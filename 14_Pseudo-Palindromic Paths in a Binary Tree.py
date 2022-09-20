# 1457. Pseudo-Palindromic Paths in a Binary Tree
# https://leetcode.com/problems/pseudo-palindromic-paths-in-a-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pseudoPalindromicPaths (self, root):
        ans=0
        def dfs(node,temp):
            if node:
                temp=temp^(1<<node.val)
                if (not node.left) and (not node.right):
                    if temp & (temp-1)==0:
                        nonlocal ans
                        ans+=1
                else:
                    dfs(node.left,temp)
                    dfs(node.right,temp)
            
        dfs(root,0)
        return ans
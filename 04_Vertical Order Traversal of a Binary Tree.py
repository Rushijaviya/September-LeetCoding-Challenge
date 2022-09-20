# 987. Vertical Order Traversal of a Binary Tree
# https://leetcode.com/problems/vertical-order-traversal-of-a-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import defaultdict

class Solution:
    def verticalTraversal(self, root):
        d=defaultdict(list)
        
        def rec(node,dis,lev):
            if not node:
                return
            d[dis].append((node.val,lev))
            rec(node.left,dis-1,lev+1)
            rec(node.right,dis+1,lev+1)
            
        rec(root,0,0)
        ans=[(i,j) for i,j in d.items()]
        ans.sort()
        res=[]
        for i,j in ans:
            j.sort(key=lambda x:(x[1],x[0]))
            res.append([x for x,y in j])
        return (res)
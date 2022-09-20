# 429. N-ary Tree Level Order Traversal
# https://leetcode.com/problems/n-ary-tree-level-order-traversal/

"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root):
        level=[root]
        ans=[]
        while level and root:
            ans.append([node.val for node in level])
            temp=[]
            for node in level:
                if node.children:
                    for child in node.children:
                        temp.append(child)
            level=temp
        return ans
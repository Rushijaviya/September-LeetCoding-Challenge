# 1448. Count Good Nodes in Binary Tree
# https://leetcode.com/problems/count-good-nodes-in-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root):
        
        def dfs(node,max_value):
            if not node:
                return 0
            count=0
            if node.val>=max_value:
                count+=1
                max_value=node.val
            count+=dfs(node.left,max_value)
            count+=dfs(node.right,max_value)
            return count

        return dfs(root,float('-inf'))

        '''
        stack=[(root,root.val)]
        count=0
        while stack:
            node,max_value=stack.pop(0)
            if node.val>=max_value:
                count+=1
                max_value=node.val
            if node.left:
                stack.append((node.left,max_value))
            if node.right:
                stack.append((node.right,max_value))
        return count
        '''
    
    '''
    def goodNodes(self, r, ma=-10000):
        return self.goodNodes(r.left, max(ma, r.val)) + self.goodNodes(r.right, max(ma, r.val)) + (r.val >= ma) if r else 0
    '''
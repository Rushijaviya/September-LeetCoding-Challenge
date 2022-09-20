# 637. Average of Levels in Binary Tree
# https://leetcode.com/problems/average-of-levels-in-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root):
        '''
        ans=[]
        queue=[root]
        while queue:
            sum=0
            length=0
            for _ in range(len(queue)):
                node=queue.pop(0)
                sum+=node.val
                length+=1
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            ans.append(sum/length)
        return ans
        '''
        
        '''
        ans=[]

        def dfs(node,level):
            if not node:
                return
            if level>=len(ans):
                ans.append([0,0])
            ans[level][0]+=node.val
            ans[level][1]+=1
            dfs(node.left,level+1)
            dfs(node.right,level+1)
        
        dfs(root,0)
        return [i/j for i,j in ans]
        '''

        level=[root]
        ans=[]
        while level and root:
            x=[node.val for node in level]
            ans.append(sum(x)/len(x))
            temp=[[node.left,node.right] for node in level]
            level=[side for node in temp for side in node if side]
        return ans
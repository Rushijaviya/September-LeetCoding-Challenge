# 1770. Maximum Score from Performing Multiplication Operations
# https://leetcode.com/problems/maximum-score-from-performing-multiplication-operations/

class Solution:
    def maximumScore(self, nums, multipliers):
        n,m=len(nums),len(multipliers)
        dp=[[0]*(m+1) for _ in range(m+1)]
        for i in range(m-1,-1,-1):
            for left in range(i,-1,-1):
                right=n-1-(i-left)
                temp=multipliers[i]
                dp[i][left]=max(temp*nums[left]+dp[i+1][left+1],temp*nums[right]+dp[i+1][left])
        return dp[0][0]

        '''
        # Space Optimized
        n,m=len(nums),len(multipliers)
        dp=[0]*(m+1)
        for i in range(m-1,-1,-1):
            next_row=dp.copy()
            for left in range(i,-1,-1):
                right=n-1-(i-left)
                temp=multipliers[i]
                dp[left]=max(temp*nums[left]+next_row[left+1],temp*nums[right]+next_row[left])
        return dp[0]
        '''

        '''
        @lru_cache(None)
        def dp(idx,left):
            if idx==m:
                return 0
            right=(n-1)-(idx-left)
            dol=dp(idx+1,left+1)+nums[left]*multipliers[idx]
            dor=dp(idx+1,left)+nums[right]*multipliers[idx]
            return max(dol,dor)
            
        n,m=len(nums),len(multipliers)
        return dp(0,0)
        '''
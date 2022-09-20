# 188. Best Time to Buy and Sell Stock IV
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iv/

from functools import lru_cache

class Solution:
    def maxProfit(self, k, prices):
        @lru_cache(None)
        def dp(idx,stock,trans):
            if idx==len(prices) or trans==0:
                return 0
            don=dp(idx+1,stock,trans)
            if stock:
                dos=dp(idx+1,0,trans-1)+prices[idx]
            else:
                dos=dp(idx+1,1,trans)-prices[idx]
            return max(don,dos)
        
        return dp(0,0,k)
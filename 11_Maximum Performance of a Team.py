# 1383. Maximum Performance of a Team
# https://leetcode.com/problems/maximum-performance-of-a-team/

import bisect

class Solution:
    def maxPerformance(self, n, speed, efficiency, k):
        h = []
        res = sSum = 0
        for e,s in sorted(zip(efficiency, speed), reverse=1):
            bisect.insort(h, -s)
            sSum += s
            if len(h) > k:
                sSum += h.pop()
            res = max(res, sSum * e)
        return res % (10**9+7)
        
        '''
        l=[]
        sum=0
        ans=0
        for i,j in sorted(zip(efficiency,speed),reverse=1):
            heappush(l,j)
            sum+=j
            if len(l)>k:
                sum-=heappop(l)
            ans=max(ans,sum*i)
        return ans%(10**9+7)
        '''

        '''
        # TLE
        def rec(idx,sp,eff):
            if eff:
                temp=sum(sp)*min(eff)
                nonlocal ans
                ans=max(ans,temp)
            if len(sp)==k:
                return
            if idx==n:
                return
            rec(idx+1,sp+[speed[idx]],eff+[efficiency[idx]])
            rec(idx+1,sp,eff)
        
        ans=0
        rec(0,[],[])
        return ans%(10**9+7)
        '''
# 718. Maximum Length of Repeated Subarray
# https://leetcode.com/problems/maximum-length-of-repeated-subarray/

class Solution:
    def findLength(self, nums1, nums2):
        '''
        m,n=len(nums1),len(nums2)
        dp=[[0]*(n+1) for _ in range(m+1)]
        for i in range(m-1,-1,-1):
            for j in range(n-1,-1,-1):
                if nums1[i]==nums2[j]:
                    dp[i][j]=dp[i+1][j+1]+1
        return max(max(r) for r in dp)
        '''
        
        '''
        m,n=len(nums1),len(nums2)
        dp=[[0]*(n+1) for _ in range(m+1)]
        for i in range(1,m+1):
            for j in range(1,n+1):
                if nums1[i-1]==nums2[j-1]:
                    dp[i][j]=dp[i-1][j-1]+1
        return max(max(r) for r in dp)
        '''

        def check(length):
            seen=set()
            for i in range(0,n-length+1):
                seen.add(tuple(nums1[i:i+length]))
            for j in range(0,m-length+1):
                if tuple(nums2[j:j+length]) in seen:
                    return True
            return False
        
        n,m=len(nums1),len(nums2)
        start=0
        end=min(n,m)+1
        while start<end:
            mid=(start+end)//2
            if check(mid):
                start=mid+1
            else:
                end=mid
        return start-1
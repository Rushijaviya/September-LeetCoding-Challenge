# 42. Trapping Rain Water
# https://leetcode.com/problems/trapping-rain-water/

class Solution:
    def trap(self, height):
        '''
        if not height:
            return 0
        n=len(height)
        left=[0]*n
        right=[0]*n
        left[0]=height[0]
        for i in range(1,n):
            left[i]=max(left[i-1],height[i])
        right[-1]=height[-1]
        for i in range(n-2,-1,-1):
            right[i]=max(right[i+1],height[i])
        ans=0
        for i in range(n):
            ans+=(min(left[i],right[i])-height[i])
        return ans
        '''

        '''
        if not height:
            return 0
        stack=[]
        idx=0
        n=len(height)
        ans=0
        while idx<n:
            while stack and height[idx]>height[stack[-1]]:
                top=stack.pop()
                if not stack:
                    break
                distance=idx-stack[-1]-1
                bounded_height=min(height[idx],height[stack[-1]])-height[top]
                ans+=(distance*bounded_height)
            stack.append(idx)
            idx+=1
        return ans
        '''

        if not height:
            return 0
        max_left,max_right=0,0
        start=0
        end=len(height)-1
        ans=0
        while start<end:
            if height[start]<height[end]:
                if height[start]>=max_left:
                    max_left=height[start]
                else:
                    ans+=(max_left-height[start])
                start+=1
            else:
                if height[end]>=max_right:
                    max_right=height[end]
                else:
                    ans+=(max_right-height[end])
                end-=1
        return ans
# 967. Numbers With Same Consecutive Differences
# https://leetcode.com/problems/numbers-with-same-consecutive-differences/

class Solution:
    def numsSameConsecDiff(self, n, k):
        def dfs(length,num):
            if length==0:
                ans.append(num)
                return
            tail_digit=num%10
            next_digits=set([tail_digit+k,tail_digit-k])
            for next in next_digits:
                if 0<=next<10:
                    new_num=num*10+next
                    dfs(length-1,new_num)

        ans=[]
        for i in range(1,10):
            dfs(n-1,i)
        return ans
        
        '''
        def bfs(num):
            stack=[num]
            while stack:
                temp=stack.pop(0)
                if len(str(temp))==n:
                    ans.append(temp)
                else:
                    ld=temp%10
                    nd=set([ld-k,ld+k])
                    for i in nd:
                        if 0<=i<=9:
                            stack.append(temp*10+i)

        ans=[]
        for i in range(1,10):
            bfs(i)
        return ans
        '''
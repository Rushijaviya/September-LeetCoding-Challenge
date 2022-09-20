# 948. Bag of Tokens
# https://leetcode.com/problems/bag-of-tokens/

import collections

class Solution:
    def bagOfTokensScore(self, tokens, P):
        tokens.sort()
        deque = collections.deque(tokens)
        ans = bns = 0
        while deque and (P >= deque[0] or bns):
            while deque and P >= deque[0]:
                P -= deque.popleft()
                bns += 1
            ans = max(ans, bns)

            if deque and bns:
                P += deque.pop()
                bns -= 1
        return ans
        
        '''
        tokens.sort()
        ans=0
        score=0
        while tokens and (P>=tokens[0] or score):
            while tokens and P>=tokens[0]:
                P-=tokens.pop(0)
                score+=1
            ans=max(ans,score)
            if tokens and score:
                P+=tokens.pop()
                score-=1
        return ans
        '''
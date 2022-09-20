# 1996. The Number of Weak Characters in the Game
# https://leetcode.com/problems/the-number-of-weak-characters-in-the-game/

from collections import defaultdict

class Solution:
    def numberOfWeakCharacters(self, properties):
        properties.sort(key=lambda x: (-x[0],x[1]))
        
        ans = 0
        curr_max = 0
        
        for _, d in properties:
            if d < curr_max:
                ans += 1
            else:
                curr_max = d
        return ans
        
        '''
        X = sorted(properties)
        n = len(properties)
        ans, d, max_y = 0, defaultdict(list), -1
 
        for a, b in X:
            d[a] += [b]
            
        for t in sorted(list(d.keys()))[::-1]:
            for q in d[t]:
                if q < max_y: ans += 1
            for q in d[t]:
                max_y = max(max_y, q)
                
        return ans
        '''

        '''
        properties.sort(key=lambda x: (x[0], -x[1]))
        stack = []
        ans = 0
        
        for a, d in properties:
            while stack and stack[-1] < d:
                stack.pop()
                ans += 1
            stack.append(d)
        return ans
        '''
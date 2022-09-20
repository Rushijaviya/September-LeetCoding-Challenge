# 2007. Find Original Array From Doubled Array
# https://leetcode.com/problems/find-original-array-from-doubled-array/

import collections

class Solution:
    def findOriginalArray(self, changed):
        check=collections.Counter(changed)
        if check[0]%2:
            return []
        for x in sorted(check):
            if check[x]>check[2*x]:
                return []
            check[2*x]-=check[x] if x else check[x]//2
        return list(check.elements())
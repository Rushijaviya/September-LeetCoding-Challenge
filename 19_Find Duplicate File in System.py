# 609. Find Duplicate File in System
# https://leetcode.com/problems/find-duplicate-file-in-system/

from collections import defaultdict

class Solution:
    def findDuplicate(self, paths):
        d=defaultdict(list)
        for path in paths:
            s=path.split()
            dir_path=s[0]
            for i in s[1:]:
                j=0
                temp_name=""
                temp_content=""
                while j<len(i) and i[j]!='(':
                    temp_name+=i[j]
                    j+=1
                j+=1
                while j<len(i) and i[j]!=')':
                    temp_content+=i[j]
                    j+=1
                d[temp_content].append(dir_path+'/'+temp_name)
        ans=[]
        for i in d:
            if len(d[i])>1:
                ans.append(d[i])
        return ans
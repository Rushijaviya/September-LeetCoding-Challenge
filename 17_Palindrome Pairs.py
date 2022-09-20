# 336. Palindrome Pairs
# https://leetcode.com/problems/palindrome-pairs/

class Solution:
    def palindromePairs(self, words):
        '''
        def checkpalindrome(s,t):
            x=s+t
            return x==x[::-1]
        
        ans=[]
        for i in range(len(words)):
            for j in range(i+1,len(words)):
                if checkpalindrome(words[i],words[j]):
                    ans.append([i,j])
                if checkpalindrome(words[j],words[i]):
                    ans.append([j,i])                    
        return ans
        '''

        def checkpalindrome(x):
            return x==x[::-1]

        words={word:idx for idx,word in enumerate(words)}
        ans=[]
        for word,idx in words.items():
            n=len(word)
            for j in range(n+1):
                pref=word[:j]
                suff=word[j:]
                if checkpalindrome(pref):
                    back=suff[::-1]
                    if back!=word and back in words:
                        ans.append([words[back],idx])
                if j!=n and checkpalindrome(suff):
                    back=pref[::-1]
                    if back!=word and back in words:
                        ans.append([idx,words[back]])
        return ans
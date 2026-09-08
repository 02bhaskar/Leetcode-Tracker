# Last updated: 9/8/2026, 9:09:58 AM
1class Solution:
2    def findWords(self, words: List[str]) -> List[str]:
3        l1="qwertyuiop"
4        l2="asdfghjkl"
5        l3="zxcvbnm"
6        res=[]
7        for word in words:
8            w=word.lower()
9            if len(set(l1+w))==len(l1) or len(set(l2+w))==len(l2) or len(set(l3+w))==len(l3) :
10                res.append(word)
11        return res
12
13
14                
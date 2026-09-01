# Last updated: 9/1/2026, 10:27:41 PM
1class Solution:
2    def findRepeatedDnaSequences(self, s: str) -> List[str]:
3        left = 0
4        res = []
5        n = len(s)
6        count = {}
7
8        for right in range(9, n):
9            curr = s[left:right+1]
10            if curr not in count:
11                count[curr] = 1
12            else:
13                if count[curr] == 1:
14                    res.append(curr[:])
15                    count[curr] += 1
16            left += 1
17        return res
# Last updated: 9/1/2026, 1:48:57 PM
1class Solution:
2    def reverseStr(self, s, k):
3        ch = list(s)
4        n = len(ch)
5
6        start = 0
7
8        while start < n:
9            end = min(start + k - 1, n - 1)
10
11            l, r = start, end
12
13            while l < r:
14                ch[l], ch[r] = ch[r], ch[l]
15                l += 1
16                r -= 1
17
18            start += 2 * k
19
20        return ''.join(ch)
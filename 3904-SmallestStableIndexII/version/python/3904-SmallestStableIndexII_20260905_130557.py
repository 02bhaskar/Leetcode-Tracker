# Last updated: 9/5/2026, 1:05:57 PM
1class Solution:
2    def firstStableIndex(self, A: List[int], k: int) -> int:
3        pmax = -1
4        cand = cmax = 0
5
6        for i, x in enumerate(A):
7            pmax = max(pmax, x)
8
9            if i == cand:
10                cmax = pmax
11
12            if x < cmax - k:
13                cand = i + 1
14
15        return cand if cand < len(A) else -1
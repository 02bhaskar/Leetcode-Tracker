# Last updated: 10/9/2026, 9:32:55 AM
1class Solution:
2    def combine(self, n: int, k: int) -> List[List[int]]:
3        res = []
4        comb = []
5
6        def backtrack(start):
7            if len(comb) == k:
8                res.append(comb[:])
9                return
10            
11            for num in range(start, n + 1):
12                comb.append(num)
13                backtrack(num + 1)
14                comb.pop()
15
16        backtrack(1)
17        return res
# Last updated: 9/11/2026, 9:56:56 PM
1class Solution:
2    def totalNumbers(self, digits: List[int]) -> int:
3        f = Counter(digits)
4
5        res = 0
6        for n in range(100, 1000, 2):
7            i, r = divmod(n, 100)
8            j, k = divmod(r, 10)
9            res += f[i] > 0 and f[j] > (i == j) and f[k] > (i == k) + (j == k)
10
11        return res
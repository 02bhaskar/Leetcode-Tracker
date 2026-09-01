# Last updated: 9/1/2026, 10:22:37 PM
1class Solution:
2    def minCut(self, s: str) -> int:
3        n = len(s)
4
5        # is_pal[i][j] = True if s[i:j+1] is palindrome
6        is_pal = [[False] * n for _ in range(n)]
7
8        for i in range(n - 1, -1, -1):
9            for j in range(i, n):
10                if s[i] == s[j] and (j - i <= 2 or is_pal[i + 1][j - 1]):
11                    is_pal[i][j] = True
12
13        dp = [0] * n
14
15        for i in range(n):
16            if is_pal[0][i]:
17                dp[i] = 0
18            else:
19                dp[i] = float("inf")
20                for j in range(i):
21                    if is_pal[j + 1][i]:
22                        dp[i] = min(dp[i], dp[j] + 1)
23
24        return dp[-1]
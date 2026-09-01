# Last updated: 9/1/2026, 10:17:16 PM
1class Solution:
2    def numDecodings(self, s: str) -> int:
3        if s[0] == '0':
4            return 0
5        
6        n = len(s)
7        dp = [0] * (n + 1)
8        dp[0], dp[1] = 1, 1
9
10        for i in range(2, n + 1):
11            first = int(s[i - 1])
12            second = int(s[i - 2:i])
13
14            if 1 <= first <= 9:
15                dp[i] += dp[i - 1]
16            if 10 <= second <= 26:
17                dp[i] += dp[i - 2]
18
19        return dp[n]
20        
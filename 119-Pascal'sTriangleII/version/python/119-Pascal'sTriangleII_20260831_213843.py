# Last updated: 8/31/2026, 9:38:43 PM
1class Solution(object):
2    def getRow(self, r):
3        ans = [1]*(r+1);
4        up = r
5        down = 1
6        for i in range(1, r):
7            ans[i] = ans[i-1]*up/down;
8            up = up - 1
9            down = down + 1
10        return ans;
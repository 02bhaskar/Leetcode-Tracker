# Last updated: 9/1/2026, 12:36:13 PM
1class Solution:
2    def convertToBase7(self, num: int) -> str:
3
4        if num == 0: return '0'
5
6        ans, n = '', abs(num)
7
8        while n:
9            n, m = divmod(n,7)
10            ans+=str(m)
11
12        if num < 0: ans+= '-'
13
14        return ans[::-1]
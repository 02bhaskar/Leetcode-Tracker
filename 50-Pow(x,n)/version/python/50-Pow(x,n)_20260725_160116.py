# Last updated: 7/25/2026, 4:01:16 PM
1class Solution:
2    def myPow(self, x: float, n: int) -> float:
3
4        def calc_power(x, n):
5            if x == 0:
6                return 0
7            if n == 0:
8                return 1
9            
10            res = calc_power(x, n // 2)
11            res = res * res
12
13            if n % 2 == 1:
14                return res * x
15            
16            return res
17
18        ans = calc_power(x, abs(n))
19
20        if n >= 0:
21            return ans
22        
23        return 1 / ans 
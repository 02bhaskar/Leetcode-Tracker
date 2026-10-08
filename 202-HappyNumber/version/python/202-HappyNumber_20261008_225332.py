# Last updated: 10/8/2026, 10:53:32 PM
1class Solution:
2    def isHappy(self, n: int) -> bool:
3
4        def findSqrSum(n):
5            sqrSum = 0
6            while n > 0:
7                n, mod = divmod(n, 10)
8                sqrSum+= mod * mod
9            return sqrSum    
10
11        while n > 9:
12            n = findSqrSum(n)
13        return n == 1 or n == 7
14    
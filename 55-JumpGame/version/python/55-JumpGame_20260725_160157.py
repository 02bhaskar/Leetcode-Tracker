# Last updated: 7/25/2026, 4:01:57 PM
1class Solution:
2    def canJump(self, nums: List[int]) -> bool:
3        gas = 0
4        for n in nums:
5            if gas < 0:
6                return False
7            elif n > gas:
8                gas = n
9            gas -= 1
10            
11        return True
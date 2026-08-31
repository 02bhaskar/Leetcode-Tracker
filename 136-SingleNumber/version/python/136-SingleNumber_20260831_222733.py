# Last updated: 8/31/2026, 10:27:33 PM
1class Solution:
2    def singleNumber(self, nums: List[int]) -> int:
3        xor = 0
4        for num in nums:
5            xor ^= num
6        
7        return xor
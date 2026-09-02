# Last updated: 9/2/2026, 9:32:36 AM
1class Solution:
2    def removeDuplicates(self, nums: List[int]) -> int:
3        count = 0
4        current = 1
5        for i in range(1, len(nums)):
6            if nums[i] != nums[i - 1]:
7                count = 0
8                nums[current] = nums[i]
9                current += 1
10            else:
11                count += 1
12                if count <= 1:
13                    nums[current] = nums[i]
14                    current += 1
15        return current
# Last updated: 7/25/2026, 4:06:33 PM
1class Solution:
2    def findMin(self, nums: List[int]) -> int:
3        left, right = 0, len(nums) - 1
4
5        while left < right:
6            mid = (left + right) // 2
7
8            if nums[mid] > nums[right]:
9                left = mid + 1
10            elif nums[mid] < nums[right]:
11                right = mid
12            else:
13                right -= 1
14
15        return nums[left]
# Last updated: 10/12/2026, 10:48:04 PM
1class Solution:
2    def intersection(self, nums1: list[int], nums2: list[int]) -> list[int]:
3
4        return list(set(nums1) & set(nums2))
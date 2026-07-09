# Last updated: 7/9/2026, 3:09:03 PM
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        Left = 0
        Right = len(nums) - 1
        while Left <= Right:
            mid = (Left + Right) // 2
            if target == nums[mid]:
                return mid
            elif target < nums[mid]:
                Right = mid - 1
            else:
                Left = mid + 1
        return Left
// Last updated: 7/9/2026, 3:08:05 PM
class Solution {
    public int findMin(int[] nums) {
        int i = 0;
        int j = nums.length - 1;
        int ans = Integer.MAX_VALUE;
        while (i <= j) {
            if (nums[i] <= nums[j]) {
                ans = Math.min(ans, nums[i]);
                break;
            }
            int mid = i + (j - i) / 2;
            if (nums[i] <= nums[mid]) {
                ans = Math.min(ans, nums[i]);
                i = mid + 1;
            }
            else {
                ans = Math.min(ans, nums[mid]);
                j = mid - 1;
            }
        }
        return ans;
    }
}
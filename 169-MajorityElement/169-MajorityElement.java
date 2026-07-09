// Last updated: 7/9/2026, 3:07:59 PM
class Solution {
    public int majorityElement(int[] nums) {
      int n = nums.length;
      Arrays.sort(nums);
      return nums[n/2];
    }
}
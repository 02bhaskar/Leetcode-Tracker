// Last updated: 7/9/2026, 3:06:57 PM
class Solution {
    public int missingNumber(int[] nums) {
        int xor = 0;
        for (int i = 0; i <= nums.length; i++) {
            xor ^= i;
        }
        for (int x : nums) {
            xor ^= x;
        }
        return xor;
    }
}

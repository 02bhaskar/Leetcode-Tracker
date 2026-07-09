// Last updated: 7/9/2026, 3:05:45 PM
class Solution {
    public int differenceOfSum(int[] nums) {
        int elementSum = 0;
        for (int num : nums) {
            elementSum += num;
        }
        int digitSum = 0;
        for (int num : nums) {
            int temp = num;
            while (temp > 0) {
                digitSum += temp % 10;
                temp /= 10;
            }
        }
        return Math.abs(elementSum - digitSum);
    }
}

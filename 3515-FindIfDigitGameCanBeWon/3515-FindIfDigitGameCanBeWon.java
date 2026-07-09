// Last updated: 7/9/2026, 3:05:32 PM
class Solution {
    public boolean canAliceWin(int[] nums) {
        int sumSingle = 0, sumDouble = 0;
        for (int num:nums){
            if (num < 10) sumSingle += num;
            else sumDouble += num;
        }
        return sumSingle > sumDouble || sumDouble > sumSingle;
    }
}
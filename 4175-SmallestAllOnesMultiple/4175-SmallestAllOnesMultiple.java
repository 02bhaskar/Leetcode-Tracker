// Last updated: 7/9/2026, 3:05:24 PM
class Solution {
    public int minAllOneMultiple(int k) {
        if(k % 2 == 0 || k % 5 == 0) return - 1;
        int rem = 0;
        for(int i = 1; i <= k; i++) {
            rem = (rem * 10 + 1) % k;
            if(rem == 0) return i;
        }
        return -1;
    }
}
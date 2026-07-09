// Last updated: 7/9/2026, 3:07:38 PM
public class Solution {
    public int reverseBits(int n) {
        int result = 0;
        for (int i = 0; i < 32; i++) {
            result |= ((n >> i) & 1) << (31 - i);
        }
        return result;
    }
}

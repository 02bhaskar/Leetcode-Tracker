// Last updated: 7/9/2026, 3:06:41 PM
public class Solution {
    public int hammingDistance(int x, int y) {
        int xor = x ^ y;  
        int count = 0;
        while (xor != 0) {
            xor &= xor - 1; 
            count++;
        }
        return count;
    }
}

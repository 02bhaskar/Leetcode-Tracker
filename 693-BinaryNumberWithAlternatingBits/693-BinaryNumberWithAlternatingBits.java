// Last updated: 7/9/2026, 3:06:23 PM
public class Solution {
    public boolean hasAlternatingBits(int n) {
        int xor = n ^ (n >> 1);
        int check = xor + 1;
        return (check & (check - 1)) == 0;
    }
}

// Last updated: 7/9/2026, 3:05:36 PM
class Solution {

    public int differenceOfSums(int p, int q) {
        int a = p / q;
        int b = (p * (p + 1)) / 2;
        int c = a * (a + 1) * q;
        return  b - c;
    }
}
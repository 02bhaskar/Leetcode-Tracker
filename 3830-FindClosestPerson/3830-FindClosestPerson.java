// Last updated: 7/9/2026, 3:05:30 PM
class Solution {
    public int findClosest(int x, int y, int z) {
        int dist1 = x > z ? x - z : z - x;
        int dist2 = y > z ? y - z : z - y;
        if (dist1 < dist2) {
            return 1; 
        } else if (dist2 < dist1) {
            return 2; 
        } else {
            return 0;
        }
    }
    public static void main(String[] args) {
        Solution s = new Solution();
        System.out.println(s.findClosest(2, 7, 4));
        System.out.println(s.findClosest(2, 5, 6));
        System.out.println(s.findClosest(1, 5, 3));
    }
}

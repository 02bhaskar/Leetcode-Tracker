// Last updated: 7/9/2026, 3:06:43 PM
class Solution {
    public int arrangeCoins(int n) {
        int row=1;
            while (n>=row){
                n-=row;
                row++;
            }
        return row-1;
    }
}
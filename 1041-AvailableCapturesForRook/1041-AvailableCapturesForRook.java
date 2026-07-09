// Last updated: 7/9/2026, 3:06:14 PM
class Solution {
    public int numRookCaptures(char[][] board) {
        int R = 0, C = 0;

        for (int i = 0; i < 8; i++)
            for (int j = 0; j < 8; j++)
                if (board[i][j] == 'R') { R = i; C = j; }

        int count = 0;
        int[][] dirs = {{1,0},{-1,0},{0,1},{0,-1}};


        for (int[] d : dirs) {
            int r = R + d[0], c = C + d[1];
            while (r >= 0 && r < 8 && c >= 0 && c < 8) {
                if (board[r][c] == 'B') break;
                if (board[r][c] == 'p') { count++; break; }
                r += d[0]; 
                c += d[1];
            }
        }
        return count;
    }
}

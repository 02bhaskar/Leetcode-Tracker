// Last updated: 9/8/2026, 9:06:09 AM
1class Solution {
2    public int islandPerimeter(int[][] grid) {
3        int row = grid.length;
4        int col = grid[0].length;
5
6        int perimeter = 0;
7
8        // Iterate through all cells in the grid 🗺️
9        for (int i = 0; i < row; i++) {
10            for (int j = 0; j < col; j++) {
11                // Process only land cells 🏝️
12                if (grid[i][j] == 1) {
13                    // Check - UP ⬆️
14                    if (i == 0 || grid[i - 1][j] == 0) {
15                        perimeter++;
16                    }
17                    // Check - DOWN ⬇️
18                    if (i == row - 1 || grid[i + 1][j] == 0) {
19                        perimeter++;
20                    }
21                    // Check - LEFT ⬅️
22                    if (j == 0 || grid[i][j - 1] == 0) {
23                        perimeter++;
24                    }
25                    // Check - RIGHT ➡️
26                    if (j == col - 1 || grid[i][j + 1] == 0) {
27                        perimeter++;
28                    }
29                }
30            }
31        }
32        return perimeter;
33    }
34}
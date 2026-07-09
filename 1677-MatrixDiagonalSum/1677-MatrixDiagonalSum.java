// Last updated: 7/9/2026, 3:05:55 PM
// class Solution {
//     public int diagonalSum(int[][] mat) {
//         int a = mat.length;
//         int result = 0;
//         for (int i = 0; i < a; i++) {
//             result += mat[i][i];
//             result += mat[a - 1 - i][i];
//         }
//         if (a % 2 != 0) {
//             result -= mat[a / 2][a / 2];
//         }
//         return result;
//     }
// }


class Solution {
    public int diagonalSum(int[][] mat){
        int sum=0;
        int n=mat.length;
        for(int i=0;i<n;i++){
            for(int j=0;j<n;j++){
                if(i==j ||(i+j)==n-1)
                sum+=mat[i][j];
            }
        }
        return sum;
    }
}
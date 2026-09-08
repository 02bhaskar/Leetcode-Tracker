// Last updated: 9/8/2026, 9:06:35 AM
1class Solution {
2
3    public int findComplement(int num) {
4
5        int ans = 0;
6        int power = 1;
7
8        while (num > 0) {
9
10            // Get the last binary bit
11            int bit = num % 2;
12
13            // Flip the bit:
14            // 0 becomes 1, so add its place value
15            if (bit == 0) {
16                ans += power;
17            }
18
19            // Remove the last binary bit
20            num = num / 2;
21
22            // Move to the next binary position
23            power = power * 2;
24        }
25
26        return ans;
27    }
28}
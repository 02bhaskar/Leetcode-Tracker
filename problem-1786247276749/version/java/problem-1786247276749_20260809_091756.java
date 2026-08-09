// Last updated: 8/9/2026, 9:17:56 AM
1import java.util.*;
2
3class Solution {
4    public double minPrice(int[] prices, int[] discounts) {
5        Arrays.sort(prices);
6        Arrays.sort(discounts);
7
8        double a = 0;
9
10        for (int i = 0; i < prices.length; i++) {
11            a += prices[i];
12        }
13
14        int b = Math.min(prices.length, discounts.length);
15
16        for (int i = 0; i < b; i++) {
17            int c = prices[prices.length - 1 - i];
18            int d = discounts[discounts.length - 1 - i];
19
20            a -= (c * d) / 100.0;
21        }
22
23        return a;
24    }
25}
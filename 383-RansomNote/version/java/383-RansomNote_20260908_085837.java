// Last updated: 9/8/2026, 8:58:37 AM
1class Solution {
2
3    public boolean isSubsequence(String s, String t) {
4
5        int index = 0;
6
7        for (char c : t.toCharArray()) {
8
9            if (index == s.length())
10                return true;
11
12            if (s.charAt(index) == c) {
13                index++;
14            }
15        }
16
17        return index == s.length();
18    }
19}
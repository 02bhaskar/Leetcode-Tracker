// Last updated: 10/2/2026, 6:06:32 PM
1class Solution {
2    void generate(List<String> ans, String s, int open, int close, int n) {
3        if (open == n && close == n) {
4            ans.add(s);
5            return;
6        }
7
8        if (open > close)
9            generate(ans, s + ")", open, close + 1, n);
10
11        if (open < n)
12            generate(ans, s + "(", open + 1, close, n);
13    }
14
15    public List<String> generateParenthesis(int n) {
16        List<String> ans = new ArrayList<>();
17        generate(ans, "", 0, 0, n);
18        return ans;
19    }
20}
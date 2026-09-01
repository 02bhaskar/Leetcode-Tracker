// Last updated: 9/1/2026, 10:28:17 PM
1class Solution {
2    public boolean isIsomorphic(String s, String t) {
3        char[] sHash = new char[256];
4        char[] tHash = new char[256];
5
6        Arrays.fill(sHash, '0');
7        Arrays.fill(tHash, '0');
8
9        String ans = "";
10
11        for(int i = 0; i < s.length(); i++) {
12            if(sHash[s.charAt(i)] == '0' && tHash[t.charAt(i)] == '0' ) {
13                sHash[s.charAt(i)] =(char) (t.charAt(i)+1);
14                tHash[t.charAt(i)] =(char) (s.charAt(i)+1);
15            }
16        }
17        for(int i = 0; i < s.length(); i++) {
18            ans += (char)(sHash[s.charAt(i)] - 1);
19        }
20        if ( ans.equals(t)) return true;
21        return false;
22    }
23}
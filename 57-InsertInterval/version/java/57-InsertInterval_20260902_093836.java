// Last updated: 9/2/2026, 9:38:36 AM
1class Solution {
2    public List<List<Integer>> subsetsWithDup(int[] nums) {
3        Arrays.sort(nums); // Sort to handle duplicates
4        List<List<Integer>> outer = new ArrayList<>();
5        outer.add(new ArrayList<>());
6        
7        for (int num : nums) {
8            int n = outer.size();
9            for (int i = 0; i < n; i++) {
10                List<Integer> internal = new ArrayList<>(outer.get(i));
11                internal.add(num);
12                if (!outer.contains(internal)) {
13                    outer.add(internal);
14                }
15            }
16        }
17        
18        return outer;
19    }
20}
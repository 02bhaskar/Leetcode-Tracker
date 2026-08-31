// Last updated: 8/31/2026, 4:01:44 PM
1class Solution {
2    public TreeNode sortedArrayToBST(int[] nums) {
3        if (nums.length == 0)
4			return null;
5		return sortedArrayToBST(nums, 0, nums.length - 1);
6	}
7	public TreeNode sortedArrayToBST(int[] nums, int beg, int end) {
8		if (beg > end)
9			return null;
10		int mid = (beg + end) / 2;
11		TreeNode root = new TreeNode(nums[mid]);
12		root.left = sortedArrayToBST(nums, beg, mid - 1);
13		root.right = sortedArrayToBST(nums, mid + 1, end);
14		return root;
15    }
16}
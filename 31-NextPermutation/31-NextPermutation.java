// Last updated: 7/9/2026, 3:09:07 PM
class Solution {
    public void nextPermutation(int[] nums) {
        int idx = -1;
        int n = nums.length;

        for(int i = n-2 ;i>=0;i--){
            if(nums[i+1] > nums[i]){
                idx = i;
                break;
            }
        }
        if(idx == -1){
            reverse(0,nums);
            return;
        }

        for(int i = n-1;i>=idx;i--){
            if(nums[i] > nums[idx]){
                int temp = nums[i];
                nums[i] = nums[idx];
                nums[idx] = temp;
                break;
            }
        }

        reverse(idx+1,nums);
    }

    public int[] reverse(int i ,int[] nums){
        int j = nums.length -1;
        while(i<j){
            int temp = nums[i];
            nums[i] = nums[j];
            nums[j] = temp;
            i++;
            j--;
        }
        return nums;
    }
}
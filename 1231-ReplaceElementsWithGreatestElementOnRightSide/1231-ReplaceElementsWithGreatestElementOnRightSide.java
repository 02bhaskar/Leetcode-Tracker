// Last updated: 7/9/2026, 3:06:05 PM
class Solution {
    public int[] replaceElements(int[] arr) {
        int currentMax = -1;
        for (int i = arr.length - 1; i >= 0; i--) {
            int temp = arr[i];    
            arr[i] = currentMax;  
            currentMax = Math.max(currentMax, temp);
        }
        return arr;
    }
}

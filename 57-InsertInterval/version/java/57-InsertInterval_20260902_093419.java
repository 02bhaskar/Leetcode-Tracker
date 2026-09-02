// Last updated: 9/2/2026, 9:34:19 AM
1class Solution {
2    public boolean search(int[] nums, int target) {
3      int start = 0, end = nums.length - 1;
4      while(start <= end) {
5          int mid = start + (end - start) / 2;
6          if(nums[mid] == target) return true;
7          
8          //if there are duplicates
9          if(nums[start] == nums[mid] && nums[mid] == nums[end]) {
10                start ++;
11                end --;
12            }
13          
14          //left half is sorted
15          else if(nums[start] <= nums[mid]) {
16              if(target >= nums[start] && target <= nums[mid])
17              end = mid - 1;
18
19              else
20              start = mid + 1;
21          }
22
23          //right half is sorted
24          else {
25              if(target <= nums[end] && target >= nums[mid])
26              start = mid + 1;
27
28              else
29              end = mid - 1; 
30          }
31      }
32      return false;
33    }
34}
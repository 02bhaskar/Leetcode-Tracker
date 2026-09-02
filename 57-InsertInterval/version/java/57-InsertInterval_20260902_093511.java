// Last updated: 9/2/2026, 9:35:11 AM
1class Solution {
2    public boolean search(int[] nums, int target) {
3      int start = 0, end = nums.length - 1;
4      while(start <= end) {
5          int mid = start + (end - start) / 2;
6          if(nums[mid] == target) return true;
7          
8          if(nums[start] == nums[mid] && nums[mid] == nums[end]) {
9                start ++;
10                end --;
11            }
12          
13          else if(nums[start] <= nums[mid]) {
14              if(target >= nums[start] && target <= nums[mid])
15              end = mid - 1;
16
17              else
18              start = mid + 1;
19          }
20
21          else {
22              if(target <= nums[end] && target >= nums[mid])
23              start = mid + 1;
24
25              else
26              end = mid - 1; 
27          }
28      }
29      return false;
30    }
31}
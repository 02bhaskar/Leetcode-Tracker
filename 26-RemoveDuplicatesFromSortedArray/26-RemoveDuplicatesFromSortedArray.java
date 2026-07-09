// Last updated: 7/9/2026, 3:09:15 PM
  class Solution {
      public int removeDuplicates(int[] nums) {                                                                         
          // Slow pointer — position to place next unique element
          int slow = 0;                       
                                          
          // Fast pointer — scans every element
          for (int fast = 0; fast < nums.length; fast++) {                                                              
  
              // Found a new unique element (different from last placed)                                                
              if (nums[fast] != nums[slow]) {
                  slow++;                  // Move to next position                                                     
                  nums[slow] = nums[fast]; // Place the unique element
              }                               
              // If equal → duplicate → fast just moves ahead, slow stays                                               
          }                                   
                                                                                                                        
          // slow is last index of unique array → count = slow + 1
          return slow + 1;                                                                                              
      }           
  }   
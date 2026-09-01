# Last updated: 9/1/2026, 12:31:54 PM
1class Solution(object):
2    def nextGreaterElement(self, nums1, nums2):
3        ans = []
4        for i in range(len(nums1)):
5            max_num = -1
6            for j in range(len(nums2)):
7                index = j
8                if nums1[i] == nums2[j]: # Found element in nums2 that matches current element in nums1
9                    while index != len(nums2): # Iterate through remaining elements in nums2 to find next greater element
10                        if nums2[index] > nums1[i]:
11                            max_num = nums2[index] # Update max if we find a greater element
12                            break
13                        index += 1
14            ans.append(max_num)
15        return ans
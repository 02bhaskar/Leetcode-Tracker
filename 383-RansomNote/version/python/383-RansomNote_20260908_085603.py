# Last updated: 9/8/2026, 8:56:03 AM
1class Solution(object):
2    def canConstruct(self, ransomNote, magazine):
3        # Create a dictionary to store character counts
4        dictionary = {}
5
6        # Iterate through the magazine and count characters
7        for char in magazine:
8            if char not in dictionary:
9                dictionary[char] = 1
10            else:
11                dictionary[char] += 1
12
13        # Iterate through the ransom note and check character counts
14        for char in ransomNote:
15            if char in dictionary and dictionary[char] > 0:
16                dictionary[char] -= 1
17            else:
18                return False
19        
20        return True
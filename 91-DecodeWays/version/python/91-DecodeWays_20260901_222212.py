# Last updated: 9/1/2026, 10:22:12 PM
1class Solution:
2    def checkPalindrome(self, str, startIndex, lastIndex):
3        while startIndex <= lastIndex:
4            if str[startIndex] != str[lastIndex]:
5                return False
6            startIndex += 1
7            lastIndex -= 1
8        return True
9
10    def palindromePartition(self, index, ds, output, str):
11        if index == len(str):
12            output.append(ds[:])
13            return
14        for i in range(index, len(str)):
15            if self.checkPalindrome(str, index, i):
16                ds.append(str[index:i+1])
17                self.palindromePartition(i+1, ds, output, str)
18                ds.pop()
19
20    def partition(self, s: str) -> List[List[str]]:
21        output = []
22        ds = []
23        self.palindromePartition(0, ds, output, s)
24        return output
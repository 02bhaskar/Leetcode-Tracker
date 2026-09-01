# Last updated: 9/1/2026, 10:42:02 PM
1class Solution:
2    def removeDuplicateLetters(self, s: str) -> str:
3        last_occur = {}
4
5        for i, char in enumerate(s):
6            last_occur[char] = i        
7
8        stack = [] 
9        visited = set() 
10        for i in range(len(s)):
11            if s[i] in visited:
12                continue 
13            while stack and s[i] < stack[-1] and i < last_occur.get(stack[-1], -1):
14                visited.remove(stack.pop())
15
16            visited.add(s[i])  
17            stack.append(s[i])  
18        
19        return ''.join(stack)  
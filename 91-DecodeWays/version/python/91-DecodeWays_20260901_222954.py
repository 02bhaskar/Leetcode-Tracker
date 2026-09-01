# Last updated: 9/1/2026, 10:29:54 PM
1class Solution:
2    def isAdditiveNumber(self, num: str) -> bool:
3        n = len(num)
4        
5        # Try every split for first two numbers
6        for i in range(1, n):
7            for j in range(i+1, n):
8                num1, num2 = num[:i], num[i:j]
9                
10                # Skip if any number has leading zero (except "0" itself)
11                if (len(num1) > 1 and num1[0] == '0') or (len(num2) > 1 and num2[0] == '0'):
12                    continue
13                
14                n1, n2 = int(num1), int(num2)
15                k = j
16                while k < n:
17                    next_num = n1 + n2
18                    next_num_str = str(next_num)
19                    if not num.startswith(next_num_str, k):
20                        break
21                    k += len(next_num_str)
22                    n1, n2 = n2, next_num  # move window
23                
24                if k == n:
25                    return True
26        return False
# Last updated: 9/8/2026, 9:08:43 AM
1class Solution:
2    def constructRectangle(self, area: int) -> List[int]:
3        for l in range(int(area**0.5), 0, -1):            
4            if area % l == 0: 
5                return [area // l, l]
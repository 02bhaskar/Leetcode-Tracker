# Last updated: 7/9/2026, 3:08:32 PM
class Solution:
    def isNumber(self, s: str) -> bool:
        try:
            return (float(s) or int(float(s)) == 0) and not ('n'in s)
        except:
            return(False)
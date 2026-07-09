# Last updated: 7/9/2026, 3:08:56 PM
class Solution(object):
    def combinationSum(self, cand, tar):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        ans=[]
        li=[]
        cand.sort()
        self.find(tar,cand,ans,li,0)
        return li
    
    def find(self,t,c,ans,li,idx):
        if(t==0):
            li.append(ans[:])
            return

        for i in range(idx,len(c)):

            if(t>=c[i]):
                ans.append(c[i])
                self.find(t-c[i],c,ans,li,i)
                ans.pop()
        

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        #inreasing he hash ma
        h = {}
        l,r= 0 ,0
        res = 0
        maxF = 0
        while r < len(s):
            # increasing with get method in hash 
            h[s[r]] =  1 + h.get(s[r],0)

            if (r-l+1) - max(h.values()) >k:
                h[s[l]] -=1
                l+=1

            res = max(r-l+1,res)
            r+=1
        return res
                       
            
        




        
import math
class Solution: 
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        ans  = max(piles) 
        l = 1 # eating speed can not be negative or 0
        r = max(piles) # max values of piles 

        while l<=r:
            m = (l+r)//2  # mid
            hour = 0
            for i in piles:
                hour+= math.ceil(i/m)
            if hour <= h:
                ans = min(ans,m)
                r = m-1
            else:
                l = m+1
        return ans



                
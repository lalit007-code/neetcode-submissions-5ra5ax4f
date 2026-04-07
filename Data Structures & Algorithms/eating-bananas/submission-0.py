import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        max_piles = max(piles)
        if len(piles) == h:
            return max_piles
        piles.sort()

        ans = max_piles
        l = 1
        r = max_piles
        while l<=r:
            mid = (l+r)//2
            print(mid)
            total_hours = 0

            for i in piles:
                total_hours += math.ceil(i/mid)
            if total_hours > h:
                l = mid + 1
             # it means i have to eat more banans in one hours

            else:
                ans = min(ans,mid) 
                # it means i want to find minimum for which
                # r will be decrement as it has max(piles)
                r  = mid - 1                   
        return ans




            
class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights)-1

        ans = 0

        while l < r:
            minus_h = min(heights[l],heights[r])
            minus_idx = abs(r - l)
            # print("idx",l,r)
            # print("val",minus_h,minus_idx)
            mx = minus_h * minus_idx
            ans = max(mx,ans)

            if heights[r] < heights[l]:
                r-=1
            else:
                l+=1
        return ans
class Solution:
    def findMin(self, nums: List[int]) -> int:
        min_ans = nums[0]
        l ,r = 0,len(nums)-1

        while l<=r:
            if nums[l]<nums[r]:
                min_ans = min(min_ans,nums[l])
                break
            
            m = (l+r)//2
            min_ans = min(min_ans,nums[m])

            if nums[m]>=nums[l]:
                l = m + 1
            else:
                r = m-1
        return min_ans
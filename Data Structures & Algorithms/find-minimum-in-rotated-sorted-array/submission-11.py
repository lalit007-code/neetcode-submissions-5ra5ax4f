class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums)-1
        res = nums[0]

        while l <= r:
            if nums[l]<nums[r]:
                print("inside if condition")
                res  = min(nums[l],res)
                break

            m = (l+r)//2
            print(m,nums[m],res)
            res = min(nums[m],res)
            if nums[l] <= nums[m]:
                l = m+1
            else:
                r = m-1
        return res
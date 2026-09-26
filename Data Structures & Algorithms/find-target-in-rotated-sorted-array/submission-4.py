class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums)-1
        
        while l <=r :
            m = (l+r)//2
            # print("l",l,"r",r,"m",nums[m])
            if nums[m] == target:
                return m
            elif nums[l] <= nums[m]:
                if nums[l] <=  target and nums[m] >= target:
                    r = m -1
                else:
                    l = m + 1
            else:
                if nums[r] >= target and nums[m] <= target:
                    l = m + 1
                else:
                    r = m-1
        return -1
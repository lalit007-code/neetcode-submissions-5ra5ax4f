class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = []
        for idx,val in enumerate(nums):
            # if there is no value less than rero
            if val > 0:
                break;

            if idx > 0 and val == nums[idx-1]:
                continue
            l = idx + 1
            r = len(nums) - 1
            while l < r:
                total = val+  nums[l] + nums[r]
                if total > 0:
                    r-=1
                    
                elif total < 0:
                    l+=1
                    continue
                else:
                    ans.append([val,nums[l],nums[r]])
                    l+=1
                    r-=1
                    while nums[l] == nums[l-1] and l<r:
                        l+=1
        return ans

                
        
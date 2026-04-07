class Solution:
    def backtrack(self,idx,ans,ds,nums,target):
        if target == 0:
            ans.append(ds.copy())
            return
        
        if idx == len(nums):
            return
        
        if nums[idx] <= target:
                
            ds.append(nums[idx])
            self.backtrack(idx,ans,ds,nums,target-nums[idx])
            ds.pop()

        self.backtrack(idx+1,ans,ds,nums,target)

    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        ans = []
        ds = []

        self.backtrack(0,ans,ds,nums,target)
        return ans
class Solution:

    def dfs(self,idx,ds,ans,nums,target):
        if target == 0:
            ans.append(ds.copy())
            return
        
        if len(nums) == idx:
            return
        
        for i in range(idx,len(nums)):
            if nums[i] > target:
                continue
            
            ds.append(nums[i])
            self.dfs(i,ds,ans,nums,target - nums[i])
            ds.pop()

    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        ans  = []
        ds = []

        self.dfs(0,ds,ans,nums,target)
        return ans
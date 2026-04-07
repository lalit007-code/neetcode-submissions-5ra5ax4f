class Solution:

    def dfs(self,idx,ds,ans,nums,mp):
        if len(ds) == len(nums):
            ans.append(ds.copy())
            return
        
        for i in range(len(nums)):
            if mp[nums[i]]:
                continue
            ds.append(nums[i])
            mp[nums[i]] = True
            self.dfs(i+1,ds,ans,nums,mp)
            mp[nums[i]] = False
            ds.pop()

        
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        mp = {}
        for i in range(len(nums)):
            mp[nums[i]] = False 

        self.dfs(0,[],ans,nums,mp)
        return ans
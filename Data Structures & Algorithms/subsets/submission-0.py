class Solution:
    def dfs(self,idx,ds,ans,nums):

        ans.append(ds.copy())

        if idx == len(nums):
            return

        for i in range(idx,len(nums)):
            ds.append(nums[i])
            self.dfs(i+1,ds,ans,nums)
            ds.pop()

    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        ds = []
        
        self.dfs(0,ds,ans,nums)
        return ans
        
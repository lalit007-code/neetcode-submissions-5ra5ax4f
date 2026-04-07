class Solution:
    def backtrack(self,ds,ans,nums,maps):
        if len(nums) == len(ds):
            ans.append(ds.copy())
            return
        
        for i in range(len(nums)):
            # print("called")
            if nums[i] in maps and maps[nums[i]] > 0:
                continue 
            ds.append(nums[i])
            maps[nums[i]] = maps.get(nums[i],0)+1
            self.backtrack(ds,ans,nums,maps)
            ds.pop()
            maps[nums[i]]-=1
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        ds = []
        maps = {}
        self.backtrack(ds,ans,nums,maps)
        return ans
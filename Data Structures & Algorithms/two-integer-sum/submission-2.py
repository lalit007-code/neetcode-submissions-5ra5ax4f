class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_ans = {}
        for i in range(len(nums)):
            left = target - nums[i]
            if left in hash_ans:
                return [hash_ans[left],i]
            hash_ans[nums[i]] = i
        
        
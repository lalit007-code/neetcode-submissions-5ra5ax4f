class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ans = {}
        for i,n in enumerate(nums):
            left = target - n
            if left in ans:
                return [ans[left],i]
            ans[n] = i





        
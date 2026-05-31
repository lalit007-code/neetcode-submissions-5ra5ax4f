class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        freq = {}


        for k,v in enumerate(nums):
            left = target - nums[k]

            if left in freq:
                return [freq[left],k]
            else:
                freq[v] = k
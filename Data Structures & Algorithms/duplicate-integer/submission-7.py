class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        s = len(set(nums))
        n = len(nums)
        return s < n
        
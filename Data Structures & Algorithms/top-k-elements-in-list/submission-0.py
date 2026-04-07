class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        freq = [[] for i in range(len(nums)+1)]
        ans = []
        for idx,val in enumerate(nums):
            count[val] = 1 + count.get(val,0)
        for key,values in count.items():
            freq[values].append(key)
        for idx in range(len(freq)-1,0,-1):
            for val in freq[idx]:
                ans.append(val)
                if len(ans) == k:
                    return ans
                
        
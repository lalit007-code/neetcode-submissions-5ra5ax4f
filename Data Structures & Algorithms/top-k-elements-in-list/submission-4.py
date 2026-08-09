class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # make map
        # assing array len of max freq val
        # list of list containg elements as frequency equls tp index
        ## that list should be equals to k


        mp = {}
        arr = [ [] for _ in range(len(nums)+1) ]

        for i in nums:
            mp[i] = mp.get(i,0)+1

        # print(mp)
        # print(maxLen)
        # arr = [[]] * (maxLen+1)
        # arr = [[]] * (maxLen+1)
        # print(arr)

        # print(mp)
        for i,v in mp.items():
            # print(k,v)
            # print(arr[v])
            arr[v].append(i)
            # print(arr)

        # print("outside arr",arr)

        res = []

        for i in range(len(arr)-1,0,-1):
            for num in arr[i]:
                res.append(num)
                # print(res,k)
                if len(res) == k:
                    return res





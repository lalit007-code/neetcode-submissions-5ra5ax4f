class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        mp = set(nums)
        counter = 0
        ans = 0
        
        # for i in mp:
        #     print(i-1)

        for i in mp:
            counter = 1
            # print("i-1",i-1)
            # print("i+1",i+1)
            if i-1 not in mp:
                # print(i+1)
                while i+1 in mp:
                    counter+=1
                    i+=1

            # print("before while loop ans and counter",ans, counter)
            ans  = max(ans,counter)
            # print("after while loop ans and counter",ans, counter)

        return ans 
from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        dq = deque() # save index to keep track for length
        res = []
        #should use 2 pointer
        l = r = 0

        while r < len(nums):
            
            while dq and nums[dq[-1]] < nums[r]:
                dq.pop()
            
            dq.append(r)

            if l > dq[0]:
                dq.popleft()
            
            
            if r+1 >= k:
                #do not have to pop
                # keep it for comparsion
                res.append(nums[dq[0]])
                l+=1
            r+=1
        return res


            


        
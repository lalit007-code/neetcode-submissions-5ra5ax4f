class Solution:
    def trap(self, height: List[int]) -> int:
        # max_left_height = [0] * len(height)
        # max_right_height = [0] * len(height)
        # min_left_and_right_height = [0] * len(height)
        # max_left,max_right,min_left_and_right = 0,0,0 
        
        l = 0
        r = len(height)-1
        max_l ,max_r = height[l],height[r]

        res = 0
        #iterate with two pointers
        #take min of heights of l and r
        #and take max of l or r if there is and update maxL and maxR
        # subtract it from height of i
        # 
        while l < r:
            if max_l < max_r:
                l+=1
                max_l = max(height[l],max_l) # suppose of max(2,1)
                res+=max_l-height[l] # 2-2 = 0
            else:
                r -=1
                max_r = max(height[r],max_r)
                res+=max_r-height[r]
        return res

            


        # for idx,val in enumerate(height):
        #     max_left = max(val,max_left)
        #     max_left_height[idx] = max_left
        
        # for i in range(len(height)-1,-1,-1):
        #     max_right = max(height[i],max_right)
        #     max_right_height[i] = max_right
        
        # i = 0

        # while i < len(max_left_height):
        #     min_left_right = min(max_left_height[i],max_right_height[i])
        #     min_left_and_right_height[i] = min_left_right
        #     i+=1
        # sum = 0
        # for i in range(len(height)):
        #     cal = min_left_and_right_height[i] - height[i]
        #     if cal > 0:
        #         sum+=cal
        #     else:
        #         continue
        # return sum

            
            
            
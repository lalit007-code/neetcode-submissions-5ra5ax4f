class Solution:
    def trap(self, height: List[int]) -> int:
        max_left_height = [0] * len(height)
        max_right_height = [0] * len(height)
        min_left_and_right_height = [0] * len(height)
        max_left,max_right,min_left_and_right = 0,0,0 

        for idx,val in enumerate(height):
            max_left = max(val,max_left)
            max_left_height[idx] = max_left
        for i in range(len(height)-1,-1,-1):
            max_right = max(height[i],max_right)
            max_right_height[i] = max_right
        i = 0
        while i < len(max_left_height):
            min_left_right = min(max_left_height[i],max_right_height[i])
            min_left_and_right_height[i] = min_left_right
            i+=1
        sum = 0
        for i in range(len(height)):
            cal = min_left_and_right_height[i] - height[i]
            if cal > 0:
                sum+=cal
            else:
                continue
        return sum

            
            
            
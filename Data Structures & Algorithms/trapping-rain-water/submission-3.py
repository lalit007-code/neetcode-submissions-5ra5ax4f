class Solution:
    def trap(self, height: List[int]) -> int:

        leftmaxheight = [0] * len(height)
        rightmaxheight = [0] * len(height)

        leftmaxheight[0] = height[0]
        rightmaxheight[len(height)-1] = height[len(height)-1]

        #left height 
        for i in range(1,len(height)):
            leftmaxheight[i] = max(leftmaxheight[i-1],height[i])
        
        for i in range(len(height)-2,-1,-1):
            rightmaxheight[i] = max(rightmaxheight[i+1],height[i])


        ans = 0

        for i in range(len(height)):

            ans += min(leftmaxheight[i],rightmaxheight[i]) - height[i]
        
        return ans

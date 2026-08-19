class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        i = 0
        j = 0
        ans = []
        
        nums.sort()
        for k in range(len(nums)):
            if k > 0 and nums[k] == nums[k-1]:
                continue
            i = k + 1
            j = len(nums)-1
            # print(k,i,j)
            while i < j:
                # print(k,i,j)
  
                if nums[k] + nums[j] + nums[i] > 0:
                    j-=1
                elif nums[k] + nums[j] + nums[i] < 0:
                    i+=1
                else:
                    ans.append([nums[k],nums[j],nums[i]])
                    i+=1
                    j-=1
                    while nums[i] == nums[i-1] and i < j:
                        print("inside while loop loop")
                        i+=1         


        return ans
                
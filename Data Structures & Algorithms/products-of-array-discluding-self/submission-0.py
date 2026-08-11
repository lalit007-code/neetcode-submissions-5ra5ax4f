class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = []
        product = 1

        suffix = [0] *len(nums)
        for num in nums:
            product *= num
            prefix.append(product)
        
        product = 1
        for i in range(len(nums)-1,-1,-1):
            product *= nums[i]
            suffix[i] = product

        ans = [0]*len(prefix)

        for i in range(len(prefix)):
            if i-1 < 0 :
                # print(i)
                ans[i] = suffix[i+1]
            elif i + 1 > len(prefix)-1:
                ans[i] = prefix[i-1]
            else:
                ans[i] = prefix[i-1] * suffix[i+1]
        # print(ans)
        return ans
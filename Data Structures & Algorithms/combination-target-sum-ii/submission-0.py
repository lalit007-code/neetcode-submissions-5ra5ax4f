class Solution:
    def backtrack(self,idx,ans,ds,arr,target):
        if target == 0:
            # print(target,ds)
            ans.append(ds.copy())
            return
        
        if len(arr) == idx:
            return

        for i in range(idx,len(arr)):
            if i > idx and arr[i] == arr[i-1]:
                continue
            if arr[idx] > target:
                break
            ds.append(arr[i])
            self.backtrack(i+1,ans,ds,arr,target-arr[i])
            ds.pop()

    def combinationSum2(self, arr1: List[int], target: int) -> List[List[int]]:
        ans = []
        ds = []
        arr1.sort()
        self.backtrack(0,ans,ds,arr1,target)
        return ans
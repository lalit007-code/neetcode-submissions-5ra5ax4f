class Solution:
    def letterCombinations(self, digits: str) -> List[str]:

        if digits == "":
            return []
        ans = []
        mp: dict[str, str] = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }


        def dfs(idx,currSum):
            if len(currSum) == len(digits):
                ans.append(currSum)
                return

            for i in mp[digits[idx]]:
                dfs(idx+1,currSum+i)

        dfs(0,"")
        return ans
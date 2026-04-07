class Solution:
    def dfs(self,s,ans,ope,close,n):
        if ope > n:
            return
        if len(s) == 2*n:
            ans.append(s)
            return

        self.dfs(s+"(",ans,ope+1,close,n)

        if close < ope:
            self.dfs(s+")",ans,ope,close+1,n)



    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        ope = 0
        close = 0

        self.dfs("",ans,ope,close,n)
        return ans
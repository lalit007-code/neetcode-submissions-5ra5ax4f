class Solution:

    def partition(self, s: str) -> List[List[str]]:
        ans = []
        part = []
        def dfs(j):
            if j >=  len(s):
                ans.append(part.copy())
                return

            for i in range(j,len(s)):

                print("inside loop",i,j)
                if self.checkPalindrome(s,j,i):
                    part.append(s[j:i+1])
                    dfs(i+1)
                    part.pop()
            print("outside loop",i,j)
        dfs(0)
        return ans

    def checkPalindrome(self,s,l,r):
        while l<r:
            if s[l]!=s[r]:
                return False
            l+=1
            r-=1
        return True
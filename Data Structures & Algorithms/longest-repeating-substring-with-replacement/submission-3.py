class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        ans = 0

        for r in range(len(s)):
            count,max_f = {},0
            for j in range(r,len(s)):
                count[s[j]] = 1 + count.get(s[j],0)
                max_f = max(max_f,count[s[j]])
                if (j-r+1)- max_f <= k:
                    ans = max(j-r+1,ans)


        return ans

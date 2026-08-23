class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l ,r,maxLength = 0,0,0
        hashMap = {}
        while r<len(s):
            if s[r] in hashMap and hashMap[s[r]] >= l:
                l = hashMap[s[r]] + 1
                hashMap[s[r]] = r
            else:
                hashMap[s[r]] = r
            maxLength = max(maxLength,r-l+1)
            r+=1
        return maxLength

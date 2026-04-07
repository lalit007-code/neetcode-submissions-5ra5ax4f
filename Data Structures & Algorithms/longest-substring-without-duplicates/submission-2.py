class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l,max_len = 0 , 1 
        curr_set = set()
        if len(s) == 0:
            return 0
        for r in range(len(s)):
            while s[r] in curr_set:
                curr_set.remove(s[l])
                l+=1
            curr_set.add(s[r])
            max_len = max(max_len,r-l+1)
        return max_len


            

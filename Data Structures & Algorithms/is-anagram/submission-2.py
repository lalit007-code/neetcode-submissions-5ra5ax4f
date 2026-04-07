class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hash_str = {}

        if len(s) != len(t):
            return False
        
        for i in range(len(s)):
            if s[i] in hash_str:
                hash_str[s[i]]+=1
            else:
                hash_str[s[i]] = 1
            

        # print(hash_str)
        for i in range(len(t)):
            if t[i] in hash_str:
                print(t[i])
                hash_str[t[i]]-=1
                print(hash_str[t[i]])
            else:
                hash_str[t[i]] = -1
            
        # print(hash_str)
        for i in hash_str:
            if hash_str[i] != 0:
                return False
        return True


        
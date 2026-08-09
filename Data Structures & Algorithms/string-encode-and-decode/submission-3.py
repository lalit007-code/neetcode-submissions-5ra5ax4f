class Solution:
    def encode(self, strs: List[str]) -> str:
        ans = ""
        for i in strs:
            ans += str(len(i)) + "#" + i 
        print(ans)
        return ans

    def decode(self, s: str) -> List[str]:
        ans = []
        i = 0

        while i< len(s):
            strs = ""
            j = i
            while s[j] != "#":
                j+=1
            length = int(s[i:j])
            ans.append(s[j+1:j+length+1])
            i = j+1+length
        return ans


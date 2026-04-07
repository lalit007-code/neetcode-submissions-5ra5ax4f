class TimeMap:

    def __init__(self):
        self.s = defaultdict(list)
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.s[key].append([value,timestamp])
        

    def get(self, key: str, timestamp: int) -> str:
        res = ""
        v = self.s.get(key,[])

        l,r = 0,len(v)-1
        
        while l<=r:
            m = (l+r)//2
            if v[m][1] <= timestamp:
                #result so far
                res = v[m][0]
                l = m+1
                     
            else:
                r = m - 1
        return res
        

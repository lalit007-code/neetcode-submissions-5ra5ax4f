from collections import defaultdict
class TimeMap:

    def __init__(self):
        self.ds = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.ds[key].append([value,timestamp])
        # print(self.ds)
        # print(len(self.ds))
        

    def get(self, key: str, timestamp: int) -> str:
        res = ""
        value = self.ds.get(key,[])

        l,r = 0, len(value)-1

        while l<=r:
            m = (l+r)//2
            if value[m][1] <= timestamp:
                res = value[m][0]
                l = m+1
            else:
                r = m-1
                
        return res
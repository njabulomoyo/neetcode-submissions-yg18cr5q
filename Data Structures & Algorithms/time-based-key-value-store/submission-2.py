class TimeMap:
    from collections import defaultdict
    def __init__(self):
        self.store = defaultdict(list)
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.store[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.store:
            return ""
        
        values = self.store[key]
        l, r = 0, len(values)-1
        result = ""
        while l <= r:
            m = (l+r)//2
            if values[m][1] == timestamp:
                return values[m][0]
            if values[m][1] < timestamp:
                result = values[m][0]
                l = m + 1
            else:
                r = m - 1

        return result
        

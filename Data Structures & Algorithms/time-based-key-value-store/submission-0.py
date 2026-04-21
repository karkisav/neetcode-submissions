class TimeMap:

    def __init__(self):
        self.result = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        # store key and value in a dict, at a perticular timestamp
        ...
        if key not in self.result:
            self.result[key] = []

        self.result[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        """you know timstamp is in sorted way so use Binary search to get
        the timestamp with the key and value pair"""

        res, finalList = "", self.result.get(key, [])

        l, r = 0, len(finalList) - 1

        while l <= r:
            m = (l + r) // 2
            if finalList[m][1] <= timestamp:
                res = finalList[m][0]
                l = m + 1
            else:
                r = m - 1
                
        return res

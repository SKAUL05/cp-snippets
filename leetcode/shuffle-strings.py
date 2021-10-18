class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        d = {}
        sr = ""
        for i in range(len(indices)):
            d[indices[i]] = s[i]
        print(d)
        for i in range(len(indices)):
            sr += d[i]
        return sr

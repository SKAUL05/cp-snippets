class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        d = {indices[i]: s[i] for i in range(len(indices))}
        print(d)
        return "".join(d[i] for i in range(len(indices)))


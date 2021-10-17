class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        a = set(nums)
        nums[:len(a)] = sorted(a)
        return len(a)
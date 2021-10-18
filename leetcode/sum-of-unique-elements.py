class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        l = [x for x in nums if nums.count(x) == 1]
        sum = 0
        for i in l:
            sum += i
        return sum

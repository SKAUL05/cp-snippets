"""
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.



Example 1:

Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Explanation:
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
The distinct triplets are [-1,0,1] and [-1,-1,2].
Notice that the order of the output and the order of the triplets does not matter.
Example 2:

Input: nums = [0,1,1]
Output: []
Explanation: The only possible triplet does not sum up to 0.
Example 3:

Input: nums = [0,0,0]
Output: [[0,0,0]]
Explanation: The only possible triplet sums up to 0.


Constraints:

3 <= nums.length <= 3000
-105 <= nums[i] <= 105
"""


class Solution(object):
    @staticmethod
    def threeSum(nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = set()
        zero_set = []
        positive_set = []
        negative_set = []
        for num in nums:
            if num < 0:
                negative_set.append(num)
            elif num > 0:
                positive_set.append(num)
            else:
                zero_set.append(num)

        neg_check = set(negative_set)
        pos_check = set(positive_set)

        if zero_set:
            for pos in pos_check:
                if (-1 * pos) in neg_check:
                    result.add((-1 * pos, 0, pos))

        if len(zero_set) >= 3:
            result.add((0, 0, 0))

        for i in range(len(negative_set)):
            for j in range(i + 1, len(negative_set)):
                target = -1 * (negative_set[i] + negative_set[j])
                if target in pos_check:
                    result.add(
                        tuple(sorted([negative_set[i], negative_set[j], target]))
                    )

        for i in range(len(positive_set)):
            for j in range(i + 1, len(positive_set)):
                target = -1 * (positive_set[i] + positive_set[j])
                if target in neg_check:
                    result.add(
                        tuple(sorted([positive_set[i], positive_set[j], target]))
                    )

        return result


s = Solution()
print(s.threeSum([-1, 0, 1, 2, -1, -4]))

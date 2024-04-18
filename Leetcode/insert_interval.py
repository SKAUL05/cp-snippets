"""
Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
Output: [[1,5],[6,9]]

Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
Output: [[1,2],[3,10],[12,16]]
"""


class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[List[int]]
        :type newInterval: List[int]
        :rtype: List[List[int]]
        """
        final = []
        n = len(intervals)
        i = 0

        while i < n and intervals[i][1] < newInterval[0]:
            final.append(intervals[i])
            i += 1

        while i < n and newInterval[1] >= intervals[i][0]:
            newInterval[0] = min(intervals[i][0], newInterval[0])
            newInterval[1] = max(intervals[i][1], newInterval[1])
            i += 1
        final.append(newInterval)

        while i < n:
            final.append(intervals[i])
            i += 1

        print(final)


s = Solution()
s.insert([[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]], [4, 8])
s.insert([[1, 3], [6, 9]], [2, 5])

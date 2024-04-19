import math


class Solution(object):
    @staticmethod
    def kClosest(points, k):
        """
        :type points: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """
        final = {}
        for i in points:
            dist = math.sqrt(math.pow((i[0] - 0), 2) + math.pow((i[1] - 0), 2))
            final[f"{str(i[0])}_{str(i[1])}"] = dist
        final = dict(sorted(final.items(), key=lambda item: item[1]))
        print(final)
        z = []
        for i in final:
            z.append([int(i.split("_")[0]), int(i.split("_")[1])])
            if len(z) == k:
                return z
        return z


s = Solution()
print(s.kClosest([[1, 3], [-2, 2]], 1))

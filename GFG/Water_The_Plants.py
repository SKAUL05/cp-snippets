"""
A gallery with plants is divided into n parts, numbered 0, 1, 2, 3, ..., n-1. There are provisions for attaching water sprinklers in every division. A sprinkler with range x at division i can water all divisions from i-x to i+x.

Given an array gallery[] consisting of n integers, where gallery[i] is the range of the sprinkler at partition i (a power of -1 indicates no sprinkler attached), return the minimum number of sprinklers that need to be turned on to water the entire gallery. If there is no possible way to water the full length using the given sprinklers, print -1.

Example 1:

Input:
n = 6
gallery[] = {-1, 2, 2, -1, 0, 0}
Output:
2
Explanation:
Sprinklers at index 2 and 5
can water the full gallery, span of
sprinkler at index 2 = [0,4] and span
of sprinkler at index 5 = [5,5].
Example 2:

Input:
n = 9
gallery[ ] = {2, 3, 4, -1, 2, 0, 0, -1, 0}
Output:
-1
Explanation:
No sprinkler can throw water
at index 7. Hence all plants cannot be
watered.
Example 3:

Input:
n = 9
gallery[ ] = {2, 3, 4, -1, 0, 0, 0, 0, 0}
Output:
3
Explanation:
Sprinkler at indexes 2, 7 and
8 together can water all plants.
Your task:
You do not have to take any input or print anything. Your task is to complete the function min_sprinklers() which takes the array gallery[ ] and the integer n as input parameters and returns the minimum number of sprinklers that need to be turned on to water the entire gallery.

Expected Time Complexity: O( nlog(n) )
Expected Auxiliary Space: O( n )
"""


# User function Template for python3


class Solution:
    def min_sprinklers(self, gallery, n):
        sprinkler = [(i - gallery[i], i + gallery[i]) for i in range(n)]
        sprinkler.sort()
        # print(sprinkler)
        target = 0
        cnt = 0
        i = 0
        while target < n:
            if i == n or sprinkler[i][0] > target:
                return -1
            max_range = sprinkler[i][1]
            while i + 1 < n and sprinkler[i + 1][0] <= target:
                i += 1
                max_range = max(max_range, sprinkler[i][1])
            if max_range < target:
                return -1
            cnt += 1
            target = max_range + 1

        return cnt


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n = int(input())
        gallery = [int(x) for x in input().strip().split()]
        obj = Solution()
        print(obj.min_sprinklers(gallery, n))

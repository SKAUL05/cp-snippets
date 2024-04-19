"""
Given an m x n binary matrix mat, return the distance of the nearest 0 for each cell.
The distance between two adjacent cells is 1.

Input: mat = [[0,0,0],[0,1,0],[0,0,0]]
Output: [[0,0,0],[0,1,0],[0,0,0]]

Input: mat = [[0,0,0],[0,1,0],[1,1,1]]
Output: [[0,0,0],[0,1,0],[1,2,1]]
"""

from collections import deque


class Solution(object):
    @staticmethod
    def update_matrix(mat):
        """
        :type mat: List[List[int]]
        :rtype: List[List[int]]
        """
        dq = deque()
        for row in range(len(mat)):
            for col in range(len(mat[row])):
                if mat[row][col] == 0:
                    dq.append((row, col))
                else:
                    mat[row][col] = -1

        while dq:
            r, c = dq.popleft()
            directions = [(0, -1), (0, 1), (-1, 0), (1, 0)]
            for direction in directions:
                new_row, new_col = direction[0] + r, direction[1] + c
                if (
                    0 <= new_row < len(mat)
                    and 0 <= new_col < len(mat[0])
                    and mat[new_row][new_col] == -1
                ):
                    mat[new_row][new_col] = mat[r][c] + 1
                    dq.append((new_row, new_col))
        return mat


s = Solution()
print(s.update_matrix([[0, 0, 0], [0, 1, 0], [0, 0, 0]]))
print(s.update_matrix([[0, 0, 0], [0, 1, 0], [1, 1, 1]]))

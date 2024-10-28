class Solution(object):
    def possibleStringCount(self, word):
        """
        :type word: str
        :rtype: int
        """
        cnt = 1
        sums = 0
        for i in range(1, len(word)):
            if word[i] == word[i - 1]:
                sums += 1
            else:
                if sums > 0:
                    cnt += sums
                    sums = 0
        if sums > 0:
            cnt += sums
        return cnt

class Solution(object):
    def possibleStringCount(self, word):
        """
        :type word: str
        :rtype: int
        """
        count = 1
        consecutive_count = 0

        for i in range(1, len(word)):
            if word[i] == word[i - 1]:
                consecutive_count += 1
            else:
                count += consecutive_count
                consecutive_count = 0

        return count + consecutive_count

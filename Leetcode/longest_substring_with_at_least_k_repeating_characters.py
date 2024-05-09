from collections import OrderedDict


class Solution(object):
    @staticmethod
    def longestSubstring(s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        iter_set = set()
        substring_arr = ""
        counter = OrderedDict({s[0]: 0})
        var_sub = 0
        substring = ""

        for i in range(len(s)):
            iter_set.add(s[i])
            if s[var_sub] != s[i]:
                if s[i] in counter:
                    del counter[s[i]]
                counter.update({s[i]: i})
                var_sub = i
                if len(counter) > k:
                    counter.popitem(last=False)
                    var_sub = next(iter(counter))
                    var_sub = counter[var_sub]

            if len(iter_set) <= k:
                substring += s[i]
            else:
                if len(substring_arr) < len(substring):
                    substring_arr = substring
                substring = s[var_sub:i] + s[i]
                iter_set = set(substring)

        return substring_arr if len(substring) < len(substring_arr) else substring


s = Solution()
print(s.longestSubstring("aabbbbcbbbadef", 2))

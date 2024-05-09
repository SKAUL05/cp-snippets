"""
Given two strings s and t of lengths m and n respectively, return the minimum window
substring
 of s such that every character in t (including duplicates) is included in the window. If there is no such substring, return the empty string "".

The testcases will be generated such that the answer is unique.



Example 1:

Input: s = "ADOBECODEBANC", t = "ABC"
Output: "BANC"
Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.
Example 2:

Input: s = "a", t = "a"
Output: "a"
Explanation: The entire string s is the minimum window.
Example 3:

Input: s = "a", t = "aa"
Output: ""
Explanation: Both 'a's from t must be included in the window.
Since the largest window of s only has one 'a', return empty string.

"""


class Solution(object):
    @staticmethod
    def minWindow(s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        counter = len(t)
        begin, end, n = 0, 0, len(s)
        min_length = len(s) + 1
        head = 0

        chr_map = {}
        for i in t:
            if i in chr_map:
                chr_map[i] += 1
            else:
                chr_map[i] = 1

        while end < n:
            if s[end] in chr_map:
                if chr_map[s[end]] > 0:
                    counter -= 1
                chr_map[s[end]] -= 1

            end += 1

            while counter == 0:
                if (end - begin) < min_length:
                    min_length = end - begin
                    head = begin

                if s[begin] in chr_map:
                    chr_map[s[begin]] += 1
                    if chr_map[s[begin]] > 0:
                        counter += 1
                begin += 1
        return "" if min_length == n + 1 else s[head:head + min_length]


s = Solution()
print(s.minWindow("ADOBECODEBANC", "ABC"))
print(s.minWindow("a", "a"))
print(s.minWindow("a", "aa"))

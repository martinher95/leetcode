"""
3. Longest Substring Without Repeating Characters
"""


class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        sub = ""
        if len(s) > 0:
            length = 1
            for i in range(0, len(s)):
                substring = s[i:]
                print(substring)
                for n in substring:
                    if n not in sub:
                        sub += n
                        if len(sub) > length:
                            length = len(sub)
                    else:
                        if len(sub) > length:
                            length = len(sub)
                        sub = ""
                        break
        else:
            length = 0
        return length


if __name__ == '__main__':
    sol = Solution().lengthOfLongestSubstring("jbpnbwwd")
    print(sol)

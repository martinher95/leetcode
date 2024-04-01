"""
3. Longest Substring Without Repeating Characters
"""


class Solution(object):
    # subarray approach
    def lengthOfLongestSubstring0(self, s):
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

    # window approach
    def lengthOfLongestSubstring1(self, s):
        length = len(s)
        maxi = 0
        if len(s) > 0:
            for start in range(0, length):
                end = start
                sub = ""
                while end < length:
                    char = s[end]
                    if char not in sub:
                        sub = s[start:end+1]
                        print(sub)
                        end += 1
                        maxi = max(maxi, len(sub))
                    else:
                        break
        return maxi


if __name__ == '__main__':
    sol = Solution().lengthOfLongestSubstring1("pwwkew")
    print(sol)

"""
9. Palindrome Number
"""


class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        str_x = str(x)
        str_y = "".join([n for n in reversed(str_x)])
        if str_x == str_y:
            return True
        return False


if __name__ == '__main__':
    sol = Solution().isPalindrome(121)
    print(sol)

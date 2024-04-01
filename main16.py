"""125. Valid Palindrome"""


class Solution:
    def isPalindrome(self, s):
        s = ''.join([char.lower() for char in s if char.isalnum()])
        if s == s[::-1]:
            return True
        else:
            return False


if __name__ == '__main__':
    s = "0P"
    sol = Solution().isPalindrome(s)
    print(sol)
"""5. Longest palindromic"""


def longestPalindrome(self, s: str) -> str:
    if len(s) == 1:
        return s

    max_length = 0
    longest_palindrome = ""

    for i in range(len(s)):
        for j in range(i + 1, len(s) + 1):
            substring = s[i:j]
            if substring == substring[::-1] and len(substring) > max_length:
                max_length = len(substring)
                longest_palindrome = substring

    return longest_palindrome
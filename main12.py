"""
1647. Minimum Deletions to Make Character Frequencies Unique
"""

def has_duplicate_values(dictionary):
    seen_values = set()
    for value in dictionary.values():
        if value in seen_values:
            return True
        seen_values.add(value)
    return False


def get_keys_with_same_values(dictionary):
    keys_by_value = {}
    for key, value in dictionary.items():
        if value not in keys_by_value:
            keys_by_value[value] = []
        keys_by_value[value].append(key)
    return keys_by_value


class Solution(object):
    def minDeletions(self, s):
        """
        :type s: str
        :rtype: int
        """
        total = 0
        letter_count = {}
        for char in s:
            letter_count[char] = letter_count.get(char, 0) + 1
        while has_duplicate_values(letter_count):
            same = get_keys_with_same_values(letter_count)
            for k, v in same.items():
                if len(v) > 1:
                    letter_count[v[0]] = letter_count[v[0]] - 1
                    if letter_count[v[0]] == 0:
                        del letter_count[v[0]]
                    total += 1
        return total


if __name__ == '__main__':
    sol = Solution().minDeletions("abcdefghijklmnopqrstuvwxwzabcdefghijklmnopqrstuvwxwzabcdefghijklmnopqrstuvwxwzabcdef"
                                  "ghijklmnopqrstuvwxwzabcdefghijklmnopqrstuvwxwzabcdefghijklmnopqrstuvwxwzabcdefghijkl"
                                  "mnopqrstuvwxwzabcdefghijklmnopqrstuvwxwzabcdefghijklmnopqrstuvwxwzabcdefghijklmnopqr"
                                  "stuvwxwzabcdefghijklmnopqrstuvwxwzabcdefghijklmnopqrstuvwxwzabcdefghijklmnopqrstuvwx"
                                  "wzabcdefghijklmnopqrstuvwxwzabcdefghijklmnopqrstuvwxwzabcdefghijklmnopqrstuvwxwzabcd"
                                  "efghijklmnopqrstuvwxwzabcdefghijklmnopqrstuvwxwzabcdefghijklmnopqrstuvwxwzabcdefghij"
                                  "klmnopqrstuvwxwzabcdefghijklmnopqrstuvwxwzabcdefghijklmnopqrstuvwxwzabcdefghijklmnop"
                                  "qrstuvwxwzabcdefghijklmnopqrstuvwxwzabcdefghijklmnopqrstuvwxwzabcdefghijklmnopqrstuv"
                                  "wxwz")
    print(sol)
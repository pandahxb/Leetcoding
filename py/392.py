class Solution:
    @staticmethod
    def isSubsequence(s: str, t: str) -> bool:
        # Empty s is a subsequence of any string
        if not s:
            return True
        # s is not a subsequence if t is empty
        if not t:
            return False
        i = 0
        for char in t:
            if s[i] == char:
                i += 1
                if i == len(s):
                    return True
        return False

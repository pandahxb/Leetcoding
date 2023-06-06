class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if str1 + str2 != str2 + str1:
            return ""
        return str1[:self.gcd(len(str1), len(str2))]

    def gcd(self, a, b):
        return a if b == 0 else self.gcd(b, a % b)

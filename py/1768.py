class Solution:
    @staticmethod
    def mergeAlternately(word1: str, word2: str) -> str:
        word1 = list(word1)
        word2 = list(word2)
        result = []
        while word1 and word2:
            result.append(word1.pop(0))
            result.append(word2.pop(0))
        if word1:
            result.extend(word1)
        if word2:
            result.extend(word2)
        return "".join(result)

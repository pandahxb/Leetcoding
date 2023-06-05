class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:

        # Different length are not isomorphic
        if len(s) != len(t):
            return False

        # 0 or 1 length strings are isomorphic
        elif (len(s) == 0 and len(t) == 0) or (len(s) == 1 and len(t) == 1):
            return True

        else:
            # Create dictionaries to record the mapping
            s2t = {}
            t2s = {}

            for i in range(len(s)):

                # Not isomorphic if s[i] is already mapped to a different t[i]
                if s[i] in s2t:
                    if s2t[s[i]] != t[i]:
                        return False
                # If s[i] is not mapped, map it to t[i]
                else:
                    s2t[s[i]] = t[i]
                # Not isomorphic if t[i] is already mapped to a different s[i]
                if t[i] in t2s:
                    if t2s[t[i]] != s[i]:
                        return False
                # If t[i] is not mapped, map it to s[i]
                else:
                    t2s[t[i]] = s[i]

            # Otherwise, all mappings are valid, therefore isomorphic
            return True

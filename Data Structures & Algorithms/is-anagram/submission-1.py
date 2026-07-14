class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        checker = {}
        if len(s) != len(t):
            return False
        for i in s:
            checker[i] = checker.get(i,0) + 1
        for j in t:
            if j in checker:
                checker[j] -= 1
                if checker[j] < 0:
                    return False
            else:
                return False
        return True
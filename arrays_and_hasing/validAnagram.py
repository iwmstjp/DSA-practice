class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sMap = {}
        for c in s:
            sMap[c] = 1 + sMap.get(c,0)
        for c in t:
            if c not in sMap:
                return False
            sMap[c] -= 1
        for v in sMap.values():
            if v != 0:
                return False
        return True
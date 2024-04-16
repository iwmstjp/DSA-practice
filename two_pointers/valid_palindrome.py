class Solution:
    def isPalindrome(self, s: str) -> bool:
        ss = []
        for c in s:
            if c.isalnum():
                ss.append(c)
            else:
                continue
        ss = "".join(ss)
        ss = ss.lower()
        return ss == ss[::-1]
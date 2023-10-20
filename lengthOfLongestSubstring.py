class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ans = 0
        cList = []
        for c in s:
            if c not in cList:
                cList.append(c)
            else:
                count = 0
                for cOfcList in cList:
                    if cOfcList == c:
                        count += 1
                        for i in range(count):
                            cList.pop(0)
                        cList.append(c)
                        break
                    else:
                        count += 1
            ans = max(ans, len(cList))
        return ans
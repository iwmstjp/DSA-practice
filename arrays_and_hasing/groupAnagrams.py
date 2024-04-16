class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        strsMap = defaultdict(list)
        for s in strs:
            strsMap["".join(sorted(s))].append(s)
        ans = []
        for key, values in strsMap.items():
            ans.append(values)
        return ans
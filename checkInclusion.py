# 区間のアルファベット26文字の数が同じならTrue
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        s1Count, s2Count = [0] * 26, [0] * 26
        # 最初の区間のアルファベットの数を計算
        for i in range(len(s1)):
            s1Count[ord(s1[i]) - ord("a")] += 1
            s2Count[ord(s2[i]) - ord("a")] += 1
        matches = 0
        # 最初の区間における文字数の一致数を計算
        for i in range(26):
            if s1Count[i] == s2Count[i]:
                matches += 1
        l = 0
        # 最初の区間を除いた区間の計算
        for r in range(len(s1), len(s2)):
            if matches == 26:
                return True
            index = ord(s2[r]) -ord("a")
            s2Count[index] += 1
            # アルファベットの数が同じになったらマッチを増やし、超えてしまったら減らす。
            if s1Count[index] == s2Count[index]:
                matches += 1
            elif s1Count[index] + 1 == s2Count[index]:
                matches -= 1
            # 上の逆
            index = ord(s2[l]) - ord("a")
            s2Count[index] -= 1
            if s1Count[index] == s2Count[index]:
                matches += 1
            elif s1Count[index] - 1 == s2Count[index]:
                matches -= 1
            l += 1
        # 最後の計算はできてないので比較する
        return matches == 26
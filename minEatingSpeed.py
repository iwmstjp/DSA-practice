class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        minSpeed = 1
        maxSpeed = max(piles)
        while minSpeed <= maxSpeed:
            middle = (minSpeed + maxSpeed)//2
            time = 0
            for bananas in piles:
                time += bananas // middle
                if bananas % middle != 0:
                    time += 1
            if time > h:
                minSpeed = middle + 1
            else:
                maxSpeed = middle - 1
        return minSpeed
        
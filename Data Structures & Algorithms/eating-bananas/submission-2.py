
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        s = sum(piles)
        l = math.ceil(s / h)
        r = max(piles) if len(piles) == h else math.ceil((s - 6 * len(piles) ) / (h - len(piles)))
        
        while r > l:
            s = 0
            mid = (l + r) // 2
            for p in piles:
                s += math.ceil(p / mid)
            if s > h:
                l = mid + 1
            else:
                r = mid
        return l
        
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distance = [[(point[0]-0)**2 + (point[1]-0)**2, point] for point in points]
        heapq.heapify(distance)
        res = []
        for i in range(k):
            res.append(heapq.heappop(distance)[1])

        return res
    
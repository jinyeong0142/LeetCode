class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        val_max = 987654321
        ans = -1

        for idx, point in enumerate(points):
            if x == point[0] or y == point[1]:
                if val_max > abs(x-point[0]) + abs(y-point[1]):
                    val_max = abs(x-point[0]) + abs(y-point[1])
                    ans = idx
        
        return ans
        

            
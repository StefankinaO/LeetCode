class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        result = 0
        for i in range(1, len(points)):
            diff1 = abs(points[i][0] - points[i - 1][0])
            diff2 = abs(points[i][1] - points[i - 1][1])
            result = result + max(diff1, diff2);
        
        return result
#label: array difficulty: easy

class Solution:
    def distanceBetweenBusStops(self, distance: List[int], start: int, destination: int) -> int:
        if start < destination:
            a = sum(distance[start:destination])
        else:
            a = sum(distance[destination:start])
        b = sum(distance) - a
        return min(a,b)

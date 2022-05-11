import math
from typing import List


class Solution:
    def minSpeedOnTime(self, dist: List[int], hour: float) -> int:
        def check(speed):
            time_it_takes = 0
            for i, km in enumerate(dist):
                time = km / speed
                time_it_takes += math.ceil(time) if i != len(dist) - 1 else time
            return time_it_takes <= hour

        l, r = 1, 10 ** 7
        while (l < r):
            speed = (l + r) >> 1
            if check(speed):
                r = speed
            else:
                l = speed + 1

        return l if check(l) else -1

dist = [1,3,2]
hour = 2.7
sol = Solution()
speed = sol.minSpeedOnTime(dist, hour)
print(speed)
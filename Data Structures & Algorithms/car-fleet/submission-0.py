class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = sorted(range(len(speed)), 
                            reverse=True, 
                            key=lambda i: position[i])
        ans = len(position) + 1
        current = cars[0]
        for car in cars:
            time_1 = (target - position[car])/speed[car]
            time_2 = (target - position[current])/speed[current]
            if time_1 <= time_2:
                ans -= 1
            else:
                current = car
        return ans

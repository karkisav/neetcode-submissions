class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        P_S = [(p,s) for p, s in zip(position, speed)]
        P_S.sort(reverse=True)
        stack = []
        for p,s in P_S:
            stack.append((target - p) / s)
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
        return len(stack)
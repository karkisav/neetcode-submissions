class Solution:
    def isValid(self, s: str) -> bool:
        opening_bracket = ['(', '{', '[']
        closing_bracket = [')', '}', ']']
        mapping = {')': '(', '}': '{', ']': '['}
        stack = []

        for bracket in s:
            if bracket in opening_bracket:
                stack.append(bracket)
            elif bracket in closing_bracket:
                if not stack or stack.pop() != mapping[bracket]:
                    return False

        if len(stack) != 0:
            return False
        return True
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        index1, index2 = 0, len(numbers) - 1
        while (index1 < index2):
            Val = numbers[index1] + numbers[index2]
            if Val == target:
                return [index1 + 1, index2 + 1]
            
            if Val > target:
                index2 -= 1

            if Val < target:
                index1 += 1
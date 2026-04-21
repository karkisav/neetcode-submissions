class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # 1 every row is sorted
        # for mtx[m][n]
        # 2 mtx[i][0] > mtx[i-1][n] 

        # First search for which row using binary search
        # then a simple binary search in that row

        l ,r = 0, len(matrix) - 1
        
        while l <= r:
            idx = l + (r - l) // 2
            if matrix[idx][0] == target:
                return True
            elif matrix[idx][0] < target:
                l = idx + 1
            else:
                r = idx - 1
        
        row = r
        if row < 0:
            return False
            
        l, r = 0, len(matrix[0]) - 1

        while l <= r:
            idx = l + (r - l) // 2
            if matrix[row][idx] == target:
                return True
            elif matrix[row][idx] < target:
                l = idx + 1
            else:
                r = idx -1

        return False
            
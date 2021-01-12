class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix or not matrix[0]: return False
        def search_matrix(row_lo, row_hi, col_lo, col_hi):
            if row_lo >= row_hi or col_lo >= col_hi: return False
            if row_hi - row_lo == 1 and col_hi - col_lo == 1:
                if matrix[row_lo][col_lo] == target: return True
                else: return False

            row_md, col_md = (row_lo + row_hi) // 2, (col_lo + col_hi) // 2

            pv = matrix[row_md][col_md]

            if pv == target: return True
            elif pv < target:  # discard small area
                return search_matrix(row_lo, row_md + 1, col_md + 1, col_hi) \
                    or search_matrix(row_md + 1, row_hi, col_lo, col_hi)

            else:  # discard big area
                return search_matrix(row_lo, row_md, col_lo, col_hi) \
                    or search_matrix(row_md, row_hi, col_lo, col_md)
        return search_matrix(0, len(matrix), 0, len(matrix[0]))

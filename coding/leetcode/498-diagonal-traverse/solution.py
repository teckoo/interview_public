class Solution:

    def findDiagonalOrder(self, matrix: List[List[int]]) -> List[int]:

        # check for empty matrices
        if not matrix or not matrix[0]: return []

        # get the dimentions of the matrix
        N, M = len(matrix), len(matrix[0])

        # the two arrays in the algorithm
        result, intermediate = [], []

        # We have to go over all the elments in the first row
        # and the last column to cover all possible diagonals
        for d in range(N + M - 1):
            intermediate.clear()

            r = 0 if d < M else d - M + 1
            c = d if d < M else M - 1

            while r < N and c > -1:
                intermediate.append(matrix[r][c])
                r += 1
                c -= 1
            
            # reverse even numbered diagonals
            if d % 2 == 0:
                result.extend(intermediate[::-1])
            else:
                result.extend(intermediate)

        return result
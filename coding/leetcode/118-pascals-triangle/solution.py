class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        triangle = []

        for row_num in range(numRows):
            row = [1 for _ in range(row_num+1)]

            # each triangle element is equal to the sume of the elements
            # above-left and above
            for j in range(1, len(row)-1):
                row[j] = triangle[row_num-1][j-1] + triangle[row_num-1][j]

            triangle.append(row)
        return triangle

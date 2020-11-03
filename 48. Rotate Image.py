class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        n = len(matrix)
        h = ceil(n/2)
        n-=1
        j=co=0
        for i in range(h):
            j=i
            while j<n:
                temp = matrix[i][j]
                matrix[i][j] = matrix[n-j+co][i]
                matrix[n-j+co][i] = matrix[n][n-j+co]
                matrix[n][n-j+co] = matrix[j][n]
                matrix[j][n] = temp

                j+=1
            n-=1
            co+=1
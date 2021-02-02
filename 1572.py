class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        main_diag, poboch_diag = 0, 0
        for i in range(len(mat)):
            if i != len(mat) - i - 1:
                main_diag += mat[i][i]
                main_diag += mat[i][len(mat) - i - 1]
            elif mat[i][i] == mat[i][len(mat) - i - 1]:
                poboch_diag += mat[i][i]
        return main_diag + poboch_diag
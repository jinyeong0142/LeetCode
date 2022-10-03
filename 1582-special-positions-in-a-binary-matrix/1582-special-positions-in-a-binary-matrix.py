class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        row_length = len(mat)
        answer = 0
        
        for i in range(row_length):
            col_length = len(mat[i])
            for j in range(col_length):
                if mat[i][j] != 1:
                    continue
                col = [tmp[j] for tmp in mat]
                if sum(mat[i]) == 1 and sum(col) == 1:
                    answer = answer + 1
                
        return answer
        
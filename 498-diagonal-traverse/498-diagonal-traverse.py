from collections import defaultdict

class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        mat_dict = defaultdict(list)
        
        row_length = len(mat)
        
        for i in range(row_length):
            col_length = len(mat[i])
            
            for j in range(col_length):
                mat_dict[i+j].append(mat[i][j])

        answer = []
        
        for idx, val in enumerate(sorted(mat_dict.keys())):
            if idx % 2 == 0:
                answer.extend(mat_dict[val][::-1])
            else:
                answer.extend(mat_dict[val])
            
        return answer
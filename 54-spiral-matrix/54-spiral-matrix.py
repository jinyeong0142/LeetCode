class Solution:
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
    
    visit = None
    matrix = None
    
    answer = []
    
    def dfs(self, y, x, direction):
        self.visit[y][x] = True
        self.answer.append(self.matrix[y][x])
        
        for i in range(4):
            nexty = self.dy[(direction + i) % 4]
            nextx = self.dx[(direction + i) % 4]
            if y + nexty < 0 or y + nexty >= len(self.matrix) or x + nextx < 0 or x + nextx >= len(self.matrix[y+nexty]) or self.visit[y+nexty][x+nextx] is True:
                continue
            self.dfs(y+nexty, x+nextx, (direction + i)%4)
            
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        self.matrix = matrix
        self.answer = []
        self.visit = [[False for y in range(len(matrix[x]))] for x in range(len(matrix))]
        
        self.dfs(0, 0, 0)
            
        return self.answer
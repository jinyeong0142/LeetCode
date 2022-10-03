class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        
        answer = True
        
        if len(coordinates) == 2:
            answer = True
        else:
            if coordinates[1][0] - coordinates[0][0] == 0:
                x_val = coordinates[0][0]
                for i in range(len(coordinates)):
                    if coordinates[i][0] != x_val:
                        answer = False
                        break
            else:
                a = ((coordinates[1][1] - coordinates[0][1])) / (coordinates[1][0] - coordinates[0][0])
                b = coordinates[0][1] - a * coordinates[0][0]
                for i in range(len(coordinates)):
                    if coordinates[i][1] - a * coordinates[i][0] - b != 0:
                        answer = False
                        break
        
        return answer
                
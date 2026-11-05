import random

class Conway:
    current = 0
    next = 1
    def __init__(self, rows, cols):
        self.rows, self.cols = rows, cols
        self.grid = [[[0 for _ in range(2)] for _ in range(cols)] for _ in range(rows)]

    def initRandom(self):
        for x in range(self.rows):
            for y in range(self.cols):
                self.grid[x][y][0] = random.randint(0,1)


    def initGlider(self, cx, cy):
        self.grid[cx][cy+1][self.current] = 1
        self.grid[cx+1][cy+2][self.current] = 1
        self.grid[cx+2][cy][self.current] = 1
        self.grid[cx+2][cy+1][self.current] = 1
        self.grid[cx+2][cy+2][self.current] = 1




    def neighbourCount(self, row, col):
        sum = 0
        for i in range(-1,2):
            for j in range(-1,2):
                if (i == 0 and j == 0):
                    continue
                neighbour_row = (row+i) % self.rows
                neighbour_col = (col+j) % self.cols
                sum += self.grid[neighbour_row][neighbour_col][self.current]
        return sum

    def updateGrid(self):
        for row in range(self.rows):
            for col in range(self.cols):  
                cell = self.grid[row][col]
                neighbours = self.neighbourCount(row,col)

                if cell[self.current] == 1:
                    if neighbours < 2:      #underpopulation
                        cell[self.next] = 0
                        continue

                    elif neighbours > 3:    #overpopulation 
                        cell[self.next] = 0
                        continue
                
                elif cell[self.current] == 0:
                    if neighbours == 3:     #reproduction
                        cell[self.next] = 1
                        continue

                #pass on
                cell[self.next] = cell[self.current]
        self.current, self.next = self.next, self.current



                 
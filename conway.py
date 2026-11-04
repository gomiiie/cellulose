import random

class Conway:
    self.current = 0
    self.next = 1
    def __init__(self, grid_x, grid_y):
        self.grid_x, self.grid_y = grid_x, grid_y
        self.grid = [[[0 for _ in range(2)] for _ in range(grid_y)] for _ in range(grid_x)]

    def randomInit(self):
        for x in range(self.grid_x):
            for y in range(self.grid_y):
                self.grid[x][y][0] = random.randint(0,1)

    def neighbourCount(self, x, y):
        sum = 0
        for i in range(3):
            for j in range(3):
                if (i == 1 and j == 1):
                    continue
                sum += self.grid[x+i-1][y+j-1][self.current]
        return sum

    def updateGrid(self):
        for x in range(self.grid_x):
            for y in range(self.grid_y):
                cell = self.grid[x][y]
                neighbours = self.neighbourCount(x,y)

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



                 
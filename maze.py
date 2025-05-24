from cell import Cell
import time
import random
from window import Window

class Maze():
    def __init__(
        self,
        x1,
        y1,
        num_rows,
        num_cols,
        cell_size_x,
        cell_size_y,
        win=None,
        seed=None
    ):
        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self.win = win
        self.__cells = []
        if seed:
            self._seed = seed
        else:
            self._seed = random.seed(seed)
        self.__create_cells()
        self.__break_entrance_and_exit()
        self.__break_walls_r(0, 0)
        self.__reset_cells_visited()
        
    def __create_cells(self):
        n_cells = self.num_rows * self.num_cols
        for i in range(self.num_cols):
            column = []
            self.__cells.append(column)
            
            # Fill the column with cells for each row                                                                                                                                                                                                                
            for j in range(self.num_rows):
                # Calculate position for this cell
                x = self.x1 + i * self.cell_size_x
                y = self.y1 + j * self.cell_size_y
                
                # Create new cell
                cell = Cell(x, y, self.cell_size_x, self.cell_size_y, self.win)
                column.append(cell)
                
                # Draw the cell
                if self.win:
                    self.__draw_cell(i, j)
    
    def __draw_cell(self, i, j):
        cell = self.__cells[i][j]
        cell.draw()
        self.__animate()
    
    def __animate(self):
        if self.win:
            self.win.redraw()
            time.sleep(0.01)
        
    def __break_entrance_and_exit(self):
        
        self.__cells[0][0].has_top_wall = False
        self.__cells[0][0].draw()
        self.__cells[-1][-1].has_bottom_wall = False
        self.__cells[-1][-1].draw()
        
    def __break_walls_r(self, i, j):

        cell = self.__cells[i][j]
        cell.visited = True
        while True:
            neighbors = []
            if i > 0 and not self.__cells[i - 1][j].visited:
                neighbors.append((i - 1,j))
            if i < self.num_cols - 1 and not self.__cells[i + 1][j].visited:
                neighbors.append((i + 1,j))
            if j > 0 and not self.__cells[i][j - 1].visited:
                neighbors.append((i, j - 1))
            if j < self.num_rows - 1 and not self.__cells[i][j + 1].visited:
                neighbors.append((i, j + 1))
                
            if len(neighbors) == 0:
                self.__draw_cell(i,j)
                return
            
            # Randomly select a neighbor
            neighbor = random.choice(neighbors)
            
            # Break the wall between the current cell and the neighbor
            neighbor_i, neighbor_j = neighbor
            
            if neighbor_i < i:
                cell.has_left_wall = False
                self.__cells[neighbor_i][neighbor_j].has_right_wall = False
            elif neighbor_i > i:
                cell.has_right_wall = False
                self.__cells[neighbor_i][neighbor_j].has_left_wall = False
            elif neighbor_j < j:
                cell.has_top_wall = False
                self.__cells[neighbor_i][neighbor_j].has_bottom_wall = False
            elif neighbor_j > j:
                cell.has_bottom_wall = False
                self.__cells[neighbor_i][neighbor_j].has_top_wall = False
                
            self.__break_walls_r(neighbor_i, neighbor_j)
            
            
    def __reset_cells_visited(self):
        for i in range(self.num_cols):
            for j in range(self.num_rows):
                self.__cells[i][j].visited = False
        
    def _solve_r(self, i, j):
        self.__animate()

        # vist the current cell
        self.__cells[i][j].visited = True

        # if we are at the end cell, we are done!
        if i == self.num_cols - 1 and j == self.num_rows - 1:
            return True

        # move left if there is no wall and it hasn't been visited            
        if (
                i > 0
                and not self.__cells[i][j].has_left_wall
                and not self.__cells[i - 1][j].visited
            ):
                self.__cells[i][j].draw_move(self.__cells[i - 1][j])
                if self._solve_r(i - 1, j):
                    return True
                else:
                    self.__cells[i][j].draw_move(self.__cells[i - 1][j], True)

            # move right if there is no wall and it hasn't been visited
        if (
                i < self.num_cols - 1
                and not self.__cells[i][j].has_right_wall
                and not self.__cells[i + 1][j].visited
            ):
                self.__cells[i][j].draw_move(self.__cells[i + 1][j])
                if self._solve_r(i + 1, j):
                    return True
                else:
                    self.__cells[i][j].draw_move(self.__cells[i + 1][j], True)

        # move up if there is no wall and it hasn't been visited
        if (
                j > 0
                and not self.__cells[i][j].has_top_wall
                and not self.__cells[i][j - 1].visited
            ):
                self.__cells[i][j].draw_move(self.__cells[i][j - 1])
                if self._solve_r(i, j - 1):
                    return True
                else:
                    self.__cells[i][j].draw_move(self.__cells[i][j - 1], True)

            # move down if there is no wall and it hasn't been visited
        if (
                j < self.num_rows - 1
                and not self.__cells[i][j].has_bottom_wall
                and not self.__cells[i][j + 1].visited
            ):
                self.__cells[i][j].draw_move(self.__cells[i][j + 1])
                if self._solve_r(i, j + 1):
                    return True
                else:
                    self.__cells[i][j].draw_move(self.__cells[i][j + 1], True)

        return False

    # create the moves for the solution using a depth first search
    def solve(self):
        return self._solve_r(0, 0)
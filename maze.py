from cell import Cell
import time

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
    ):
        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self.win = win
        self.__cells = []
        self.__create_cells()
        self.__break_entrance_and_exit()
        
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
        self.win.redraw()
        time.sleep(0.02)
        
    def __break_entrance_and_exit(self):
        
        self.__cells[0][0].has_top_wall = False
        self.__cells[0][0].draw()
        self.__cells[-1][-1].has_bottom_wall = False
        self.__cells[-1][-1].draw()
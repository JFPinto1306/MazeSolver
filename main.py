from window import Window
from point_and_line import Point, Line
from cell import Cell



def main():
    win = Window(800, 600)
    cell = Cell(100,200, 300, 400, win)
    cell.has_right_wall = False
    
    cell2 = Cell(200,300, 300, 400, win)
    cell2.has_top_wall = False
    cell2.has_left_wall = False
    cell2.has_right_wall = False
    
    cell.draw()
    cell2.draw()


    cell.draw_move(cell2)

    win.wait_for_close()
    
    

if __name__ == "__main__":
    main()
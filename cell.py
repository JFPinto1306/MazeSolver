from point_and_line import Line, Point
import random
class Cell:
    def __init__(self, x1, y1, width, height, win=None,seed=None):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self._x1 = x1
        self._y1 = y1
        self._x2 = x1 + width
        self._y2 = y1 + height
        self._win = win
        self.visited = False
        if seed:
            self._seed = seed
        else:
            self._seed = random.seed(seed)
        self._center = Point((self._x1 + self._x2) / 2, (self._y1 + self._y2) / 2)
        
    def draw(self,fill_color="black"):
        if self._win:
            if self.has_left_wall:
                self._win.draw_line(Line(Point(self._x1, self._y1), Point(self._x1, self._y2)))
            else:
                self._win.draw_line(Line(Point(self._x1, self._y1), Point(self._x1, self._y2)), fill_color='white')
                
            if self.has_right_wall:
                self._win.draw_line(Line(Point(self._x2, self._y1), Point(self._x2, self._y2)))
            else:
                self._win.draw_line(Line(Point(self._x2, self._y1), Point(self._x2, self._y2)), fill_color='white')
            
            if self.has_top_wall:
                self._win.draw_line(Line(Point(self._x1, self._y1), Point(self._x2, self._y1)))
            else:
                self._win.draw_line(Line(Point(self._x1, self._y1), Point(self._x2, self._y1)), fill_color='white')
                
            if self.has_bottom_wall:
                self._win.draw_line(Line(Point(self._x1, self._y2), Point(self._x2, self._y2)))
            else:
                self._win.draw_line(Line(Point(self._x1, self._y2), Point(self._x2, self._y2)), fill_color='white')
            
    def draw_move(self, to_cell, undo=False):
        if undo:
            fill_color = 'gray'
        else:
            fill_color = 'red'
            
        if self._win:
            self._win.draw_line(Line(self._center, to_cell._center), fill_color=fill_color)
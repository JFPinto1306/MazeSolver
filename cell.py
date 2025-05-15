from point_and_line import Line, Point

class Cell:
    def __init__(self,_x1,_x2,_y1,_y2,_win):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self._x1 = _x1
        self._x2 = _x2
        self._y1 = _y1
        self._y2 = _y2
        self._win = _win
        self._center = Point((self._x1 + self._x2) / 2, (self._y1 + self._y2) / 2)
        
    def draw(self,fill_color="black"):
        if self.has_left_wall:
            self._win.draw_line(Line(Point(self._x1, self._y1), Point(self._x1, self._y2)))
        if self.has_right_wall:
            self._win.draw_line(Line(Point(self._x2, self._y1), Point(self._x2, self._y2)))
        if self.has_top_wall:
            self._win.draw_line(Line(Point(self._x1, self._y1), Point(self._x2, self._y1)))
        if self.has_bottom_wall:
            self._win.draw_line(Line(Point(self._x1, self._y2), Point(self._x2, self._y2)))
            
    def draw_move(self, to_cell, undo=False):
        if undo:
            fill_color = 'gray'
        else:
            fill_color = 'red'
        self._win.draw_line(Line(self._center, to_cell._center), fill_color=fill_color)
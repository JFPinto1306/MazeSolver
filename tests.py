from maze import Maze
import unittest

class Tests(unittest.TestCase):
    def test_maze_create_cells(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(
            len(m1._Maze__cells),
            num_cols,
        )
        self.assertEqual(
            len(m1._Maze__cells[0]),
            num_rows,
        )
    
    def test_break_entrance_and_exit(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        m1._Maze__break_entrance_and_exit()
        self.assertFalse(m1._Maze__cells[0][0].has_top_wall)
        self.assertFalse(m1._Maze__cells[-1][-1].has_bottom_wall)
        
    def test_break_walls_r(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        m1._Maze__break_entrance_and_exit()
        m1._Maze__break_walls_r(0, 0)
        
        # Check if all cells are visited
        for i in range(num_cols):
            for j in range(num_rows):
                self.assertTrue(m1._Maze__cells[i][j].visited)
                
        self.assertTrue(m1._Maze__cells[0][0].visited)
        self.assertTrue(m1._Maze__cells[-1][-1].visited)   
        
    def test_maze_reset_cells_visited(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        for col in m1._Maze__cells:
            for cell in col:
                self.assertEqual(
                    cell.visited,
                    False,
                )
        
                
        
        
        
if __name__ == "__main__":
    unittest.main()
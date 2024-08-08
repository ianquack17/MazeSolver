import unittest
from maze import Maze
from llstack import LLStack
from node import Node


class LLStackTest(unittest.TestCase):

    def test_stack_init(self):
        ls1 = LLStack()
        self.assertEqual(ls1.head, None)
        self.assertEqual(ls1.size, 0)

    def test_stack_push(self):
        ls2 = LLStack()
        ls2.push((1, 1))
        self.assertEqual(type(ls2.head), Node)
        self.assertEqual(ls2.head.data, (1, 1))
        self.assertEqual(ls2.size, 1)

    def test_stack_pop(self):
        ls3 = LLStack()
        ls3.push((1, 1))
        ls4 = LLStack()
        self.assertEqual(ls3.pop(), (1, 1))
        with self.assertRaises(IndexError):
            ls4.pop()

    def test_stack_copy(self):
        ls5 = LLStack()
        ls5.push((1, 1))
        ls5.push((2, 2))
        ls5.push((3, 3))
        copy = ls5.copy()
        self.assertEqual(copy.size, ls5.size)
        self.assertEqual(copy.head.data, ls5.head.data)
        self.assertEqual(str(copy), str(ls5))

    def test_stack_checked(self):
        ls6 = LLStack()
        ls6.push((1, 1))
        ls6.push((2, 2))
        ls6.push((3, 3))
        ls7 = LLStack()
        self.assertEqual(ls6.checked_node((1, 1)), True)
        self.assertEqual(ls6.checked_node((1, 2)), False)
        self.assertEqual(ls7.checked_node((1, 1)), False)

    def test_stack_lt(self):
        ls8 = LLStack()
        ls9 = LLStack()
        ls8.push((1, 1))
        self.assertEqual((ls9 < ls8), True)
        self.assertEqual((ls8 < ls9), False)
        self.assertEqual((ls8 < ls8), False)

    def test_stack_str(self):
        ls10 = LLStack()
        ls10.push((1, 1))
        ls10.push((2, 2))
        ls10.push((3, 3))
        exp_str = '(3,3) -> (2,2) -> (1,1)'
        self.assertEqual(exp_str, str(ls10))
        self.assertEqual(str(LLStack()), '')


class MazeTest(unittest.TestCase):

    grid = [['o' for _ in range(5)] for _ in range(5)]
    entry = (0, 0)
    exit = (4, 4)

    def test_maze_init(self):
        m1 = Maze(self.grid, self.entry, self.exit)
        self.assertEqual(m1.entry_coords, (0, 0))
        self.assertEqual(m1.exit_coords, (4, 4))
        self.assertEqual(m1.ncols, 5)
        self.assertEqual(m1.nrows, 5)
        self.assertEqual(m1.path, None)
        self.assertEqual(m1.shortest_path, None)
        self.assertEqual(m1.stacks, [])

    def test_grid_error(self):
        g2 = ''
        g3 = [1, 2, 3, 4]
        g4 = [[1], [2], [3], [4]]
        g5 = [['t'], ['o'], ['o'], ['o']]
        with self.assertRaises(TypeError):
            m1 = Maze(g2, (0, 0), (1, 1))
        with self.assertRaises(TypeError):
            m1 = Maze(g3, (0, 0), (1, 1))
        with self.assertRaises(TypeError):
            m1 = Maze(g4, (0, 0), (1, 1))
        with self.assertRaises(ValueError):
            m1 = Maze(g5, (0, 0), (1, 1))

    def test_nrows_error(self):
        g1 = [['o' for _ in range(5)] for _ in range(5)]
        m1 = Maze(g1, (0, 0), (1, 0))
        with self.assertRaises(TypeError):
            m1.nrows = 'i'
        with self.assertRaises(ValueError):
            m1.nrows = 2

    def test_ncols_error(self):
        g1 = [['o' for _ in range(5)] for _ in range(5)]
        m1 = Maze(g1, (0, 0), (1, 0))
        with self.assertRaises(TypeError):
            m1.ncols = 'i'
        with self.assertRaises(ValueError):
            m1.ncols = 2

    def test_entry_coord_error(self):
        pass

    def test_exit_coord_error(self):
        pass

    def test_nrows_getter(self):
        pass

    def test_nrows_setter(self):
        pass

    def test_ncols_getter(self):
        pass

    def test_ncols_setter(self):
        pass

    def entry_coords_getter(self):
        pass

    def entry_coords_setter(self):
        pass

    def exit_coords_getter(self):
        pass

    def exit_coords_setter(self):
        pass

    def test_path_getter(self):
        pass

    def test_shortest_getter(self):
        pass




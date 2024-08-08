from typing import List
from llstack import LLStack


class Maze:
    """
    A class representing a Maze and how to solve it.

    Attributes:
        __nrows(int): the number of cells tall the maze is
        __ncols(int): the number of cells wide the maze is
        __entry(tuple): the indices of the entry point of the maze in the form (row, col).
        __exit(tuple): the indices of the exit point of the maze in the form (row, col).
        __grid(List): the underlying grid storing the maze. Spots with a 'o' are open and spots with an 'x' are walls.
        __path(LLStack): the path through the maze.
        __shortest_path(LLStack): the shortest path through the maze.
    """

    def __init__(self, grid: List[List[str]], entry_loc: tuple, exit_loc: tuple):
        """
        Constructor for Maze.

        Parameters:
            grid(List[List[str]]): the underlying grid storing the maze.
            entry_loc(tuple): the indices of the entry point of the maze in the form (row, col).
            exit_loc(tuple): the indices of the exit point of the maze in the form (row, col).

        Raises:
            TypeError: if the grid, nrows, ncols, entry, or exit contain the wrong type.
            ValueError: if grid, nrows, or ncols contain an incorrect value.
            InvalidCoordinateError: if the entry or exit coordinates are out of bounds or on a wall.
        """

        self.__nrows: int = 3
        self.__ncols: int = 3
        self.__entry: tuple = entry_loc
        self.__exit: tuple = exit_loc
        self.__grid: List[List[str]] = grid
        self.__path: LLStack = None
        self.__shortest_path: LLStack = None
        self.stacks = []

        # Error check grid
        accepted_grid = ['x', 'o']
        if not isinstance(grid, list):
            raise TypeError
        for lst in grid:
            if not isinstance(lst, list):
                raise TypeError
            for string in lst:
                if not isinstance(string, str):
                    raise TypeError
                if string not in accepted_grid:
                    raise ValueError

        # Error check nrows
        if not isinstance(self.__nrows, int):
            raise TypeError
        if self.__nrows < 3:
            raise ValueError

        # Error check ncols
        if not isinstance(self.__ncols, int):
            raise TypeError
        if self.__ncols < 3:
            raise ValueError

        # Error check entry coordinates
        if not isinstance(self.__entry, tuple):
            raise TypeError
        if not 0 <= self.__entry[0] < len(self.__grid):
            raise InvalidCoordinateError
        if not 0 <= self.__entry[1] < len(self.__grid[0]):
            raise InvalidCoordinateError
        if self.__grid[self.__entry[0]][self.__entry[1]] == 'x':
            raise InvalidCoordinateError

        # Error check exit coordinates
        if not isinstance(self.__exit, tuple):
            raise TypeError
        if not 0 <= self.__exit[0] < len(self.__grid):
            raise InvalidCoordinateError
        if not 0 <= self.__exit[1] < len(self.__grid[0]):
            raise InvalidCoordinateError
        if self.__grid[self.__exit[0]][self.__exit[1]] == 'x':
            raise InvalidCoordinateError

        # Set nrows and ncols to the length of grid
        self.nrows = len(grid)
        self.ncols = len(grid[0])

    # Properties
    @property
    def nrows(self):
        """
        int: returns the number of rows in the grid.
        """

        return self.__nrows

    @nrows.setter
    def nrows(self, new_rows: int):
        """
        Sets the number of rows in the grid.

        Parameters:
            new_rows(int): integer representing the new number of rows in the grid.

        Raises:
            TypeError: if new_rows is not an integer.
            ValueError: if new_rows is too small
        """

        if not isinstance(new_rows, int):
            raise TypeError
        if new_rows < 3:
            raise ValueError
        self.__nrows = new_rows

    @property
    def ncols(self):
        """
        int: returns the number of columns tall the grid is.
        """

        return self.__ncols

    @ncols.setter
    def ncols(self, new_cols: int):
        """
        Sets the number of columns in the grid.

        Parameters:
            new_cols(int): integer representing the new number of columns in the grid.

        Raises:
            TypeError: if new_cols is not an integer.
            ValueError: if new_cols is too small
        """

        if not isinstance(new_cols, int):
            raise TypeError
        if new_cols < 3:
            raise ValueError
        self.__ncols = new_cols

    @property
    def entry_coords(self):
        """
        tuple: returns the entry coordinates for the grid.
        """

        return self.__entry

    @entry_coords.setter
    def entry_coords(self, new_coords: tuple):
        """
        Sets the entry coordinates to a new location.

        Parameters:
            new_coords(tuple): new coordinates for the entry to the maze.

        Raises:
            TypeError: if new_coords are not a tuple.
            InvalidCoordinateError: if entry coordinates are out of bounds or on a wall.
        """

        if not isinstance(new_coords, tuple):
            raise TypeError
        if not 0 <= self.__entry[0] < len(self.__grid):
            raise InvalidCoordinateError
        if not 0 <= self.__entry[1] < len(self.__grid[0]):
            raise InvalidCoordinateError
        if self.__grid[self.__entry[0]][self.__entry[1]] == 'x':
            raise InvalidCoordinateError

    @property
    def exit_coords(self):
        return self.__exit

    @exit_coords.setter
    def exit_coords(self, new_exit_coords: tuple):
        """
        Sets the exit coordinates to a new location.

        Parameters:
            new_exit_coords(tuple): new coordinates for the exit to the maze.

        Raises:
            TypeError: if new_exit_coords are not a tuple.
            InvalidCoordinateError: if exit coordinates are out of bounds or on a wall.
        """

        if not isinstance(new_exit_coords, tuple):
            raise TypeError
        if not 0 <= self.__exit[0] < len(self.__grid):
            raise InvalidCoordinateError
        if not 0 <= self.__exit[1] < len(self.__grid[0]):
            raise InvalidCoordinateError
        if self.__grid[self.__exit[0]][self.__exit[1]] == 'x':
            raise InvalidCoordinateError

    @property
    def path(self):
        """
        LLStack: returns the path to the exit of the maze.
        """

        return self.__path

    @property
    def shortest_path(self):
        """
        LLStack: returns the shortest path to the exit of the maze.
        """

        return self.__shortest_path

    def solve(self):
        """
        Top level method to solve the Maze.

        Returns:
            None: if there is no solution.
            LLStack: stack holding the coordinates of the path.
        """

        # Initialize row and column
        row = self.entry_coords[0]
        col = self.entry_coords[1]

        self.__solve_helper(row, col, LLStack())
        if len(self.stacks) == 0:
            return self.__path  # Return None if no path was found
        else:
            self.__path = self.stacks[0]
        return self.__path  # Return the first path found if there was one

    def __solve_helper(self, row: int, col: int, stack: LLStack):
        """
        Recursive helper for solve method that checks every possible path of the maze.

        Parameters:
            row(int): integer representing the row of the current cell location being checked.
            col(int): integer representing the column of the current cell location being checked.
            stack(LLStack): stack used to store each path and movement.

        Returns:
            left: recursive call to check the cell to the left.
            right: recursive call to check the cell to the right.
            up: recursive call to check the cell above.
            down: recursive call to check the cell below.
        """

        # Check if path was visited
        if stack.checked_node((row, col)) is True:
            return  # End path if the cell is already in the current stack
        # Check if exit was found
        if row == self.exit_coords[0] and col == self.exit_coords[1]:
            stack.push((row, col))  # Add current location to the stack
            self.stacks.append(stack.copy())  # Append stack to possible paths if exit was found
            return  # End Path
        # Check if out of bounds
        if row < 0 or col < 0 or row >= len(self.__grid) or col >= len(self.__grid[0]):
            return  # End path
        # Check if hitting a wall
        if self.__grid[row][col] == 'x':
            return  # End path

        # Add cell to the stack
        stack.push((row, col))

        # Move to the left
        left = self.__solve_helper(row + 1, col, stack.copy())
        if left:
            return left  # Return left if a move is possible
        # Move to the right
        right = self.__solve_helper(row, col + 1, stack.copy())
        if right:
            return right  # Return right if a move is possible
        # Move up
        up = self.__solve_helper(row - 1, col, stack.copy())
        if up:
            return up  # Return up if a move is possible
        # Move down
        down = self.__solve_helper(row, col - 1, stack.copy())
        if down:
            return down  # Return down if a move is possible

    def solve_shortest(self):
        """
        Top level method to solve the maze and find the shortest path to the exit.

        Returns:
            shortest(LLStack): the shortest stack to the exit.
            []: if no solution was possible.
        """

        # Initiate row and column
        row = self.entry_coords[0]
        col = self.entry_coords[1]

        # Call solve helper to find all solutions
        self.__solve_helper(row, col, LLStack())

        # Find the shortest out of all solutions if possible
        try:
            shortest = min(self.stacks)
        except ValueError:
            return []
        # Set shortest path to the shortest path
        self.__shortest_path = shortest

        return shortest


class InvalidCoordinateError(Exception):
    pass

import os
import sys
import time

import pandas as pd

backup = sys.stdout
if os.path.exists('files\\mytimes.txt'):
    os.remove('files\\mytimes.txt')
    os.remove('files\\solutions.csv')


class PySudoku:

    def __init__(self, nums: str, fname='files\solutions.csv', dims=None, matrix=None):
        self.fname = fname
        myGrid = []
        dims = int(len(nums) ** (1 / 2))
        nums = str(nums)
        while nums:
            row = []
            myGrid.append(list(map(int, list(nums[:dims]))))
            nums = nums[dims:]
        self.grid = myGrid
        self.dims = dims

    @property
    def dimensions(self):
        return len(self.grid)

    def possible(self, y, x, n, dimensions):
        for i in range(dimensions):
            if self.grid[y][i] == n:
                return False
        for i in range(dimensions):
            if self.grid[i][x] == n:
                return False
        x0 = (x // int(dimensions ** (1 / 2))) * int(dimensions ** (1 / 2))
        y0 = (y // int(dimensions ** (1 / 2))) * int(dimensions ** (1 / 2))
        for i in range(int(dimensions ** (1 / 2))):
            for j in range(int(dimensions ** (1 / 2))):
                if self.grid[y0 + i][x0 + j] == n:
                    return False
        return True

    def solver(self):
        for y in range(self.dims):
            for x in range(self.dims):
                if self.grid[y][x] == 0:
                    for n in range(1, self.dims + 1):
                        if self.possible(y, x, n, self.dims):
                            self.grid[y][x] = n
                            self.solver()
                        self.grid[y][x] = 0
                    return

        sys.stdout = open(self.fname, 'a')
        print(matrix_to_str(self.grid))


def matrix_to_str(matrix):
    result = ""
    for row in matrix:
        for num in row:
            result += str(num)
    return result


my_csv = pd.read_csv('files\sudoku.csv')
# curr = time.time_ns()

times = {}


def run(start, end, score):
    for i in (my_csv['head'].loc[start: end]):
        time.sleep(1)
        score += 1
        curr = time.time()
        sudoku = PySudoku(i)
        sudoku.solver()
        sys.stdout = backup
        end = time.time()
        solve_time = (round((end - curr) * 1000, 3))
        times_file = open('files\\mytimes.txt', 'a+')
        print(f'{score},{solve_time}', file=times_file)
        times_file.close()
    return score


myscore = run(0, 10, 0)
print('Go')
run(10, 100, myscore - 1)

# Python-Projects
Random Python Projects

* [N-Dimensional Sudoku Solver](sudoku.py)

  * Implements recursion to solve _nxn_ sudoku puzzles. Tested on 4x4, 9x9, 16x16 puzzles. 
  * User can now input a string of integers as they are seen in a sudoku board (with 0's for empty spaces).
  * Program was tested on 10000 sudoku puzzles from [here](https://www.kaggle.com/bryanpark/sudoku). Returned correct results in 47.235 seconds
  * Created animations.py. Currently operated manually. After running sudoku.py, user needs to wait for "Go" coomand in console, and manually execute animations.py. Shows animated graph of solve time for first 100 puzzles
  
* [Password Manager with GUI](password_manager.py)
  * Primitive Password vault. Has login and register features
  * Stores credentials in plain text (working on implementing encryption algorithms)
  * Created using _tkinter_

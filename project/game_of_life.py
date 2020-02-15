""" A python script that perform the Game of Life

..module: game_of_line.py
  :platform: Apple IOS
  :synopsis: This game_of_life is a 2 dimensional list with
  30 rows and 40 columns of 0 that turn on and off to represent the living system.
            Each cell can interact with its state of neighbor in the begining and simulate
            based on the progess of "on" and "off" on the grid through out time.


..module author: Ricky Thai, hieu.thai@wsu.edu

Reviewer: Richard Houghton
Grade provided by Reviewer; 100/100

"""

from sys import argv

def main(argv):
    """Set up initial main function called "main" with initial arguments for the command line.
        This main function stores local parameters that will later passes into other
        function to run the game.
        Param script, init_tick, final_ticks, indexes set up all the initial arguments
        for the command line.
    """
    script = argv[0]
    # first argument on the command line
    init_tick = 0
    # set up the initial tick before the game running
    final_ticks = int(argv[1])
    # set up the final number of ticks-simmulation-as the first argument
    indexes = argv[2:]
    # set up the initial index for the position of ticks on the grid
    row = 30
    col = 80
    grid = [[0] * col for i in range(row)]
    # set up the 2 dimensional grid with 0
    init_grid(grid, indexes)
    #function execution with grid and indexes
    print_grid(grid, row, col)
    #function execution for printing the grid with rows and column
    while final_ticks > init_tick:
    #this while loop set up the final grid where we played the Game
        grid = next_grid(grid, row, col)
        print_grid(grid, row, col)
        init_tick = init_tick + 1

def print_grid(grid, row, col):
    """
    Here we define the print_grid function for printing the initial grid.
    Param grid: the position in the gread
    Param row: setting up row variable
    Param col: setting up col variable
    """
    # Iterate through the rows of the grid.
    for i in range(row):
        # Iterate through the columns of row i.
        for j in range(col):
            # If the cell identified by i,j is a 1 then print x
            # If the cell identified by i,j is a 0 then print x
            if grid[i][j] == 1: print("x", end="")
            if grid[i][j] == 0: print("-", end="")
        # Here we are at the end of the row and we need to have a
        # carriage return to end the row.
        print()
    # Add a carriage return to spearate this grid from any that come next.s
    print()


def init_grid(grid, indexes):
    """
    Here we define the initial grid function where we go through each element
    in the list and split them into row and column identity.
    Param indexes: initial position of ticks that represent by row (i) and column (j)
    Param grid: the position in the gread
    """
    for count in indexes:
        i, j = count.split(":")
        #seting the row i and column j for the indexes later in command line
        grid[int(i) - 1][int(j) - 1] = 1
        #set up the correct poistion of index in the grid

def next_grid(grid, row, col):
    """
    Here we define final grid function where we set the rule for the game
    Param row: set up the row variabl
    Param col: set up the column variable
    Param grid: the position in the gread
    """
    grid_new = [[0] * col for i in range(row)]
    # setting the grid while applying the rules of the game
    for i in range(row - 1):
        for j in range(col - 1):
            neighbors = int(grid[i-1][j-1]) + \
                int(grid[i][j-1]) + int(grid[i+1][j-1]) + \
                int(grid[i+1][j]) + int(grid[i+1][j+1]) + \
                int(grid[i][j+1]) + int(grid[i-1][j+1]) + \
                int(grid[i-1][j])
    # setting up the neighbor for the games from each indexes
            if grid[i][j] == 1 and neighbors < 2:
                grid_new[i][j] = 0
            elif grid[i][j] == 1 and neighbors == 2:
                grid_new[i][j] = 1
            elif grid[i][j] == 1 and neighbors == 3:
                grid_new[i][j] = 1
            elif grid[i][j] == 1 and neighbors > 3:
                grid_new[i][j] = 0
            elif grid[i][j] == 0 and neighbors == 3:
                grid_new[i][j] = 1
    return(grid_new)

if __name__ == '__main__':
# set the variable _name_ and then execute the code found earlier in the file
    main(argv)

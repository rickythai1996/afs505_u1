#def main(argv):
import sys

argv = sys.argv
script = argv[0] #name of the module
ticks = int(argv[1]) #first argument that ask user input for total of ticks
indexes = argv[2:] #second argument that ask user input for indexes in the grid

#first we create the grid of dashes "-"
def init_grid():
    grid = ["-" * 5]*5
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            print(grid[i][j], end=' ')
        print()
    return(grid)

grid = init_grid() 

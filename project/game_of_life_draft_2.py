#This code create a system of argument for the command line
from sys import argv



#for loop for i in object

#first we create the grid of dashes "-"
def init_grid():
    grid = ["0" * 31]*81
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            print(grid[i][j], end=' ')
        print()

def print_grid(grid):
    for row in range(len(grid)):
        for col in range(len(grid[i])):
            if grid[row][col] == 0:
                output += "-"
            else:
                output += "x"
        output = "\n\r"
    print(output, end=" ")
    #print(grid[i][j], end=' ')
#index = init_grid.index()_how do we use this index() to pull out the row:col in the grid

def next_grid(rows, cols, grid, next_grid):
    for row in range(rows):
        for col in range(cols):
            # Get the number of live cells adjacent to the cell at grid[row][col]
            live_neighbors = get_live_neighbors(row, col, rows, cols, grid)

            # If the number of surrounding live cells is < 2 or > 3 then we make the cell at grid[row][col] a dead cell
            if live_neighbors < 2 or live_neighbors > 3:
                next_grid[row][col] = 0
            # If the number of surrounding live cells is 3 and the cell at grid[row][col] was previously dead then make
            # the cell into a live cell
            elif live_neighbors == 3 and grid[row][col] == 0:
                next_grid[row][col] = 1
            # If the number of surrounding live cells is 3 and the cell at grid[row][col] is alive keep it alive
            else:
                next_grid[row][col] = grid[row][col]


#these function constructs manual building blocks of the program
def reader():
    read = input()
    enter = read.split(" ")
    return enter



def split_input(grid_input):
    space = grid_input.split(" ")
    return space

# taking num at the index of x
# spliting on the ':' the first value goes to i
#second goes to j
def parse_index(grid,row,col):
    cell = table[x][y]
    x, y = cell.split(":")

#this code is setting up the rules for the game
def next_grid(rows, cols, grid, next_grid):
    for row in range(rows):
        for col in range(cols):
            # Get the number of live cells adjacent to the cell at grid[row][col]
            live_neighbors = get_live_neighbors(row, col, rows, cols, grid)

            # If the number of surrounding live cells is < 2 or > 3 then we make the cell at grid[row][col] a dead cell
            if live_neighbors < 2 or live_neighbors > 3:
                next_grid[row][col] = 0
            # If the number of surrounding live cells is 3 and the cell at grid[row][col] was previously dead then make
            # the cell into a live cell
            elif live_neighbors == 3 and grid[row][col] == 0:
                next_grid[row][col] = 1
            # If the number of surrounding live cells is 3 and the cell at grid[row][col] is alive keep it alive
            else:
                next_grid[row][col] = grid[row][col]

#this code is for asking user input for the total number of ticks
    #j = grid[]
    #index = grid[i][j]
    #print(row[index], end = ' ')
    #print(col[index])
#for x in indexes:
    #test = x
    #test.split(':')
    #row.append(int(test[0]))
    #col.append(int(test[0]))
    #print(row[index], end = ' ')
    #print(col[index])
    #index = index + 1
#for num in range(ticks):
#    print("x")
def main():
    grid = init_grid()
    read = reader()
    print_grid(read)
    argv = sys.argv
    script = argv[0] #name of the module
    ticks = int(argv[1]) #first argument that ask user input for total of ticks
    indexes = argv[2:] #second argument that ask user input for indexes in the grid
if __name__= "__main__":
    main()

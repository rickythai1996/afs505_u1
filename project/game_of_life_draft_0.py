from sys import argv


def print_grid(grid, n_row, n_col):
    # Iterate through the rows of the grid.
    for i in range(n_row - 1):
        # Iterate through the columns of row i.
        for j in range(n_col - 1):
            # If the cell identified by i,j is a 0 then print
            # a -. If it's a 1 then print an x.s
            if grid[i][j] == 1: print("x", end="")
            if grid[i][j] == 0: print("-", end="")
        # Here we are at the end of the row and we need to have a
        # carriage return to end the row.
        print()
    # Add a carriage return to spearate this grid from any that come next.s
    print()


def init_grid(grid, indexes):
    for count in indexes:
        i, j = count.split(":")
        grid[int(i) - 1][int(j) - 1] = 1

def next_grid(grid, n_row, n_col):
    grid_new = [[0] * n_col for i in range(n_row)]
    for i in range(n_row - 1):
        for j in range(n_col - 1):
            neighbors = int(grid[i-1][j-1]) + \
                int(grid[i][j-1]) + int(grid[i+1][j-1]) + \
                int(grid[i+1][j]) + int(grid[i+1][j+1]) + \
                int(grid[i][j+1]) + int(grid[i-1][j+1]) + \
                int(grid[i-1][j])
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

def main(argv):
    script = argv[0]
    ticks = int(argv[1])
    indexes = argv[2:]
    n_row = 31
    n_col = 81
    grid = [[0] * n_col for i in range(n_row)]
    tick = 0
    init_grid(grid, indexes)
    print_grid(grid, n_row, n_col)
    while ticks > tick:
        grid = next_grid(grid, n_row, n_col)
        print_grid(grid, n_row, n_col)
        tick = tick + 1



if __name__ == '__main__':
    main(argv)

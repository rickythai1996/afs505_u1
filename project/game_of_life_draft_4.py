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

def count_neighbors(rows, cols, grid):
    for row in range(rows):
        for col in range(cols):
            if row + 1 <= rows:
                if grid[row+1][col] == "x" or grid[row+1][col] > 9:
                    grid[row][col] += 1
            if col + 1 <= cols:
                if grid[row][col+1] == "x" or grid[row][col+1] > 9:
                    grid[row][col] += 1
            if row - 1 > 0:
                if grid[row-1][col] == "x" or grid[row-1][col] > 9:
                    grid[row][col] += 1
            if col - 1 > 0:
                if grid[row][col-1] == "x" or grid[row][col-1] > 9:
                    grid[row][col] += 1
    return(grid)

def rules(rows, cols, grid):
    for row in range(rows):
        for col in range(cols):
            if grid[row][col] == "-":
                grid[row][col] = 0
            else:
                grid[row][col] = 10
            grid = get_live_neighbors(row, col, grid)
    grid = update_grid(rows,cols,grid)
    return(grid)

def update_grid(rows, cols, grid):
    for row in range(rows):
        for cols in range(cols):
            if grid[row][col] % 10 < 2:
                grid[row][col] = "-"
            if grid[row][col] % 10 > 3:
                grid[row][col] = "-"
            else:
                grid[row][col] = "x"
    return(grid)

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
    rules(rows, cols, grid)

if __name__ == '__main__':
    main(argv)

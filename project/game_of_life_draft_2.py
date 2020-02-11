#This code create a system of argument for the command line
import sys

#def main(argv):
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
#index = init_grid.index()_how do we use this index() to pull out the row:col in the grid

#this code is for asking user input for the total number of ticks
def print_grid(input):
    for i in range(len(input)):
        for j in range(len(input[i])):
            print(input[i][j], end=' ')
        print()



for x in indexes:
    #create an argument of i and j that represent "n:n"
    i, j = x.split(':')
    grid[int(i)][int(j)] = "x"

print_grid()


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

#if __name__= "__main__":
#    main(agrv)

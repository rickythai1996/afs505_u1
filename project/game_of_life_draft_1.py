def init_grid():

    n = 30 #column is 30
    m = 80 #row is 80
    a = [["-"] * m for i in range(n)] #
    for i in range(n):

        for j in range(n):
            a[i][j] = "-"
    for row in a:
        print(' '.join([str(elem) for elem in row]))

init_grid()

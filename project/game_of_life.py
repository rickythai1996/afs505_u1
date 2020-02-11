def init_grid():

    n = 30 #column is 30
    m = 80 #row is 80
    a = [["-"] * m for i in range(n)]
    for i in range(n):
        a.append('-'*m)
    for j in range(n):
        a[i][j] = "-"
    for row in a:
        print(' '.join([str(elem) for elem in row]))

init_grid()





#for i in range (n):
    #for j in range(m):
        #a[0][j] = ''
        #a[i][0] = ''
        #while index >= 0:
            #a[row[index]][col[index]] = 'x'
            #index = index - 1


#if __name__ == "__main__":
    #print(sys.argv[0])


#argv = sys.argv
#script = argv[0]
#total_ticks = int(argv[1])
#indexes = argv[2:]
#index = []

#for x in indexes:
    #test = x
    #test.split(':')
    #row.append(int(test[0]))
    #col.append(int(test[0]))
    #print(row[index], end = ' ')
    #print(col[index])
    #index = index + 1

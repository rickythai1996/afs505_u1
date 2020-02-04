def main(): # first we define the function "main"
    from sys import argv #we import a local variable
    script, filename = argv #we define 2 argument focus on filename
    filehand = open(filename) #we
    count = 0
    line = filehand.readline()
    words = len(line.split()) #lenght of line and split
    chars = len(line) #lenght of line
    while line:
        count += 1
        line = filehand.readline()
        words += len(line.split())
        chars += len(line)
    print(f"{count}, {words}, {chars}, {filename}")

main() #run the function

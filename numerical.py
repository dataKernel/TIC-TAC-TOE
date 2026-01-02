def     create_grid(exemple: bool = False)-> list:
    
    if (exemple):
        grid = list(range(1, 10))
        for i in range(9):
            #explicit convertion to string for print
            grid[i] = str(grid[i])
    else:
        grid = []
        for i in range(9):
            grid.append(" ")

    return grid

def     print_grid(grid: list)-> None:
    string = ""
    i = 0

    for elem in grid:
        if (i > 2):
            i = 0
            print(string)
            string = ""
        string += '[' + elem + ']'
        i += 1
    if string:
        print(string)

test = create_grid()
print_grid(test)
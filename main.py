def     create_grid()-> list:
    grid = []
    for i in range(3):
        row = []
        for j in range(3):
            row.append("[ ]")
        grid.append(row)
    return grid

def     print_grid(grid: list)-> None:
    
    for row in grid:
        str = ""
        for elem in row:
            str += " " + elem
        print(str)

test = create_grid()
print_grid(test)
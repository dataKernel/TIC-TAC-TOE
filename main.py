def     create_grid(exemple: bool = False)-> list:
    grid = []
    
    if (not exemple):
        for i in range(3):
            row = []
            for j in range(3):
                row.append("[ ]")
            grid.append(row)
    else:
        grid = list(range(1, 10))
    
    return grid

def     print_grid(grid: list)-> None:
    
    for row in grid:
        str = ""
        for elem in row:
            str += " " + elem
        print(str)


test = create_grid(True)
print(test)
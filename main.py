def     create_grid()-> list:
    grid = []
    for i in range(3):
        row = []
        for j in range(3):
            row.append("[ ]")
        grid.append(row)
    return grid

test = create_grid()
print(test)
import  os
from    typing import Tuple
##########################################################################
def     clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

def     create_grid(size: int, exemple: bool = False)-> Tuple[list, int]:
    sizeArrayGrid = size ** 2

    if (exemple):
        grid = list(range(1, sizeArrayGrid + 1))
        for i in range(sizeArrayGrid):
            #explicit convertion to string for print
            grid[i] = str(grid[i])
    else:
        grid = []
        for i in range(sizeArrayGrid):
            grid.append(' ')

    return grid, sizeArrayGrid


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

def     gen_array_freeCell_indexes(grid: list)-> list:
    arrayFreeCell = []

    for index, elem in enumerate(grid):
        if (elem == ' '):
            arrayFreeCell.append(index)

    return arrayFreeCell

def     gen_arrayRows_win_combi(grid: list)-> list:
    rowArray = []
    combi = []
    i = 0

    #row combinations
    for index, elem in enumerate(grid):
        combi.append(index)
        if (i == 2):
            rowArray.append(combi)
            combi = []
            i = 0
        else:
            i += 1
    return rowArray

def     gen_arrayColumns_win_combi(grid: list)-> list:
    columnArray = []
    combi = []
    i = 0
    
    for i in range(3):
        combi = []
        index = i
        combi.append(i)
        for j in range(2):
            index += 3
            combi.append(index)
        columnArray.append(combi)
    
    return columnArray

def     gen_arrayDiag_win_combi(grid: list)-> list:
    diagonalArray = []
    combi = []
    i = 0



def     gen_array_win_combis(grid: list)-> list:
    arrayAllCombis = []
    combi = []
    i = 0

    #adding row winning combinations to array
    arrayAllCombis = gen_arrayRows_win_combi(grid)
    #adding column combinations to array
    arrayAllCombis += gen_arrayColumns_win_combi(grid)
    #diagonal combinations
    for i in range(2):
        combi = []
        if (i == 0):
            index = 0
            combi.append(index)
            for j in range(2):
                index += 3 + 1
                combi.append(index)
            arrayAllCombis.append(combi)
        else:
            index = 3 - 1
            combi.append(index)
            for j in range(2):
                index += 2
                combi.append(index)
            arrayAllCombis.append(combi)

    return arrayAllCombis

def     main():
    print("prog start...")
    gridGame, sizeArraygrid = create_grid(3)
    gridGameEx, sizeArraygridEx = create_grid(3, True)
    print("sizeArrayGrid" + str(sizeArraygrid))
    print(gridGame)
    print("sizeArrayGridEx" + str(sizeArraygridEx))
    print(gridGameEx)
    # arrayAllCombis = gen_array_win_combis(gridGame)

    # print(f"arrayAllcombis: {arrayAllCombis}")
##########################################################################
if (__name__ == "__main__"):
    main()
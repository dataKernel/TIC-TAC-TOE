import  os
from    typing import Tuple
##########################################################################

def     clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

def     create_grid(size:int, exemple:bool = False)-> list:
    
    if (size < 0 or size > 10):
        printf("size isnt correct, prog abort..")
        pass
    
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

    return grid


def     print_grid(grid:list, size:int)-> None:
    string = ""
    i = 0

    for elem in grid:
        if (i == size):
            i = 0
            print(string)
            string = ""
        string += '[' + elem + ']'
        i += 1
    if string:
        print(string)

def     gen_array_freeCell_indexes(grid:list)-> list:
    arrayFreeCell = []

    for index, elem in enumerate(grid):
        if (elem == ' '):
            arrayFreeCell.append(index)

    return arrayFreeCell

def     gen_arrayRows_win_combi(grid:list, size:int)-> list:
    rowArray = []
    combi = []
    i = 0

    #row combinations
    for index, elem in enumerate(grid):
        combi.append(index)
        if (i == size - 1):
            rowArray.append(combi)
            combi = []
            i = 0
        else:
            i += 1
    return rowArray

def     gen_arrayColumns_win_combi(grid:list, size:int)-> list:
    columnArray = []
    combi = []
    i = 0
    
    for i in range(size):
        combi = []
        index = i
        combi.append(i)
        for j in range(size - 1):
            index += size
            combi.append(index)
        columnArray.append(combi)
    
    return columnArray

def     gen_arrayDiags_win_combi(grid:list, size:int)-> list:
    diagonalArray = []
    combi = []
    
    for i in range(2):
        combi = []
        if (i == 0):
            for j in range(0, len(grid), size + 1):
                combi.append(j)
            diagonalArray.append(combi)
        else:
            for j in range(size - 1, size * (size - 1) + 1, size - 1):
                combi.append(j)
            diagonalArray.append(combi)
    
    return diagonalArray


def     gen_array_win_combis(grid:list, size:int)-> list:
    arrayWinCombis = []
    combi = []
    i = 0

    #adding row winning combinations to array
    arrayWinCombis = gen_arrayRows_win_combi(grid, size)
    #adding column combinations to array
    arrayWinCombis += gen_arrayColumns_win_combi(grid, size)
    #adding diagonal combinations to array
    arrayWinCombis += gen_arrayDiags_win_combi(grid, size)
    

    return arrayWinCombis

def     check_winner(grid:list, arrayWinCombis:list, size:int)-> Tuple[bool, str]:
    
    for arrayCombi in arrayWinCombis:
        count = 0
        if (grid[arrayCombi[0]] == ' '):
            continue
        firstElem = grid[arrayCombi[0]]
        for i in range(1, size):
            if (grid[arrayCombi[i]] != firstElem):
                break
            elif (count == size - 1):
                return (True, firstElem)
            count += 1
    return (False, '')
        
    

##########################################################################
def     main():
    print("prog start...")
    #- - - CONSTANTES - - - -
    SIZE_GRID = 3
    #- - - - - - - - - - - -
    gridGame = create_grid(SIZE_GRID)
    gridGame[6] = 'X'
    gridGame[7] = 'X'
    gridGame[8] = 'X'
    gridGameEx = create_grid(SIZE_GRID, True)
    
    print("sizeArrayGrid" + str(SIZE_GRID ** 2))
    print_grid(gridGame, SIZE_GRID)
    print("sizeArrayGridEx" + str(SIZE_GRID ** 2))
    print_grid(gridGameEx, SIZE_GRID)
    
    arrayWinCombis = gen_array_win_combis(gridGame, SIZE_GRID)
    print(f"arrayAllcombis: {arrayWinCombis}")
    win, player = check_winner(gridGame, arrayWinCombis, SIZE_GRID)
    print(f"win: {win}, player: {player}")
if (__name__ == "__main__"):
    main()
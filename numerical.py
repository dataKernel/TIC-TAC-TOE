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

def     check_winner(grid:list, size:int)-> Tuple[bool, str]:
    arrayWinCombis = gen_array_win_combis(grid, size)
    
    for arrayCombi in arrayWinCombis:
        if (grid[arrayCombi[0]] == ' '):
            continue
        firstElem = grid[arrayCombi[0]]
        for i in range(1, size):
            if (grid[arrayCombi[i]] != firstElem):
                break
            elif (i == size - 1):
                return (True, firstElem)
    return (False, '')
        
def     game(size:int)-> None:
    grid = create_grid(size)
    winner = False
    
    round = 0 #numbers of rounds(we start to check combis at 5)
    while (not winner):
        userPosition = ''
        while (True):
            userPosition = input("choose position: ")
            if (not userPosition.isdigit()):
                continue #we reset the loop (user choice is not a digit)
            else:
                userPosition = int(userPosition)
                if (not 0 <= userPosition <= 8):
                    continue #we reset the loop (position is out of range)
                else:
                    break #we end the loop to treat the new posi
        grid[userPosition - 1] = 'X'
        clear_screen()
        print_grid(grid, size)
        round += 1
        print(f"round:{round}")
        if (round >= 5):
            winner, player = check_winner(grid, size)        

##########################################################################
def     main()-> int:
    print("prog start...")
    #- - - CONSTANTS - - - -
    SIZE_GRID = 3
    #- - - - - - - - - - - -
    
    gridGameEx = create_grid(SIZE_GRID, True)
    print("sizeArrayGridEx: " + str(SIZE_GRID ** 2))
    print_grid(gridGameEx, SIZE_GRID)
    game(SIZE_GRID)
    

if (__name__ == "__main__"):
    main()
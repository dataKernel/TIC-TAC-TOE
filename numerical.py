# 🎨 Codes ANSI utiles
# Couleur	Code
# Noir	30
# Rouge	31
# Vert	32
# Jaune	33
# Bleu	34
# Magenta	35
# Cyan	36
# Blanc	37

import      os
import      random
from        typing import Tuple
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
        if elem == 'X':
            string += '[' + "\033[35m" + elem + "\033[0m" + ']'
        elif elem == 'O':
            string += '[' + "\033[31m" + elem + "\033[0m" + ']'
        else:
            string += '[' + "\033[32m" + elem + "\033[0m" + ']'
        i += 1
    if string:
        print(string)

def     gen_array_freePosi_indexes(grid:list)-> list:
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

def     choice_user(grid:list)-> int:
    while (True):
            userPosition = input("choose position: ")
            if (not userPosition.isdigit()):
                continue #we reset the loop (user choice is not a digit)
            else:
                userPosition = int(userPosition) - 1
                if ((not 0 <= userPosition <= 8) or grid[userPosition] != ' '):
                    continue #we reset the loop (position is out of range)
                else:
                    break #we end the loop to treat the new posi
    
    return userPosition

def     computer_diff_1(grid:list)-> None:
    arrayFreePosis = gen_array_freePosi_indexes(grid)

    randomPosi = random.choice(arrayFreePosis)    
    grid[randomPosi] = 'O'
    
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
    gridGameEx = create_grid(size, True)
    winCheck = False
    
    gameRounds = 0 #numbers of game rounds(we start to check combis at 5)
    while (not winCheck):
        print("------------ \033[32mEXEMPLE GRID POSITIONS\033[0m ------------")
        print_grid(gridGameEx, size)
        print("------------------------------------------------")
        #we ask the user to give a position and we test it
        userPosition = choice_user(grid)
        
        grid[userPosition] = 'X'
        computer_diff_1(grid)
        clear_screen()
        print_grid(grid, size)
        gameRounds += 1
        print(f"round:{gameRounds}")
        if (gameRounds >= 5):
            winCheck, winner = check_winner(grid, size)
            if winner == 'X': 
                winner = "\033[35m X \033[0m"
            elif winner == 'O':
                winner = "\033[31m X \033[0m"
            print(f"The \033[32m winner \033[0m is {winner} !")  

##########################################################################
def     main()-> int:
    print("\033[32mprog start\033[0m...")
    #- - - CONSTANTS - - - -
    SIZE_GRID = 3
    #- - - - - - - - - - - -
    game(SIZE_GRID)

if (__name__ == "__main__"):
    main()
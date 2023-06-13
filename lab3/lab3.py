# Här kan du skriva programkod för labb 3.
#
# Programkoden kan t.ex. också delas upp i flera filer, men
# i så fall behöver du se till att de adderas till Git.
def new_board():
    return {}

def is_free(board, x, y):
    return not(x, y) in board

def place_piece(board, x, y, spelare):
    ifall_möjligt = is_free(board, x, y) # ifall möjligt kollar om kord. är tomma
    if ifall_möjligt:
        board[(x, y)] = spelare # kord. (x, y) döps till angiven spelare
    return ifall_möjligt 

def get_piece(board, x, y):
    vem = is_free(board, x, y)
    if not vem: # om kord. är upptagna byts till true så if satsen körs
        return board[(x, y)] # retunerar spelarens nämn
    else:
        return False
    
def remove_piece(board, x, y):
    upptagen = not is_free(board, x, y) # Platsen är upptagen
    if upptagen:
        del board[(x, y)] # ta bort "ägaren" för kord. x och y
        return upptagen
    return False

def move_piece(board, x, y, nx, ny):
    if not is_free(board, x, y) and is_free(board, nx, ny):
        spelare = get_piece(board, x, y)
        remove_piece(board, x, y)
        place_piece(board, nx, ny, spelare)
        return True
    return False

def count(board, diraction, pos, spelare):
    counter = 0
    if diraction == "column": # om column är skriven börja for loop
        for cord in board.keys():
            if cord[0] == pos and get_piece(board, cord[0], cord[1]) == spelare:
                counter += 1
        return counter
    else:
        for cord in board.keys(): # något annat än column kör row
            if cord[1] == pos and get_piece(board, cord[0], cord[1]) == spelare:
                counter += 1
        return counter

def nearest_piece(board, x, y):
    mitt_avstånd = 0
    no_piece = False
    if not is_free(board, x, y): # retunera platsen cord
        return (x,y)
    for i in board.keys(): # kolla i alla keys
        avstånd_formel = ((x-i[0])**2 + (y-i[1])**2)**(1/2)
        if mitt_avstånd == 0:
           mitt_avstånd = avstånd_formel
        if avstånd_formel <= mitt_avstånd:
            mitt_avstånd = avstånd_formel
            no_piece = i
    return no_piece
            
        

   

def factorial(n): 
    if n == 0: # fac(0) = 1
        return 1
    else:
        res_n = n * factorial(n-1) # fac(x) = x * (x-1) * (x-1 -1) 
        return res_n
    
def permitation(n, k): # permitation = n! / k! eller n!/q!
    if n == k: # K elemnt kan väljas på ett sätt av n elemnt
        return 1
    if n <= k+1:
        return k+1
    return n * permitation(n-1, k)

def choose(n, k):
    q= n-k
    perm_result= 0
    if k>= q:
        perm_result= permitation(n, k) // factorial(q) # förenkla uttryket till permitation / fakoltit av (n-k)
    else:
        perm_result= permitation(n, q) // factorial(k) # q är storre då är bättre att köra permitation (n,q)/ fakoltet(k)
    return perm_result


def read_terms(n):
    '''
    Reads an expression containing 'W' and '.' ignoring the others and while checking if it's n*n, from user input.
    
    pre: n>=3
    
    post: new term is valid only if it's length is n*n containing only 'W' and '.'
    
    para n: The size of the board(n * n)
    
    return: newterm - the valide input if all the conditions are met 
    return: None - if the conditions are not met 
    '''    
    term = input(f"Please enter the board of size {n}x{n} with empty squares denoted as . and warriors denoted as W: ")
    
    new_term = ''
    count = 0
    
    for i in term:
        if i == '.' or i == 'W':
            new_term += i
            count += 1
            
    if count != (n*n):
        print(f"The input does not make size {n}x{n} grid! ")
        
        return None
    return new_term

def create_board(new_term, n):
    '''
    creates a 2D board from the valid string input.
    pre: new_term contains nxn characters consisting of only 'W' and '.'
    post: returning a list of lists representing a chess board 
    para: new_term - string containing warriors and empty squares
          n - size of the board(n * n)
    return: board- 2D list representation of the chess board
    '''
    board = []
    value = 0
    for row in range(n):
        current_row = []
        
        for column in range(n):
            current_row.append(new_term[value])
            value += 1
        board.append(current_row)
    return board
        
    
    #option 2 we can use this equation instead of a count 
    #borad = []
    
    #for row in range(n):
        #current_row = []
        
        #for column in range(n):
            #current_row.append(new_term[row* n + column])
        #board.append(current_row)
    #return board
    
    
def print_board(board):
    '''
    prints the chess board row by row
    pre: board is a non-empty 2D list containing only 'W' and '.'
    post: displays the board
    para: board- a 2D list representation of the chess board 
    return: None
    '''
    for row in board:
        for ch in  row:
            print(ch, end='')
        print()
    
    #option 2 
    #for row in board:
        #print("".join(row))

def attack(board):
    '''
    checks whether any two warriors can attack each other 
    
    A warrior can attack by moving 2 steps horizontally or vertically and them 1 step diagonally in any direction 
    
    pre: board is a non-empty 2D list containing only 'W' and '.'
    post: returns true if at least one warrior can attack another warrior 
    para: board- a 2D list representation of the chess board 
    return: true or false 
    '''
    n = len(board)
    
    moves = [(-3,-1), (-3,1), (3, -1), (3, 1), (-1, -3), (1, -3), (-1, 3), (1, 3), (-1, -1), (-1, 1), (1, -1), (1,1)]
    
    for r in range(n):
        for c in range(n):
            #to skip the empty squares 
            
            if board[r][c] != 'W':
                continue 
            
            for dr, dc in moves:
                final_r = r + dr
                final_c = c + dc
                
                #making sure the positions stay inside the board 
                
                if 0 <= final_r < n and 0 <= final_c < n:
                    if board[final_r][final_c] == 'W':
                        return True 
                    
    return False 


def main():
    '''
    Executes the warrior checker program
    pre: user enters an integer n where n>=3
    post: prints the board and whether the warriors can attack each other
    return: None 
    '''
    print(f'Welcome to the chess warrior checker!')
    n = int(input(f'Plese enter the nxn size of the chess board as n: '))
    
    term = read_terms(n)
    
    if term is None:
        return 
    board = create_board(term, n)
    print_board(board)
    
    if attack(board):
        print(f"Warriors can attack each other!")
    else:
        print(f"Sorry, warriors cannot attack each other.")
        
        
    # instead of that we can do this as well
    
    #term = read_term(n)
        
    #if term is None: 
        #return
        
    #board = []
        
    #value = 0 
        
    #for i in range(n):
        #row = []
            
        #for j in range(n):
            #row.append(term[value])
            #value += 1
                
        #board.append(row)
            
            
    #for row in board:
        #for ch in row:
            #print(ch, end ="")
        #print()
                
    #if attack(board):
        #print(f'Warriors can attack each other')
        
    #else:
        
        #print(f'Sorry, warriors cannot attack each other')    
        
if __name__ == "__main__":
    main()

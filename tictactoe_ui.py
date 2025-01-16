class GameUI:
    def show_welcome(self):
        print("Welcome to Tic-tac-toe!")
        print("Use numbers 1-9 to make your move:")
        print("1 | 2 | 3")
        print("---------")
        print("4 | 5 | 6")
        print("---------")
        print("7 | 8 | 9")
        print()
    
    def get_player_choice(self):
        choice = input("Do you want to play as X or O? ").upper()
        while choice not in ['X', 'O']:
            choice = input("Please choose X or O: ").upper()
        return choice
    
    def display_board(self, state):
        for i in range(0, 9, 3):
            row = [cell if cell is not None else str(i + j + 1) 
                  for j, cell in enumerate(state[i:i+3])]
            print(' | '.join(row))
            if i < 6:
                print('---------')
    
    def get_human_move(self, legal_moves):
        while True:
            try:
                move = input("Enter your move (1-9) or 'r' to resign: ")
                if move.lower() == 'r':
                    return 'resign'
                move = int(move) - 1
                if move in legal_moves:
                    return move
                print("Invalid move. Cell already taken or out of range.")
            except ValueError:
                print("Please enter a number between 1 and 9 or 'r' to resign.")
    
    def show_ai_thinking(self):
        print("\nAI is thinking...", end='', flush=True)
    
    def show_ai_done(self):
        print(" done!")
    
    def show_winner(self, winner):
        print(f"\n{winner} won!")
    
    def show_draw(self):
        print("\nIt's a draw!")
    
    def play_again(self):
        return input("\nPlay again? (y/n): ").lower() == 'y' 
    
    def show_resigned(self):
        print("\nYou resigned. AI wins!") 
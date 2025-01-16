from tictactoe_ai import MCTS
from tictactoe_game import TicTacToeGame
from tictactoe_ui import GameUI

def play_game(game, ai):
    """Main game loop."""
    ui = GameUI()
    
    ui.show_welcome()
    human_player = ui.get_player_choice()
    ai_player = 'O' if human_player == 'X' else 'X'
    
    while not game.is_over():
        ui.display_board(game.state)
        
        if game.get_current_player() == human_player:
            # Human move
            move = ui.get_human_move(game.get_legal_moves())
            if move == 'resign':
                game.resign()
                break
            game.make_move(move)
        else:
            # AI move
            ui.show_ai_thinking()
            game.make_move(ai.get_best_move(game))
            ui.show_ai_done()

    # Show final board and result
    ui.display_board(game.state)
    if game.resigned:
        ui.show_resigned()
    elif game.is_winner(human_player):
        ui.show_winner("You")
    elif game.is_winner(ai_player):
        ui.show_winner("AI")
    else:
        ui.show_draw()

    return ui.play_again()

def main():
    # Initialize AI once to maintain memory between games
    ai = MCTS(iterations=5000)
    
    while True:
        # Create new game for each round
        game = TicTacToeGame()
        if not play_game(game, ai):
            break
    
    print("\nThanks for playing!")

if __name__ == "__main__":
    main()

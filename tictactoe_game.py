from typing import List, Tuple

class TicTacToeGame:
    def __init__(self):
        self.state = [None] * 9
        self._current_player = 'X'
        self.resigned = False
    
    def get_current_player(self):
        return self._current_player
    
    def get_legal_moves(self):
        return [i for i, cell in enumerate(self.state) if cell is None]
    
    def make_move(self, position):
        if self.state[position] is None:
            self.state[position] = self._current_player
            self._current_player = 'O' if self._current_player == 'X' else 'X'
            return True
        return False
    
    def is_winner(self, player):
        wins = [
            [0,1,2], [3,4,5], [6,7,8],  # Rows
            [0,3,6], [1,4,7], [2,5,8],  # Columns
            [0,4,8], [2,4,6]            # Diagonals
        ]
        return any(all(self.state[i] == player for i in line) for line in wins)
    
    def is_draw(self):
        return None not in self.state
    
    def resign(self):
        self.resigned = True
    
    def is_over(self):
        return (self.resigned or 
                self.is_winner('X') or 
                self.is_winner('O') or 
                self.is_draw())
    
    def copy(self):
        new_game = TicTacToeGame()
        new_game.state = self.state[:]
        new_game._current_player = self._current_player
        new_game.resigned = self.resigned
        return new_game 
    
    def get_move_history(self) -> List[Tuple[str, int]]:
        """Return list of (player, move) tuples."""
        return self.move_history 
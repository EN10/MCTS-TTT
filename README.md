# Tic-tac-toe with AI

A command-line implementation of Tic-tac-toe featuring an intelligent AI opponent powered by Monte Carlo Tree Search (MCTS).

## Features

- Advanced AI using Monte Carlo Tree Search (MCTS) algorithm
- Intelligent move selection prioritizing:
  - Winning moves
  - Blocking opponent wins
  - Diagonal threat defense
  - Strategic positions (center, corners, edges)
- Choose to play as X or O
- Clear visual representation of the game board
- Option to resign during game
- Play multiple games

## Project Structure

- `tictactoe_main.py` - Main game loop and program entry point
- `tictactoe_game.py` - Game state and rules
- `tictactoe_ai.py` - AI opponent using MCTS
- `tictactoe_ui.py` - User interface and input/output handling

## How to Play

1. Run the game:
   ```bash
   python tictactoe_main.py
   ```

2. Choose to play as X or O (X goes first)

3. Make moves using numbers 1-9:
   ```
   1 | 2 | 3
   ---------
   4 | 5 | 6
   ---------
   7 | 8 | 9
   ```

4. Type 'r' to resign at any time

5. Play until someone wins or it's a draw

6. Choose whether to play again

## Technical Details

### AI Implementation
- Monte Carlo Tree Search (MCTS) with:
  - 5000 iterations per move
  - UCB1 formula for node selection
  - Strategic position evaluation
  - Immediate win/block detection
  - Special handling of diagonal threats

### Game Features
- Full game state management
- Move validation
- Win/draw detection
- Game state copying for AI simulation
- Resignation option

### User Interface
- Clear command-line interface
- Real-time board display
- Input validation
- AI thinking indicators
- Game status messages

## Requirements

- Python 3.6 or higher
- No additional packages required

## License

This project is open source and available under the MIT License.

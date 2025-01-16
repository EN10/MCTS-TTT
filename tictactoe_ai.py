import math
import random
from typing import List, Optional

class Node:
    def __init__(self, game, parent=None):
        self.game = game
        self.parent = parent
        self.children: List[Node] = []
        self.visits: int = 0
        self.wins: float = 0
        self.untried_moves = game.get_legal_moves()

    def get_ucb_score(self, exploration_weight: float) -> float:
        if self.visits == 0:
            return float('inf')
        exploitation = self.wins / self.visits
        exploration = exploration_weight * math.sqrt(2 * math.log(self.parent.visits) / self.visits)
        return exploitation + exploration

class MCTS:
    def __init__(self, iterations: int = 5000):
        self.iterations = iterations

    def get_best_move(self, game) -> int:
        # First move strategy
        if sum(1 for cell in game.state if cell is not None) <= 1:
            return 4 if game.state[4] is None else 0  # Take center or corner

        # Check for critical moves
        critical = self._get_critical_move(game)
        if critical is not None:
            return critical

        # Run MCTS
        root = Node(game)
        for _ in range(self.iterations):
            node = self._select_and_expand(root)
            result = self._simulate(node)
            self._backpropagate(node, result)

        return self._get_best_child_move(root)

    def _get_critical_move(self, game) -> Optional[int]:
        player = game.get_current_player()
        opponent = 'O' if player == 'X' else 'X'
        center, corners = 4, [0, 2, 6, 8]

        # Check for win or block
        for move in game.get_legal_moves():
            test = game.copy()
            test.state[move] = player
            if test.is_winner(player):  # Win
                return move
            test.state[move] = opponent
            if test.is_winner(opponent):  # Block
                return move

        # Handle diagonal threats
        if game.state[center] == opponent:
            # Block opposite corner if opponent has one
            for c in corners:
                if game.state[c] == opponent:
                    opposite = {0:8, 2:6, 6:2, 8:0}[c]
                    if game.state[opposite] is None:
                        return opposite
            
            # Take any empty corner
            empty_corners = [c for c in corners if game.state[c] is None]
            if empty_corners:
                return random.choice(empty_corners)

        # Take center or strategic position
        for pos in [center] + corners + [1,3,5,7]:  # Center, corners, edges
            if game.state[pos] is None:
                return pos

        return None

    def _simulate(self, node: Node) -> float:
        game = node.game.copy()
        current = game.get_current_player()
        
        while not game.is_draw():
            if game.is_winner('X') or game.is_winner('O'):
                return 1.0 if game.get_current_player() != current else 0.0
            
            moves = game.get_legal_moves()
            player = game.get_current_player()
            opponent = 'O' if player == 'X' else 'X'
            move = None

            # Try to win
            for m in moves:
                test = game.copy()
                test.state[m] = player
                if test.is_winner(player):
                    move = m
                    break

            # Try to block
            if not move:
                for m in moves:
                    test = game.copy()
                    test.state[m] = opponent
                    if test.is_winner(opponent):
                        move = m
                        break

            # Take strategic position
            if not move:
                for pos in [4] + [0,2,6,8] + [1,3,5,7]:  # Center, corners, edges
                    if pos in moves:
                        move = pos
                        break

            if not move:
                move = random.choice(moves)
            
            game.make_move(move)
            
        return 0.5

    def _select_and_expand(self, node: Node) -> Node:
        while not node.game.is_winner('X') and not node.game.is_winner('O') and not node.game.is_draw():
            if node.untried_moves:
                move = random.choice(node.untried_moves)
                node.untried_moves.remove(move)
                new_game = node.game.copy()
                new_game.make_move(move)
                child = Node(new_game, parent=node)
                node.children.append(child)
                return child
            node = max(node.children, key=lambda c: c.get_ucb_score(1.414))
        return node

    def _backpropagate(self, node: Node, result: float):
        while node:
            node.visits += 1
            node.wins += result
            node = node.parent

    def _get_best_child_move(self, root: Node) -> int:
        best_child = max(root.children, key=lambda c: c.wins / c.visits)
        return next(i for i in range(9) if root.game.state[i] != best_child.game.state[i])
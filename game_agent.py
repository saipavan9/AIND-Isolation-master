"""Finish all TODO items in this file to complete the isolation project, then
test your agent's strength against a set of known agents using tournament.py
and include the results in your report.
"""
import random


class SearchTimeout(Exception):
    """Subclass base exception for code clarity. """
    pass


def custom_score(game, player):
    """Calculate the heuristic value of a game state from the point of view
    of the given player.

    This should be the best heuristic function for your project submission.

    Note: this function should be called from within a Player instance as
    `self.score()` -- you should not need to call this function directly.

    Parameters
    ----------
    game : `isolation.Board`
        An instance of `isolation.Board` encoding the current state of the
        game (e.g., player locations and blocked cells).

    player : object
        A player instance in the current game (i.e., an object corresponding to
        one of the player objects `game.__player_1__` or `game.__player_2__`.)

    Returns
    -------
    float
        The heuristic value of the current game state to the specified player.
    """
    return heuristic1(game,player)


def heuristic1(game, player):
    """Calculate the heuristic value of a game state from the point of view
    of the given player.

    Note: this function should be called from within a Player instance as
    `self.score()` -- you should not need to call this function directly.

    Parameters
    ----------
    game : `isolation.Board`
        An instance of `isolation.Board` encoding the current state of the
        game (e.g., player locations and blocked cells).

    player : object
        A player instance in the current game (i.e., an object corresponding to
        one of the player objects `game.__player_1__` or `game.__player_2__`.)

    Returns
    -------
    float
        The heuristic value of the current game state to the specified player.
    """
    # Have we won the game?
    if game.is_winner(player):
        return float("inf")

    # Do we even have moves to play?
    if game.is_loser(player):
        return float("-inf")

    # We have moves to play. How many more than our opponent?
    player_moves_left = len(game.get_legal_moves(player))
    opponent_moves_left = len(game.get_legal_moves(game.get_opponent(player)))
    return float(player_moves_left - opponent_moves_left)


def get_longest_jumping_run(game, player_y_pos, player_x_pos, moves):
    """This function computes the longest run of jumping moves that can be performed.

    Parameters
    ----------
    game : `isolation.Board`

    player_y_pos, player_x_pos : int, int
        The player's position to evaluate based on its longest jumping run.

    moves : `list` of legal moves for 'player'
        List` of legal moves for 'player'

    Returns
    -------
    int
        The longest run found.
    """

#It is the my opinion that FUNCTION INLINING and LOOP UNROLLING are CRITICAL to the success of my heuristic.
# It is BECAUSE we don't use functions and for loops that our code can explore more branches before timeout.
    longest_player_run = 1
    for move_y, move_x in moves:
        if longest_player_run == 7:
            break
        player_run = 1
        if move_y == player_y_pos + 1 and move_x == player_x_pos + 2:  # Pos 1
            # Start the run going East-South
            # +---+---+---+
            # | 5 | 2 | 7 |
            # +---+---+---+
            # | p | x | 4 |
            # +---+---+---+
            # | 3 | 6 | 1 |
            # +---+---+---+
            if not game.move_is_legal((player_y_pos - 1, player_x_pos + 1)):  # Pos 2
                longest_player_run = max(longest_player_run, player_run)
                continue
            else:
                player_run += 1
            if not game.move_is_legal((player_y_pos + 1, player_x_pos)):  # Pos 3
                longest_player_run = max(longest_player_run, player_run)
                continue
            else:
                player_run += 1
            if not game.move_is_legal((player_y_pos, player_x_pos + 2)):  # Pos 4
                longest_player_run = max(longest_player_run, player_run)
                continue
            else:
                player_run += 1
            if not game.move_is_legal((player_y_pos - 1, player_x_pos)):  # Pos 5
                longest_player_run = max(longest_player_run, player_run)
                continue
            else:
                player_run += 1
            if not game.move_is_legal((player_y_pos + 1, player_x_pos + 1)):  # Pos 6
                longest_player_run = max(longest_player_run, player_run)
                continue
            else:
                player_run += 1
            if not game.move_is_legal((player_y_pos - 1, player_x_pos + 2)):  # Pos 7
                longest_player_run = max(longest_player_run, player_run)
                continue
            else:
                longest_player_run = 7  # max(longest_player_run, player_run + 1)
                break

        if move_y == player_y_pos - 1 and move_x == player_x_pos + 2:  # Pos 1
            # Start the run going East-North
            # +---+---+---+
            # | 3 | 6 | 1 |
            # +---+---+---+
            # | p | x | 4 |
            # +---+---+---+
            # | 5 | 2 | 7 |
            # +---+---+---+
            if not game.move_is_legal((player_y_pos + 1, player_x_pos + 1)):  # Pos 2
                longest_player_run = max(longest_player_run, player_run)
                continue
            else:
                player_run += 1
            if not game.move_is_legal((player_y_pos - 1, player_x_pos)):  # Pos 3
                longest_player_run = max(longest_player_run, player_run)
                continue
            else:
                player_run += 1
            if not game.move_is_legal((player_y_pos, player_x_pos + 2)):  # Pos 4
                longest_player_run = max(longest_player_run, player_run)
                continue
            else:
                player_run += 1
            if not game.move_is_legal((player_y_pos + 1, player_x_pos)):  # Pos 5
                longest_player_run = max(longest_player_run, player_run)
                continue
            else:
                player_run += 1
            if not game.move_is_legal((player_y_pos - 1, player_x_pos + 1)):  # Pos 6
                longest_player_run = max(longest_player_run, player_run)
                continue
            else:
                player_run += 1
            if not game.move_is_legal((player_y_pos + 1, player_x_pos + 2)):  # Pos 7
                longest_player_run = max(longest_player_run, player_run)
                continue
            else:
                longest_player_run = 7  # max(longest_player_run, player_run + 1)
                break

        if move_y == player_y_pos - 2 and move_x == player_x_pos + 1:  # Pos 1
            # Start the run going North-East
            # +---+---+---+
            # | 6 | 1 | 4 |
            # +---+---+---+
            # | 3 | x | 7 |
            # +---+---+---+
            # | p | 5 | 2 |
            # +---+---+---+
            if not game.move_is_legal((player_y_pos, player_x_pos + 2)):  # Pos 2
                longest_player_run = max(longest_player_run, player_run)
                continue
            else:
                player_run += 1
            if not game.move_is_legal((player_y_pos - 1, player_x_pos)):  # Pos 3
                longest_player_run = max(longest_player_run, player_run)
                continue
            else:
                player_run += 1
            if not game.move_is_legal((player_y_pos - 2, player_x_pos + 2)):  # Pos 4
                longest_player_run = max(longest_player_run, player_run)
                continue
            else:
                player_run += 1
            if not game.move_is_legal((player_y_pos, player_x_pos + 1)):  # Pos 5
                longest_player_run = max(longest_player_run, player_run)
                continue
            else:
                player_run += 1
            if not game.move_is_legal((player_y_pos - 2, player_x_pos)):  # Pos 6
                longest_player_run = max(longest_player_run, player_run)
                continue
            else:
                player_run += 1
            if not game.move_is_legal((player_y_pos - 1, player_x_pos + 2)):  # Pos 7
                longest_player_run = max(longest_player_run, player_run)
                continue
            else:
                longest_player_run = 7  # max(longest_player_run, player_run + 1)
                break

        if move_y == player_y_pos - 2 and move_x == player_x_pos - 1:  # Pos 1
            # Start the run going North-West
            # +---+---+---+
            # | 1 | 4 | 7 |
            # +---+---+---+
            # | 6 | x | 2 |
            # +---+---+---+
            # | 3 | p | 5 |
            # +---+---+---+
            if not game.move_is_legal((player_y_pos - 1, player_x_pos + 1)):  # Pos 2
                longest_player_run = max(longest_player_run, player_run)
                continue
            else:
                player_run += 1
            if not game.move_is_legal((player_y_pos, player_x_pos - 1)):  # Pos 3
                longest_player_run = max(longest_player_run, player_run)
                continue
            else:
                player_run += 1
            if not game.move_is_legal((player_y_pos - 2, player_x_pos)):  # Pos 4
                longest_player_run = max(longest_player_run, player_run)
                continue
            else:
                player_run += 1
            if not game.move_is_legal((player_y_pos, player_x_pos + 1)):  # Pos 5
                longest_player_run = max(longest_player_run, player_run)
                continue
            else:
                player_run += 1
            if not game.move_is_legal((player_y_pos - 1, player_x_pos - 1)):  # Pos 6
                longest_player_run = max(longest_player_run, player_run)
                continue
            else:
                player_run += 1
            if not game.move_is_legal((player_y_pos - 2, player_x_pos + 1)):  # Pos 7
                longest_player_run = max(longest_player_run, player_run)
                continue
            else:
                longest_player_run = 7  # max(longest_player_run, player_run + 1)
                break

        if move_y == player_y_pos - 1 and move_x == player_x_pos - 2:  # Pos 1
            # Start the run going West-North
            # +---+---+---+
            # | 1 | 6 | 3 |
            # +---+---+---+
            # | 4 | x | p |
            # +---+---+---+
            # | 7 | 2 | 5 |
            # +---+---+---+
            if not game.move_is_legal((player_y_pos + 1, player_x_pos - 1)):  # Pos 2
                longest_player_run = max(longest_player_run, player_run)
                continue
            else:
                player_run += 1
            if not game.move_is_legal((player_y_pos - 1, player_x_pos)):  # Pos 3
                longest_player_run = max(longest_player_run, player_run)
                continue
            else:
                player_run += 1
            if not game.move_is_legal((player_y_pos, player_x_pos - 2)):  # Pos 4
                longest_player_run = max(longest_player_run, player_run)
                continue
            else:
                player_run += 1
            if not game.move_is_legal((player_y_pos + 1, player_x_pos)):  # Pos 5
                longest_player_run = max(longest_player_run, player_run)
                continue
            else:
                player_run += 1
            if not game.move_is_legal((player_y_pos - 1, player_x_pos - 1)):  # Pos 6
                longest_player_run = max(longest_player_run, player_run)
                continue
            else:
                player_run += 1
            if not game.move_is_legal((player_y_pos + 1, player_x_pos - 2)):  # Pos 7
                longest_player_run = max(longest_player_run, player_run)
                continue
            else:
                longest_player_run = 7  # max(longest_player_run, player_run + 1)
                break

        if move_y == player_y_pos + 1 and move_x == player_x_pos - 2:  # Pos 1
            # Start the run going West-South
            # +---+---+---+
            # | 7 | 2 | 5 |
            # +---+---+---+
            # | 4 | x | p |
            # +---+---+---+
            # | 1 | 6 | 3 |
            # +---+---+---+
            if not game.move_is_legal((player_y_pos - 1, player_x_pos - 1)):  # Pos 2
                longest_player_run = max(longest_player_run, player_run)
                continue
            else:
                player_run += 1
            if not game.move_is_legal((player_y_pos + 1, player_x_pos)):  # Pos 3
                longest_player_run = max(longest_player_run, player_run)
                continue
            else:
                player_run += 1
            if not game.move_is_legal((player_y_pos, player_x_pos - 2)):  # Pos 4
                longest_player_run = max(longest_player_run, player_run)
                continue
            else:
                player_run += 1
            if not game.move_is_legal((player_y_pos - 1, player_x_pos)):  # Pos 5
                longest_player_run = max(longest_player_run, player_run)
                continue
            else:
                player_run += 1
            if not game.move_is_legal((player_y_pos + 1, player_x_pos - 1)):  # Pos 6
                longest_player_run = max(longest_player_run, player_run)
                continue
            else:
                player_run += 1
            if not game.move_is_legal((player_y_pos - 1, player_x_pos - 2)):  # Pos 7
                longest_player_run = max(longest_player_run, player_run)
                continue
            else:
                longest_player_run = 7  # max(longest_player_run, player_run + 1)
                break

        if move_y == player_y_pos + 2 and move_x == player_x_pos - 1:  # Pos 1
            # Start the run going South-West
            # +---+---+---+
            # | 3 | p | 5 |
            # +---+---+---+
            # | 6 | x | 2 |
            # +---+---+---+
            # | 1 | 4 | 7 |
            # +---+---+---+
            if not game.move_is_legal((player_y_pos + 1, player_x_pos + 1)):  # Pos 2
                longest_player_run = max(longest_player_run, player_run)
                continue
            else:
                player_run += 1
            if not game.move_is_legal((player_y_pos, player_x_pos - 1)):  # Pos 3
                longest_player_run = max(longest_player_run, player_run)
                continue
            else:
                player_run += 1
            if not game.move_is_legal((player_y_pos + 2, player_x_pos)):  # Pos 4
                longest_player_run = max(longest_player_run, player_run)
                continue
            else:
                player_run += 1
            if not game.move_is_legal((player_y_pos, player_x_pos + 1)):  # Pos 5
                longest_player_run = max(longest_player_run, player_run)
                continue
            else:
                player_run += 1
            if not game.move_is_legal((player_y_pos + 1, player_x_pos - 1)):  # Pos 6
                longest_player_run = max(longest_player_run, player_run)
                continue
            else:
                player_run += 1
            if not game.move_is_legal((player_y_pos + 2, player_x_pos + 1)):  # Pos 7
                longest_player_run = max(longest_player_run, player_run)
                continue
            else:
                longest_player_run = 7  # max(longest_player_run, player_run + 1)
                break

        if move_y == player_y_pos + 2 and move_x == player_x_pos + 1:  # Pos 1
            # Start the run going South-East
            # +---+---+---+
            # | 5 | p | 3 |
            # +---+---+---+
            # | 2 | x | 6 |
            # +---+---+---+
            # | 7 | 4 | 1 |
            # +---+---+---+
            if not game.move_is_legal((player_y_pos + 1, player_x_pos - 1)):  # Pos 2
                longest_player_run = max(longest_player_run, player_run)
                continue
            else:
                player_run += 1
            if not game.move_is_legal((player_y_pos, player_x_pos + 1)):  # Pos 3
                longest_player_run = max(longest_player_run, player_run)
                continue
            else:
                player_run += 1
            if not game.move_is_legal((player_y_pos + 2, player_x_pos)):  # Pos 4
                longest_player_run = max(longest_player_run, player_run)
                continue
            else:
                player_run += 1
            if not game.move_is_legal((player_y_pos, player_x_pos - 1)):  # Pos 5
                longest_player_run = max(longest_player_run, player_run)
                continue
            else:
                player_run += 1
            if not game.move_is_legal((player_y_pos + 1, player_x_pos + 1)):  # Pos 6
                longest_player_run = max(longest_player_run, player_run)
                continue
            else:
                player_run += 1
            if not game.move_is_legal((player_y_pos + 2, player_x_pos - 1)):  # Pos 7
                longest_player_run = max(longest_player_run, player_run)
                continue
            else:
                longest_player_run = 7  # max(longest_player_run, player_run + 1)
                break

    return longest_player_run

def get_sum_jumping_runs(game, player_y_pos, player_x_pos, moves):

    """This function measures the longest run of jumping moves that can be performed .
    It can be defined by a starting position and each of its legal moves left. 

    Parameters
    ----------
    game : `isolation.Board`

    player_y_pos, player_x_pos : int, int
        The player's position to evaluate based on its longest jumping run.

    moves : `list` of legal moves for 'player'
        List` of legal moves for 'player'

    Returns
    -------
    int
        The longest run found.
    """

    sum_jumping_runs = 0
    for move_y, move_x in moves:
        if move_y == player_y_pos + 1 and move_x == player_x_pos + 2:  # Pos 1
            # Start the run going East-South
            # +---+---+---+
            # | 5 | 2 | 7 |
            # +---+---+---+
            # | p | x | 4 |
            # +---+---+---+
            # | 3 | 6 | 1 |
            # +---+---+---+
            if not game.move_is_legal((player_y_pos - 1, player_x_pos + 1)):  # Pos 2
                continue
            else:
                sum_jumping_runs += 1
            if not game.move_is_legal((player_y_pos + 1, player_x_pos)):  # Pos 3
                continue
            else:
                sum_jumping_runs += 1
            if not game.move_is_legal((player_y_pos, player_x_pos + 2)):  # Pos 4
                continue
            else:
                sum_jumping_runs += 1
            if not game.move_is_legal((player_y_pos - 1, player_x_pos)):  # Pos 5
                continue
            else:
                sum_jumping_runs += 1
            if not game.move_is_legal((player_y_pos + 1, player_x_pos + 1)):  # Pos 6
                continue
            else:
                sum_jumping_runs += 1
            if not game.move_is_legal((player_y_pos - 1, player_x_pos + 2)):  # Pos 7
                continue
            else:
                sum_jumping_runs += 1
                continue

        if move_y == player_y_pos - 1 and move_x == player_x_pos + 2:  # Pos 1
            # Start the run going East-North
            # +---+---+---+
            # | 3 | 6 | 1 |
            # +---+---+---+
            # | p | x | 4 |
            # +---+---+---+
            # | 5 | 2 | 7 |
            # +---+---+---+
            if not game.move_is_legal((player_y_pos + 1, player_x_pos + 1)):  # Pos 2
                continue
            else:
                sum_jumping_runs += 1
            if not game.move_is_legal((player_y_pos - 1, player_x_pos)):  # Pos 3
                continue
            else:
                sum_jumping_runs += 1
            if not game.move_is_legal((player_y_pos, player_x_pos + 2)):  # Pos 4
                continue
            else:
                sum_jumping_runs += 1
            if not game.move_is_legal((player_y_pos + 1, player_x_pos)):  # Pos 5
                continue
            else:
                sum_jumping_runs += 1
            if not game.move_is_legal((player_y_pos - 1, player_x_pos + 1)):  # Pos 6
                continue
            else:
                sum_jumping_runs += 1
            if not game.move_is_legal((player_y_pos + 1, player_x_pos + 2)):  # Pos 7
                continue
            else:
                sum_jumping_runs += 1
                continue

        if move_y == player_y_pos - 2 and move_x == player_x_pos + 1:  # Pos 1
            # Start the run going North-East
            # +---+---+---+
            # | 6 | 1 | 4 |
            # +---+---+---+
            # | 3 | x | 7 |
            # +---+---+---+
            # | p | 5 | 2 |
            # +---+---+---+
            if not game.move_is_legal((player_y_pos, player_x_pos + 2)):  # Pos 2
                continue
            else:
                sum_jumping_runs += 1
            if not game.move_is_legal((player_y_pos - 1, player_x_pos)):  # Pos 3
                continue
            else:
                sum_jumping_runs += 1
            if not game.move_is_legal((player_y_pos - 2, player_x_pos + 2)):  # Pos 4
                continue
            else:
                sum_jumping_runs += 1
            if not game.move_is_legal((player_y_pos, player_x_pos + 1)):  # Pos 5
                continue
            else:
                sum_jumping_runs += 1
            if not game.move_is_legal((player_y_pos - 2, player_x_pos)):  # Pos 6
                continue
            else:
                sum_jumping_runs += 1
            if not game.move_is_legal((player_y_pos - 1, player_x_pos + 2)):  # Pos 7
                continue
            else:
                sum_jumping_runs += 1
                continue

        if move_y == player_y_pos - 2 and move_x == player_x_pos - 1:  # Pos 1
            # Start the run going North-West
            # +---+---+---+
            # | 1 | 4 | 7 |
            # +---+---+---+
            # | 6 | x | 2 |
            # +---+---+---+
            # | 3 | p | 5 |
            # +---+---+---+
            if not game.move_is_legal((player_y_pos - 1, player_x_pos + 1)):  # Pos 2
                continue
            else:
                sum_jumping_runs += 1
            if not game.move_is_legal((player_y_pos, player_x_pos - 1)):  # Pos 3
                continue
            else:
                sum_jumping_runs += 1
            if not game.move_is_legal((player_y_pos - 2, player_x_pos)):  # Pos 4
                continue
            else:
                sum_jumping_runs += 1
            if not game.move_is_legal((player_y_pos, player_x_pos + 1)):  # Pos 5
                continue
            else:
                sum_jumping_runs += 1
            if not game.move_is_legal((player_y_pos - 1, player_x_pos - 1)):  # Pos 6
                continue
            else:
                sum_jumping_runs += 1
            if not game.move_is_legal((player_y_pos - 2, player_x_pos + 1)):  # Pos 7
                continue
            else:
                sum_jumping_runs += 1
                continue

        if move_y == player_y_pos - 1 and move_x == player_x_pos - 2:  # Pos 1
            # Start the run going West-North
            # +---+---+---+
            # | 1 | 6 | 3 |
            # +---+---+---+
            # | 4 | x | p |
            # +---+---+---+
            # | 7 | 2 | 5 |
            # +---+---+---+
            if not game.move_is_legal((player_y_pos + 1, player_x_pos - 1)):  # Pos 2
                continue
            else:
                sum_jumping_runs += 1
            if not game.move_is_legal((player_y_pos - 1, player_x_pos)):  # Pos 3
                continue
            else:
                sum_jumping_runs += 1
            if not game.move_is_legal((player_y_pos, player_x_pos - 2)):  # Pos 4
                continue
            else:
                sum_jumping_runs += 1
            if not game.move_is_legal((player_y_pos + 1, player_x_pos)):  # Pos 5
                continue
            else:
                sum_jumping_runs += 1
            if not game.move_is_legal((player_y_pos - 1, player_x_pos - 1)):  # Pos 6
                continue
            else:
                sum_jumping_runs += 1
            if not game.move_is_legal((player_y_pos + 1, player_x_pos - 2)):  # Pos 7
                continue
            else:
                sum_jumping_runs += 1
                continue

        if move_y == player_y_pos + 1 and move_x == player_x_pos - 2:  # Pos 1
            # Start the run going West-South
            # +---+---+---+
            # | 7 | 2 | 5 |
            # +---+---+---+
            # | 4 | x | p |
            # +---+---+---+
            # | 1 | 6 | 3 |
            # +---+---+---+
            if not game.move_is_legal((player_y_pos - 1, player_x_pos - 1)):  # Pos 2
                continue
            else:
                sum_jumping_runs += 1
            if not game.move_is_legal((player_y_pos + 1, player_x_pos)):  # Pos 3
                continue
            else:
                sum_jumping_runs += 1
            if not game.move_is_legal((player_y_pos, player_x_pos - 2)):  # Pos 4
                continue
            else:
                sum_jumping_runs += 1
            if not game.move_is_legal((player_y_pos - 1, player_x_pos)):  # Pos 5
                continue
            else:
                sum_jumping_runs += 1
            if not game.move_is_legal((player_y_pos + 1, player_x_pos - 1)):  # Pos 6
                continue
            else:
                sum_jumping_runs += 1
            if not game.move_is_legal((player_y_pos - 1, player_x_pos - 2)):  # Pos 7
                continue
            else:
                sum_jumping_runs += 1
                continue

        if move_y == player_y_pos + 2 and move_x == player_x_pos - 1:  # Pos 1
            # Start the run going South-West
            # +---+---+---+
            # | 3 | p | 5 |
            # +---+---+---+
            # | 6 | x | 2 |
            # +---+---+---+
            # | 1 | 4 | 7 |
            # +---+---+---+
            if not game.move_is_legal((player_y_pos + 1, player_x_pos + 1)):  # Pos 2
                continue
            else:
                sum_jumping_runs += 1
            if not game.move_is_legal((player_y_pos, player_x_pos - 1)):  # Pos 3
                continue
            else:
                sum_jumping_runs += 1
            if not game.move_is_legal((player_y_pos + 2, player_x_pos)):  # Pos 4
                continue
            else:
                sum_jumping_runs += 1
            if not game.move_is_legal((player_y_pos, player_x_pos + 1)):  # Pos 5
                continue
            else:
                sum_jumping_runs += 1
            if not game.move_is_legal((player_y_pos + 1, player_x_pos - 1)):  # Pos 6
                continue
            else:
                sum_jumping_runs += 1
            if not game.move_is_legal((player_y_pos + 2, player_x_pos + 1)):  # Pos 7
                continue
            else:
                sum_jumping_runs += 1
                continue

        if move_y == player_y_pos + 2 and move_x == player_x_pos + 1:  # Pos 1
            # Start the run going South-East
            # +---+---+---+
            # | 5 | p | 3 |
            # +---+---+---+
            # | 2 | x | 6 |
            # +---+---+---+
            # | 7 | 4 | 1 |
            # +---+---+---+
            if not game.move_is_legal((player_y_pos + 1, player_x_pos - 1)):  # Pos 2
                continue
            else:
                sum_jumping_runs += 1
            if not game.move_is_legal((player_y_pos, player_x_pos + 1)):  # Pos 3
                continue
            else:
                sum_jumping_runs += 1
            if not game.move_is_legal((player_y_pos + 2, player_x_pos)):  # Pos 4
                continue
            else:
                sum_jumping_runs += 1
            if not game.move_is_legal((player_y_pos, player_x_pos - 1)):  # Pos 5
                continue
            else:
                sum_jumping_runs += 1
            if not game.move_is_legal((player_y_pos + 1, player_x_pos + 1)):  # Pos 6
                continue
            else:
                sum_jumping_runs += 1
            if not game.move_is_legal((player_y_pos + 2, player_x_pos - 1)):  # Pos 7
                continue
            else:
                sum_jumping_runs += 1
                continue

    return sum_jumping_runs



class IsolationPlayer:
    """Base class for minimax and alphabeta agents -- this class is never
    constructed or tested directly.

    ********************  DO NOT MODIFY THIS CLASS  ********************

    Parameters
    ----------
    search_depth : int (optional)
        A strictly positive integer (i.e., 1, 2, 3,...) for the number of
        layers in the game tree to explore for fixed-depth search. (i.e., a
        depth of one (1) would only explore the immediate sucessors of the
        current state.)

    score_fn : callable (optional)
        A function to use for heuristic evaluation of game states.

    timeout : float (optional)
        Time remaining (in milliseconds) when search is aborted. Should be a
        positive value large enough to allow the function to return before the
        timer expires.
    """
    def __init__(self, search_depth=3, score_fn=custom_score,iterative = true, method='minimax' timeout=10.):
        self.search_depth = search_depth
        self.iterative = iterative
        self.score = score_fn
        self.method = method
        self.time_left = None
        self.TIMER_THRESHOLD = timeout


class MinimaxPlayer(IsolationPlayer):
    """Game-playing agent that chooses a move using depth-limited minimax
    search. You must finish and test this player to make sure it properly uses
    minimax to return a good move before the search time limit expires.
    """

    def get_move(self, game, time_left):
        """Search for the best move from the available legal moves and return a
        result before the time limit expires.

        **************  YOU DO NOT NEED TO MODIFY THIS FUNCTION  *************

        For fixed-depth search, this function simply wraps the call to the
        minimax method, but this method provides a common interface for all
        Isolation agents, and you will replace it in the AlphaBetaPlayer with
        iterative deepening search.

        Parameters
        ----------
        game : `isolation.Board`
            An instance of `isolation.Board` encoding the current state of the
            game (e.g., player locations and blocked cells).

        time_left : callable
            A function that returns the number of milliseconds left in the
            current turn. Returning with any less than 0 ms remaining forfeits
            the game.

        Returns
        -------
        (int, int)
            Board coordinates corresponding to a legal move; may return
            (-1, -1) if there are no available legal moves.
        """
        self.time_left = time_left

        #check for any legal moves

        if not legal_moves:
            return (-1, -1)

        # If we started the game.Take the center move.
        if game.move_count == 0:
            return(int(game.height/2), int(game.width/2))

        # Let's search for a good move!
        best_move_so_far = (-1, -1)

        try:
            """
            The try and catch block will help us to evaluate the status of the both
            the methods minimax and alphabeta when the time is getting near.
            """
            if self.iterative == True:
                iterative_search_depth = 1
                if self.method == 'minimax':
                    while True:
                        best_score_so_far, best_move_so_far = self.minimax(game, iterative_search_depth)
                        if best_score_so_far == float("inf") or best_score_so_far == float("-inf"):
                            break
                        iterative_search_depth += 1
                elif self.method == 'alphabeta':
                    while True:
                        best_score_so_far, best_move_so_far = self.alphabeta(game, iterative_search_depth)
                        if best_score_so_far == float("inf") or best_score_so_far == float("-inf"):
                            break
                        iterative_search_depth += 1
                else:
                    raise ValueError('Invalid Parameters')
            else:
                if self.method == 'minimax':
                    _, best_move_so_far = self.minimax(game, self.search_depth)
                elif self.method == 'alphabeta':
                    _, best_move_so_far = self.alphabeta(game, self.search_depth)
                else:
                    raise ValueError('Invalid Parameters')

        except Timeout:
            # Handle any actions required at timeout, if necessary
            pass

        # Return the best move from the last completed search iteration
        return best_move_so_far


    def minimax(self, game, depth):
        """Implement depth-limited minimax search algorithm as described in
        the lectures.

        This should be a modified version of MINIMAX-DECISION in the AIMA text.
        https://github.com/aimacode/aima-pseudocode/blob/master/md/Minimax-Decision.md

        **********************************************************************
            You MAY add additional methods to this class, or define helper
                 functions to implement the required functionality.
        **********************************************************************

        Parameters
        ----------
        game : isolation.Board
            An instance of the Isolation game `Board` class representing the
            current game state

        depth : int
            Depth is an integer representing the maximum number of plies to
            search in the game tree before aborting

        Returns
        -------
        (int, int)
            The board coordinates of the best move found in the current search;
            (-1, -1) if there are no legal moves

        Notes
        -----
            (1) You MUST use the `self.score()` method for board evaluation
                to pass the project tests; you cannot call any other evaluation
                function directly.

            (2) If you use any helper functions (e.g., as shown in the AIMA
                pseudocode) then you must copy the timer check into the top of
                each helper function or else your agent will timeout during
                testing.
        """
        if self.time_left() < self.TIMER_THRESHOLD:
            raise SearchTimeout()

        # Check for the legal moves
        legal_moves = game.get_legal_moves()
        if not legal_moves:
            if maximizing_player == True:
                return float("-inf"), (-1, -1)
            else:
                return float("inf"), (-1, -1)

        #If legal moves left and reached the target search depth ,return the best possible move at this level.
        lowest_score_so_far, highest_score_so_far = float("inf"), float("-inf")
        best_move_so_far = (-1, -1)
        if depth == 1:
            if maximizing_player == True:
                for move in legal_moves:
                    score = self.score(game.forecast_move(move), self)
                    # If this is a winning move, no need to search further. Otherwise, remember the best move.
                    if score == float("inf"):
                        return score, move
                    if score > highest_score_so_far:
                        highest_score_so_far, best_move_so_far = score, move
                return highest_score_so_far, best_move_so_far
            else:
                for move in legal_moves:
                    score = self.score(game.forecast_move(move), self)
                    # If this is a winning move, no need to search further. Otherwise, remember the best move.
                    if score == float("-inf"):
                        return score, move
                    if score < lowest_score_so_far:
                        lowest_score_so_far, best_move_so_far = score, move
                return lowest_score_so_far, best_move_so_far

        # If legal moves left and didn't reached the target search depth , go down the search branches and return the best possible move at this level.
        if maximizing_player == True:
            for move in legal_moves:
                score, _ = self.minimax(game.forecast_move(move), depth-1, maximizing_player = False)
                # If brach gives us a win, no need to search further else remember the best move.
                if score == float("inf"):
                    return score, move
                if score > highest_score_so_far:
                    highest_score_so_far, best_move_so_far = score, move
            return highest_score_so_far, best_move_so_far
        else:
            for move in legal_moves:
                score, _ = self.minimax(game.forecast_move(move), depth-1, maximizing_player=True)
                # If this branch yields a sure win, no need to search further. Otherwise, remember the best move.
                if score == float("-inf"):
                    return score, move
                if score < lowest_score_so_far:
                    lowest_score_so_far, best_move_so_far = score, move
            return lowest_score_so_far, best_move_so_far

    def alphabeta(self, game, depth, alpha=float("-inf"), beta=float("inf")):
        """Implement depth-limited minimax search with alpha-beta pruning as
        described in the lectures.

        This should be a modified version of ALPHA-BETA-SEARCH in the AIMA text
        https://github.com/aimacode/aima-pseudocode/blob/master/md/Alpha-Beta-Search.md

        **********************************************************************
            You MAY add additional methods to this class, or define helper
                 functions to implement the required functionality.
        **********************************************************************

        Parameters
        ----------
        game : isolation.Board
            An instance of the Isolation game `Board` class representing the
            current game state

        depth : int
            Depth is an integer representing the maximum number of plies to
            search in the game tree before aborting

        alpha : float
            Alpha limits the lower bound of search on minimizing layers

        beta : float
            Beta limits the upper bound of search on maximizing layers

        Returns
        -------
        (int, int)
            The board coordinates of the best move found in the current search;
            (-1, -1) if there are no legal moves

        Notes
        -----
            (1) You MUST use the `self.score()` method for board evaluation
                to pass the project tests; you cannot call any other evaluation
                function directly.

            (2) If you use any helper functions (e.g., as shown in the AIMA
                pseudocode) then you must copy the timer check into the top of
                each helper function or else your agent will timeout during
                testing.
        """
        # Checking for possible legal moves.
        legal_moves = game.get_legal_moves()
        if not legal_moves:
            if maximizing_player == True:
                return float("-inf"), (-1, -1)
            else:
                return float("inf"), (-1, -1)


    """
    If there are legal moves and also if we had reache the search depth target.
    
    The maximizing player returns the move with the highest score, but this move will never be propagated by minimizing player.
    The minimizing player will be able to attack the other and the same thing happens withe minimizing player too.
    This means the maximizing player can stop evaluating moves as soon as it finds a move with a score >= beta and
    the minimizing player can stop evaluating moves as soon as if finds a move with a score <= alpha.
    
    """
        lowest_score_so_far, highest_score_so_far = float("inf"), float("-inf")
        best_move_so_far = (-1, -1)
        if depth == 1:
            if maximizing_player == True:
                for move in legal_moves:
                    score = self.score(game.forecast_move(move), self)
                    # If this is a score better than beta, no need to search further. Otherwise, remember the best move.
                    if score >= beta:
                        return score, move
                    if score > highest_score_so_far:
                        highest_score_so_far, best_move_so_far = score, move
                return highest_score_so_far, best_move_so_far
            else:
                for move in legal_moves:
                    score = self.score(game.forecast_move(move), self)
                    # If this is a score worse than alpha, no need to search further. Otherwise, remember the best move.
                    if score <= alpha:
                        return score, move
                    if score < lowest_score_so_far:
                        lowest_score_so_far, best_move_so_far = score, move
                return lowest_score_so_far, best_move_so_far

        """
        If there are legal moves and we don't reach the search depth

         The maximizing player returns the move with the highest score, but this move will never be propagated by minimizing player.
         The minimizing player will be able to attack the other and the same thing happens withe minimizing player too.
         This means the maximizing player can stop evaluating moves as soon as it finds a move with a score >= beta and
         the minimizing player can stop evaluating moves as soon as if finds a move with a score <= alpha.
           
        """
        if maximizing_player == True:
            for move in legal_moves:
                # Evaluate this move in depth
                score, _ = self.alphabeta(game.forecast_move(move), depth-1, alpha, beta, maximizing_player = False)
                # If this branch yields a score better than beta, no need to search further.
                if score >= beta:
                    return score, move
                # Otherwise, remember the best move and update alpha.
                if score > highest_score_so_far:
                    highest_score_so_far, best_move_so_far = score, move
                alpha = max(alpha, highest_score_so_far)
            return highest_score_so_far, best_move_so_far
        else:
            for move in legal_moves:
                # Evaluate this move in depth.
                score, _ = self.alphabeta(game.forecast_move(move), depth-1, alpha, beta, maximizing_player=True)
                # If this branch yields a score worse than alpha, no need to search further.
                if score <= alpha:
                    return score, move
                # Otherwise, remember the best move and update beta.
                if score < lowest_score_so_far:
                    lowest_score_so_far, best_move_so_far = score, move
                beta = min(beta, lowest_score_so_far)
            return lowest_score_so_far, best_move_so_far

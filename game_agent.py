"""This file contains all the classes you must complete for this project.

You can use the test cases in agent_test.py to help during development, and
augment the test suite with your own test cases to further test your code.

You must test your agent's strength against a set of agents with known
relative strength using tournament.py and include the results in your report.
"""
import random


class SearchTimeout(Exception):
    """Subclass base exception for code clarity."""
    pass


def custom_score(game, player):
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
    return gameStrategy4(game, player)

def custom_score_2(game, player):
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
    return gameStrategy3(game, player)



def custom_score_3(game, player):
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
    return gameStrategy2(game, player)

def gameStrategy1(game, player):
    """
    In this strategy, We consider the availabilty of moves for player evaluates them being in the better position
    in the game. This function simply returns the difference in number of legal moves left between the players.
    If the player and opponent have the same number of moves, then the returned value is zero.
    If the returned value is positive , then player is doing better  than its opponent.

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

def gameStrategy2(game, player):
    """
    We consider the availabilty of moves for player and the starting positions evaluates them being in the better position
    in the game. If a player's position is closer to the center of the board, it is more probable that this player can do 
    better than a player whose remaining moves are near the edge of the board 
    If the players have the same number of moves and are at the same distance from the center, then returned value is 0.
    If the returned value is positive, then is doing better than its opponent.

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

    # moves left?
    if game.is_loser(player):
        return float("-inf")

    player_moves_left = len(game.get_legal_moves(player))
    opponent_moves_left = len(game.get_legal_moves(game.get_opponent(player)))

    if player_moves_left != opponent_moves_left:
        return float(player_moves_left - opponent_moves_left)

    else:
        #if same number of moves, look for a positional advantage.
        # Used the Manhattan distance to the center of the board to assess positional advantage..
        center_y_pos, center_x_pos = int(game.height / 2), int(game.width / 2)
        player_y_pos, player_x_pos = game.get_player_location(player)
        opponent_y_pos, opponent_x_pos = game.get_player_location(game.get_opponent(player))
        player_distance = abs(player_y_pos - center_y_pos) + abs(player_x_pos - center_x_pos)
        opponent_distance = abs(opponent_y_pos - center_y_pos) + abs(opponent_x_pos - center_x_pos)
        # Calculate the difference between the two distances to evaluate positional advantage.
        # If both players are at the same distance from the center -> return 0.
        return float(opponent_distance - player_distance) / 10.

def gameStrategy3(game, player):
    """
     We consider the availabilty of moves for player and the starting positions evaluates them being in the better position
    in the game. If a player's position is closer to the center of the board, it is more probable that this player can do 
    better than a player whose remaining moves are near the edge of the board 
    If there is no clear positional advantage, we calculate the longest distance in 3x3 board which comes out to be 7 in general. 
    If the returned value is positive (negative), then `player` is doing better (worse) than its opponent.

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

    # moves left?
    player_moves = game.get_legal_moves(player)
    opponent_moves = game.get_legal_moves(game.get_opponent(player))
    player_moves_left = len(player_moves)
    opponent_moves_left = len(opponent_moves)

    if player_moves_left != opponent_moves_left:
        return float(player_moves_left - opponent_moves_left)

    else:
        #if same number of moves, look for a positional advantage.
        # Used the Manhattan distance to the center of the board to assess positional advantage.
        center_y_pos, center_x_pos = int(game.height / 2), int(game.width / 2)
        player_y_pos, player_x_pos = game.get_player_location(player)
        opponent_y_pos, opponent_x_pos = game.get_player_location(game.get_opponent(player))
        player_distance = abs(player_y_pos - center_y_pos) + abs(player_x_pos - center_x_pos)
        opponent_distance = abs(opponent_y_pos - center_y_pos) + abs(opponent_x_pos - center_x_pos)
        if player_distance != opponent_distance:
            # Take the difference between the two distances to evaluate positional advantage.
            return float(opponent_distance - player_distance) / 10.

        else:
            # If both players are at the same distance from the center, assess best survival odds.
            # What's the longest run we can achieve between our current position and any of our legal moves left?
            longest_player_run = get_longest_jumping_run(game, player_y_pos, player_x_pos, player_moves)
            longest_opponent_run = get_longest_jumping_run(game, opponent_y_pos, opponent_x_pos, opponent_moves)

            # All we need now is to take the difference between the two numbers to evaluate which player can last the longest in a tight spot.
            # If the two numbers are the same, return 0.
            return float(longest_player_run - longest_opponent_run) / 100.


def gameStrategy4(game, player):
    """
    In this strategy ,specifically we assess our ability to survive the longest.
    We look at ALL the 3x3 squares in which the player's current position belongs and SUM the RUNS of moves that can be
    performed over all these squares. This allows us to evaluate how long we can survive if we're cornered in a tight zone.
    If the returned value is positive (negative), then `player` is doing better (worse) than its opponent.
    
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

    if game.is_loser(player):
        return float("-inf")

    # We have moves to play. How many more than our opponent?
    player_moves = game.get_legal_moves(player)
    opponent_moves = game.get_legal_moves(game.get_opponent(player))

    player_y_pos, player_x_pos = game.get_player_location(player)
    opponent_y_pos, opponent_x_pos = game.get_player_location(game.get_opponent(player))
    longest_player_run = get_sum_jumping_runs(game, player_y_pos, player_x_pos, player_moves)
    longest_opponent_run = get_sum_jumping_runs(game, opponent_y_pos, opponent_x_pos, opponent_moves)

    return float(longest_player_run - longest_opponent_run)

def get_longest_jumping_run(game, player_y_pos, player_x_pos, moves):
    """This function measures the longest run of jumping moves that can be performed inside the 3x3 squares
    defined by a starting position and EACH of its legal moves left. The longest run one can hope to reach is 7.

    Parameters
    ----------
    game : `isolation.Board`
        An instance of `isolation.Board` encoding the current state of the
        game (e.g., player locations and blocked cells).

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
#It is BECAUSE we don't use functions and for loops that our code can explore more branches before timeout.


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
    """
    This is an helper function

    This function measures the longest run of jumping moves that can be performed inside the 3x3 squares
    defined by a starting position and each of its legal moves left. The longest run one can hope to reach is 7.

    Parameters
    ----------
    game : `isolation.Board`
        An instance of `isolation.Board` encoding the current state of the
        game (e.g., player locations and blocked cells).

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
    """Game-playing agent that chooses a move using your evaluation function
    and a depth-limited minimax algorithm with alpha-beta pruning. You must
    finish and test this player to make sure it properly uses minimax and
    alpha-beta to return a good move before the search time limit expires.

    Parameters
    ----------
    search_depth : int (optional)
        A strictly positive integer (i.e., 1, 2, 3,...) for the number of
        layers in the game tree to explore for fixed-depth search. (i.e., a
        depth of one (1) would only explore the immediate sucessors of the
        current state.)

    score_fn : callable (optional)
        A function to use for heuristic evaluation of game states.

    iterative : boolean (optional)
        Flag indicating whether to perform fixed-depth search (False) or
        iterative deepening search (True).

    method : {'minimax', 'alphabeta'} (optional)
        The name of the search method to use in get_move().

    timeout : float (optional)
        Time remaining (in milliseconds) when search is aborted. Should be a
        positive value large enough to allow the function to return before the
        timer expires.
    """

    def __init__(self, search_depth=3, score_fn=custom_score,
                 iterative=True, method='minimax', timeout=30.):
        self.search_depth = search_depth
        self.iterative = iterative
        self.score = score_fn
        self.method = method
        self.time_left = None
        self.TIMER_THRESHOLD = timeout

class MinimaxPlayer(IsolationPlayer):

    def get_move(self, game, time_left):
        """Search for the best move from the available legal moves and return a
        result before the time limit expires.

        This function must perform iterative deepening if self.iterative=True,
        and it must use the search method (minimax or alphabeta) corresponding
        to the self.method value.

        **********************************************************************
        NOTE: If time_left < 0 when this function returns, the agent will
              forfeit the game due to timeout. You must return _before_ the
              timer reaches 0.
        **********************************************************************

        Parameters
        ----------
        game : `isolation.Board`
            An instance of `isolation.Board` encoding the current state of the
            game (e.g., player locations and blocked cells).

        legal_moves : list<(int, int)>
            A list containing legal moves. Moves are encoded as tuples of pairs
            of ints defining the next (row, col) for the agent to occupy.

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

        legal_moves = game.get_legal_moves()

        if not legal_moves:
            return (-1,-1)

        # If we started the game.Take the center move.
        if game.move_count == 0:
            return(int(game.height/2), int(game.width/2))

        #Search for a good move!
        best_move_so_far = legal_moves[0]

        try:
            """
            The try and catch block will help us to evaluate the status of the both
            the methods minimax and alphabeta when the time is getting near.
            """
            if self.iterative == True:
                iterative_search_depth = 1
                while True:
                    best_score_so_far, best_move_so_far = self.minimax(game, iterative_search_depth)
                    if best_score_so_far == float("inf") or best_score_so_far == float("-inf"):
                        break
            else:    
                _, best_move_so_far = self.minimax(game, self.search_depth)

        except SearchTimeout:
            # Handle any actions required at timeout, if necessar
            return best_move_so_far

        return best_move_so_far

    def minimax(self, game, depth):
        """Implement the minimax search algorithm as described in the lectures.

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
        float
            The score for the current search branch

        tuple(int, int)
            The best move for the current branch; (-1, -1) for no legal moves

        Notes
        -----
            (1) You MUST use the `self.score()` method for board evaluation
                to pass the project unit tests; you cannot call any other
                evaluation function directly.
        """
        if self.time_left() < self.TIMER_THRESHOLD:
            raise SearchTimeout()

        def terminal_test(gameState, depth):
            #For timeout 
            if self.time_left() < self.TIMER_THRESHOLD:
                raise SearchTimeout()
            return not bool(gameState.get_legal_moves()) or depth == 0

        def min_value(gameState,depth):
            if self.time_left() < self.TIMER_THRESHOLD:
                raise SearchTimeout()
            if terminal_test(gameState,depth):
                return self.score(gameState,self)
            v = float("inf")
            for m in gameState.get_legal_moves():
                v = min(v,max_value(gameState.forecast_move(m),depth - 1))
            return v

        def max_value(gameState,depth):
            if self.time_left() < self.TIMER_THRESHOLD:
                raise SearchTimeout()
            if terminal_test(gameState,depth):
                return self.score(gameState,self)
            v = float("-inf")
            for m in gameState.get_legal_moves():
                v = max(v,min_value(gameState.forecast_move(m),depth - 1))
            return v

        best_score = float("-inf")
        best_move = game.get_legal_moves()[0]

        for m in game.get_legal_moves():
            v = min_value(game.forecast_move(m),depth - 1)
        #if v is has a better value than current score, then it's updated
            if v > best_score:
                best_score = v
                best_move  = m
        return best_move

class AlphaBetaPlayer(IsolationPlayer):

    def get_move(self, game, time_left):
        """Search for the best move from the available legal moves and return a
        result before the time limit expires.

        Modify the get_move() method from the MinimaxPlayer class to implement
        iterative deepening search instead of fixed-depth search.

        **********************************************************************
        NOTE: If time_left() < 0 when this function returns, the agent will
              forfeit the game due to timeout. You must return _before_ the
              timer reaches 0.
        **********************************************************************

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
        legal_moves = game.get_legal_moves()
        if not legal_moves:
            return (-1, -1)

        #Search for a good move!
        best_move = legal_moves[0]

        try:
            """
            The try and catch block will help us to evaluate the status of the 
            alphabeta when the time is getting near.
            """
            iterative_search_depth = 1
            while True:
                best_move = self.alphabeta(game, iterative_search_depth)
                iterative_search_depth += 1
            
        except SearchTimeout:
            # Handle any actions required at timeout, if necessary
            return best_move

        return best_move

    def alphabeta(self, game, depth, alpha=float("-inf"), beta=float("inf")):
        """Implement minimax search with alpha-beta pruning as described in the
        lectures.

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
        float
            The score for the current search branch

        tuple(int, int)
            The best move for the current branch; (-1, -1) for no legal moves

        Notes
        -----
            (1) You MUST use the `self.score()` method for board evaluation
                to pass the project unit tests; you cannot call any other
                evaluation function directly.
        """
        if self.time_left() < self.TIMER_THRESHOLD:
            raise SearchTimeout()
        #If there are no legal moves
        if not game.get_legal_moves():
            return (-1,-1)
        #helper function for max_value
        def max_value(game,alpha,beta,depth):
            if self.time_left() < self.TIMER_THRESHOLD:
                raise SearchTimeout()
            if not game.get_legal_moves() or depth == 0:
                return self.score(game,self)
            v = float("-inf")
            for m in game.get_legal_moves():
                v = max(v,min_value(game.forecast_move(m),alpha,beta,depth - 1))
                if v >= beta:
                    return v
                alpha = max(alpha,v)
            return v
        #helper function for min_value
        def min_value(game,alpha,beta,depth):
            if self.time_left() < self.TIMER_THRESHOLD:
                raise SearchTimeout()
            if not game.get_legal_moves() or depth == 0:
                return self.score(game,self)
            v = float("inf")
            for m in game.get_legal_moves():
                v = min(v,max_value(game.forecast_move(m),alpha,beta,depth - 1))
                if v <= alpha:
                    return v
                beta = min(beta,v)
            return v

        best_score = float("-inf")
        #This would be passed if there is a timeout or similar thing happens
        best_move = game.get_legal_moves()[0]

        for m in game.get_legal_moves():
            v = min_value(game.forecast_move(m),alpha,beta,depth-1)
            if v > best_score:
                best_score = v
                best_move  = m
        #alpha value is updated if there is a more better value
            alpha = max(alpha,best_score)
        return best_move
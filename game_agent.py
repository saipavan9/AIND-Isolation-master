"""This file contains all the classes you must complete for this project.

You can use the test cases in agent_test.py to help during development, and
augment the test suite with your own test cases to further test your code.

You must test your agent's strength against a set of agents with known
relative strength using tournament.py and include the results in your report.
"""
import random


class Timeout(Exception):
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
    return gameStrategy3(game, player)

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

        
        Playing Matches:
        ----------

        Match 1: ID_Improved vs   Random      Result: 16 to 4
        Match 2: ID_Improved vs   MM_Null     Result: 13 to 7
        Match 3: ID_Improved vs   MM_Open     Result: 13 to 7
        Match 4: ID_Improved vs MM_Improved   Result: 13 to 7
        Match 5: ID_Improved vs   AB_Null     Result: 11 to 9
        Match 6: ID_Improved vs   AB_Open     Result: 10 to 10
        Match 7: ID_Improved vs AB_Improved   Result: 13 to 7

        Results:
        ----------
        ID_Improved         63.57%

        *************************
        Evaluating: Student
        *************************

        Playing Matches:
        ----------
        Match 1:   Student   vs   Random      Result: 18 to 2
        Match 2:   Student   vs   MM_Null     Result: 16 to 4
        Match 3:   Student   vs   MM_Open     Result: 13 to 7
        Match 4:   Student   vs MM_Improved   Result: 12 to 8
        Match 5:   Student   vs   AB_Null     Result: 14 to 6
        Match 6:   Student   vs   AB_Open     Result: 10 to 10
        Match 7:   Student   vs AB_Improved   Result: 15 to 5


        Results:
        ----------
        Student             70.00%

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


Playing Matches:
----------
  Match 1: ID_Improved vs   Random      Result: 18 to 2
  Match 2: ID_Improved vs   MM_Null     Result: 14 to 6
  Match 3: ID_Improved vs   MM_Open     Result: 13 to 7
  Match 4: ID_Improved vs MM_Improved   Result: 12 to 8
  Match 5: ID_Improved vs   AB_Null     Result: 15 to 5
  Match 6: ID_Improved vs   AB_Open     Result: 13 to 7
  Match 7: ID_Improved vs AB_Improved   Result: 11 to 9


Results:
----------
ID_Improved         68.57%

*************************
   Evaluating: Student
*************************

Playing Matches:
----------
  Match 1:   Student   vs   Random      Result: 16 to 4
  Match 2:   Student   vs   MM_Null     Result: 15 to 5
  Match 3:   Student   vs   MM_Open     Result: 17 to 3
  Match 4:   Student   vs MM_Improved   Result: 14 to 6
  Match 5:   Student   vs   AB_Null     Result: 13 to 7
  Match 6:   Student   vs   AB_Open     Result: 13 to 7
  Match 7:   Student   vs AB_Improved   Result: 12 to 8


Results:
----------
Student             71.43%

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
    Playing Matches:
----------
  Match 1: ID_Improved vs   Random      Result: 16 to 4
  Match 2: ID_Improved vs   MM_Null     Result: 17 to 3
  Match 3: ID_Improved vs   MM_Open     Result: 14 to 6
  Match 4: ID_Improved vs MM_Improved   Result: 12 to 8
  Match 5: ID_Improved vs   AB_Null     Result: 15 to 5
  Match 6: ID_Improved vs   AB_Open     Result: 14 to 6
  Match 7: ID_Improved vs AB_Improved   Result: 11 to 9


Results:
----------
ID_Improved         70.71%

*************************
   Evaluating: Student
*************************

Playing Matches:
----------
  Match 1:   Student   vs   Random      Result: 17 to 3
  Match 2:   Student   vs   MM_Null     Result: 15 to 5
  Match 3:   Student   vs   MM_Open     Result: 15 to 5
  Match 4:   Student   vs MM_Improved   Result: 13 to 7
  Match 5:   Student   vs   AB_Null     Result: 14 to 6
  Match 6:   Student   vs   AB_Open     Result: 16 to 4
  Match 7:   Student   vs AB_Improved   Result: 10 to 10


Results:
----------
Student             71.43%


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

    
Playing Matches:
----------
  Match 1: ID_Improved vs   Random      Result: 17 to 3
  Match 2: ID_Improved vs   MM_Null     Result: 16 to 4
  Match 3: ID_Improved vs   MM_Open     Result: 9 to 11
  Match 4: ID_Improved vs MM_Improved   Result: 9 to 11
  Match 5: ID_Improved vs   AB_Null     Result: 12 to 8
  Match 6: ID_Improved vs   AB_Open     Result: 14 to 6
  Match 7: ID_Improved vs AB_Improved   Result: 8 to 12


Results:
----------
ID_Improved         60.71%

*************************
   Evaluating: Student
*************************

Playing Matches:
----------
  Match 1:   Student   vs   Random      Result: 18 to 2
  Match 2:   Student   vs   MM_Null     Result: 20 to 0
  Match 3:   Student   vs   MM_Open     Result: 17 to 3
  Match 4:   Student   vs MM_Improved   Result: 15 to 5
  Match 5:   Student   vs   AB_Null     Result: 17 to 3
  Match 6:   Student   vs   AB_Open     Result: 13 to 7
  Match 7:   Student   vs AB_Improved   Result: 10 to 10


Results:
----------
Student             78.57%

   
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
                 iterative=True, method='minimax', timeout=10.):
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
            return (-1, -1)

        # If we started the game.Take the center move.
        if game.move_count == 0:
            return(int(game.height/2), int(game.width/2))

        #Search for a good move!
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
                else:
                    raise ValueError('ERR in CustomPlayer.get_move() - invalid param')
            else:
                
                _, best_move_so_far = self.minimax(game, self.search_depth)

        except Timeout:
            # Handle any actions required at timeout, if necessary
            pass

        # Return the best move from the last completed search iteration
        return best_move_so_far

    def minimax(self, game, depth, maximizing_player=True):
        """Implement the minimax search algorithm as described in the lectures.

        Parameters
        ----------
        game : isolation.Board
            An instance of the Isolation game `Board` class representing the
            current game state

        depth : int
            Depth is an integer representing the maximum number of plies to
            search in the game tree before aborting

        maximizing_player : bool
            Flag indicating whether the current search depth corresponds to a
            maximizing layer (True) or a minimizing layer (False)

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
            raise Timeout()
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
                    # Evaluate this move.
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
                # Evaluate this move in depth.
                score, _ = self.minimax(game.forecast_move(move), depth-1, maximizing_player = False)
                # If this branch yields a sure win, no need to search further. Otherwise, remember the best move.
                if score == float("inf"):
                    return score, move
                if score > highest_score_so_far:
                    highest_score_so_far, best_move_so_far = score, move
            return highest_score_so_far, best_move_so_far
        else:
            for move in legal_moves:
                # Evaluate this move in depth.
                score, _ = self.minimax(game.forecast_move(move), depth-1, maximizing_player=True)
                # If this branch yields a sure win, no need to search further. Otherwise, remember the best move.
                if score == float("-inf"):
                    return score, move
                if score < lowest_score_so_far:
                    lowest_score_so_far, best_move_so_far = score, move
            return lowest_score_so_far, best_move_so_far

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

        # If we started the game.Take the center move.
        if game.move_count == 0:
            return(int(game.height/2), int(game.width/2))

        #Search for a good move!
        best_move_so_far = (-1, -1)

        try:
            """
            The try and catch block will help us to evaluate the status of the both
            the methods minimax and alphabeta when the time is getting near.
            """
            if self.iterative == True:
                iterative_search_depth = 1
                if self.method == 'alphabeta':
                    while True:
                        best_score_so_far, best_move_so_far = self.alphabeta(game, iterative_search_depth)
                        if best_score_so_far == float("inf") or best_score_so_far == float("-inf"):
                            break
                        iterative_search_depth += 1
            else:
                
                 _, best_move_so_far = self.alphabeta(game, self.search_depth)
               
        except Timeout:
            # Handle any actions required at timeout, if necessary
            pass

        # Return the best move from the last completed search iteration
        return best_move_so_far

    def alphabeta(self, game, depth, alpha=float("-inf"), beta=float("inf"), maximizing_player=True):
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

        maximizing_player : bool
            Flag indicating whether the current search depth corresponds to a
            maximizing layer (True) or a minimizing layer (False)

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
            raise Timeout()

        # Are there any legal moves left for us to play? If not, then we lost!
        # The maximizing (minimizing) player returns the lowest (highest) possible score.
        legal_moves = game.get_legal_moves()
        if not legal_moves:
            if maximizing_player == True:
                return float("-inf"), (-1, -1)
            else:
                return float("inf"), (-1, -1)

        """
        If there are legal moves and we don't reach the search depth

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
                # Evaluate this move in depth.
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

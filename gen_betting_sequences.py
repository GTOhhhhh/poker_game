from typing import Generator, List, Tuple, Optional

# Constants
CHECK = "CHECK"
BET = "BET"
FOLD = "FOLD"
CALL = "CALL"
RAISE = "RAISE"


def gen_betting_sequences(
    current_player: int,
    aggressor: Optional[int],
    sequence: List[str],
    players_remaining: List[bool],
    pot: int,
) -> Generator[Tuple[List[str], int], None, None]:
    """
    A generator function that yields all possible betting sequences in a poker game
    given the current state of the game.

    Parameters:
        current_player (int): The player whose turn it is.
        aggressor (Optional[int]): The player who made the last bet or raise, if any.
        sequence (List[str]): The sequence of actions taken so far.
        players_remaining (List[bool]): A list indicating which players are still in the game.
        pot (int): Current pot amount.

    Yields:
        Tuple[List[str], int]: A possible betting sequence and the resulting pot.
    """

    # Display the sequence and pot for debugging purposes
    if sequence:
        print(f"{'-'.join(sequence)} = {pot}")

    # Halting conditions
    # The current player cannot perform any action since they already folded
    if not players_remaining[current_player]:
        yield sequence, pot
        return

    # All players have checked
    elif len(sequence) == 3 and all(a == CHECK for a in sequence):
        yield sequence, pot
        return

    # The last bet has been matched
    elif current_player == aggressor:
        yield sequence, pot
        return

    # Only one player has not already folded
    elif players_remaining.count(True) == 1:
        yield sequence, pot
        return

    # Determine the current state of the round
    is_raised = RAISE in sequence
    players_prior_action = sequence[-3] if len(sequence) > 2 else None

    # Decision tree based on game state
    # If there is no bet yet, CHECK or BET is allowed
    if aggressor is None and not is_raised:
        yield from gen_betting_sequences(
            (current_player + 1) % 3, aggressor, sequence + [CHECK], players_remaining, pot
        )
        yield from gen_betting_sequences(
            (current_player + 1) % 3, current_player, sequence + [BET], players_remaining, pot + 10
        )

    # If there is a bet but no raise yet, CALL, FOLD, or RAISE is allowed
    elif (aggressor is not None) and (not is_raised):
        yield from gen_betting_sequences(
            (current_player + 1) % 3,
            aggressor,
            sequence + [FOLD],
            players_remaining[:current_player] + [False] + players_remaining[current_player + 1 :],
            pot,
        )
        yield from gen_betting_sequences(
            (current_player + 1) % 3, aggressor, sequence + [CALL], players_remaining, pot + 10
        )
        yield from gen_betting_sequences(
            (current_player + 1) % 3,
            current_player,
            sequence + [RAISE],
            players_remaining,
            pot + 20,
        )

    # If there is a raise, CALL or FOLD is allowed
    elif is_raised:
        yield from gen_betting_sequences(
            (current_player + 1) % 3,
            aggressor,
            sequence + [FOLD],
            players_remaining[:current_player] + [False] + players_remaining[current_player + 1 :],
            pot,
        )
        call_amount = 20 if players_prior_action in [CHECK, None] else 10
        yield from gen_betting_sequences(
            (current_player + 1) % 3,
            aggressor,
            sequence + [CALL],
            players_remaining,
            pot + call_amount,
        )


if __name__ == "__main__":
    generated_sequences = gen_betting_sequences(
        current_player=0, aggressor=None, sequence=[], players_remaining=[True, True, True], pot=60
    )
    for _, _ in enumerate(generated_sequences):
        pass

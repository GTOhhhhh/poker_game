from poker_game import BET, CALL, CHECK, FOLD, RAISE, gen_betting_sequences, PokerGame

EXPECTED_SEQUENCES_WITH_POT = {
        (CHECK, CHECK, CHECK): 60,
        (CHECK, CHECK, BET, FOLD, FOLD): 70,
        (CHECK, CHECK, BET, FOLD, CALL): 80,
        (CHECK, CHECK, BET, FOLD, RAISE, FOLD): 90,
        (CHECK, CHECK, BET, FOLD, RAISE, CALL): 100,
        (CHECK, CHECK, BET, CALL, FOLD): 80,
        (CHECK, CHECK, BET, CALL, CALL): 90,
        (CHECK, CHECK, BET, CALL, RAISE, FOLD, FOLD): 100,
        (CHECK, CHECK, BET, CALL, RAISE, FOLD, CALL): 110,
        (CHECK, CHECK, BET, CALL, RAISE, CALL, FOLD): 110,
        (CHECK, CHECK, BET, CALL, RAISE, CALL, CALL): 120,
        (CHECK, CHECK, BET, RAISE, FOLD, FOLD): 90,
        (CHECK, CHECK, BET, RAISE, FOLD, CALL): 100,
        (CHECK, CHECK, BET, RAISE, CALL, FOLD): 110,
        (CHECK, CHECK, BET, RAISE, CALL, CALL): 120,
        (CHECK, BET, FOLD, FOLD): 70,
        (CHECK, BET, FOLD, CALL): 80,
        (CHECK, BET, FOLD, RAISE, FOLD): 90,
        (CHECK, BET, FOLD, RAISE, CALL): 100,
        (CHECK, BET, CALL, FOLD): 80,
        (CHECK, BET, CALL, CALL): 90,
        (CHECK, BET, CALL, RAISE, FOLD, FOLD): 100,
        (CHECK, BET, CALL, RAISE, FOLD, CALL): 110,
        (CHECK, BET, CALL, RAISE, CALL, FOLD): 110,
        (CHECK, BET, CALL, RAISE, CALL, CALL): 120,
        (CHECK, BET, RAISE, FOLD, FOLD): 90,
        (CHECK, BET, RAISE, FOLD, CALL): 100,
        (CHECK, BET, RAISE, CALL, FOLD): 110,
        (CHECK, BET, RAISE, CALL, CALL): 120,
        (BET, FOLD, FOLD): 70,
        (BET, FOLD, CALL): 80,
        (BET, FOLD, RAISE, FOLD): 90,
        (BET, FOLD, RAISE, CALL): 100,
        (BET, CALL, FOLD): 80,
        (BET, CALL, CALL): 90,
        (BET, CALL, RAISE, FOLD, FOLD): 100,
        (BET, CALL, RAISE, FOLD, CALL): 110,
        (BET, CALL, RAISE, CALL, FOLD): 110,
        (BET, CALL, RAISE, CALL, CALL): 120,
        (BET, RAISE, FOLD, FOLD): 90,
        (BET, RAISE, FOLD, CALL): 100,
        (BET, RAISE, CALL, FOLD): 110,
        (BET, RAISE, CALL, CALL): 120,
    }

def test_gen_betting_sequences():
    # Generate betting sequences
    generated_sequences = list(
        gen_betting_sequences(
            current_player=0,
            aggressor=None,
            sequence=[],
            players_remaining=[True, True, True],
            pot=60,
        )
    )

    # Convert the generated sequences into a dictionary
    generated_sequences = {tuple(seq): pot for seq, pot in generated_sequences}

    # Assert that the generated sequences match the expected sequences
    assert (
        generated_sequences == EXPECTED_SEQUENCES_WITH_POT
    ), f"Generated sequences do not match expected sequences"


def test_gen_betting_sequences_oop():
    # Instantiate the PokerGame object for OOP approach
    game = PokerGame()

    # Generate betting sequences
    generated_sequences = list(game.gen_betting_sequences())

    # Convert the generated sequences into a dictionary
    generated_sequences = {tuple(seq): pot for seq, pot in generated_sequences}

    # Assert that the generated sequences match the expected sequences
    assert (
        generated_sequences == EXPECTED_SEQUENCES_WITH_POT
    ), f"Generated sequences do not match expected sequences"

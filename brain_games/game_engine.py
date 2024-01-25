import prompt

NUMBER_OF_QUESTIONS_IN_GAME = 3


def run_game(game_module):
    """Common function for all games.

    First parameter: The rules of the right game.

    Second parameter: The function that is implemented in the desired game,
    which returns the question condition for the player and the expected result
    from the user.

    This function also implements a greeting, a request for a player's response,
     a comparison with the expected result and the end of the game."""

    name_player = prompt.string("Welcome to the Brain Games!\n"
                                "May I have your name? ")
    print(f"Hello, {name_player}!\n{game_module.GAME_RULES}")

    for _ in range(NUMBER_OF_QUESTIONS_IN_GAME):
        question_to_player, right_answer = game_module.get_question_and_answer()
        response_player = prompt.string(f"Question: {question_to_player}\n"
                                        "Your answer: ")

        if response_player != right_answer:
            print(f"'{response_player}' is wrong answer :(. "
                  f"Correct answer was '{right_answer}'\n"
                  f"Let's try again, {name_player}!")
            return
        else:
            print('Correct!')
    else:
        print(f"Congratulations, {name_player}!")

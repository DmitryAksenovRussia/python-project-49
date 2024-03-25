import prompt

NUMBER_OF_QUESTIONS_IN_GAME = 3


def run(game):
    """Common function for all games.

    Parameter: Game module that has RULES attributes (rules of the current game)
    and a function that returns the question condition for the player
    and the expected result from the player.

    This function also implements a greeting, a request for a player's response,
     a comparison with the expected result and the end of the game."""

    print("Welcome to the Brain Games!")
    name_player = prompt.string("May I have your name? ")

    print(f"Hello, {name_player}!")
    print(game.RULES)

    for _ in range(NUMBER_OF_QUESTIONS_IN_GAME):
        question_to_player, right_answer = game.get_question_and_answer()
        print(f"Question: {question_to_player}")
        response_player = prompt.string("Your answer: ")

        if response_player != right_answer:
            print(f"'{response_player}' is wrong answer :(. "
                  f"Correct answer was '{right_answer}'\n"
                  f"Let's try again, {name_player}!")
            return
        else:
            print('Correct!')
    else:
        print(f"Congratulations, {name_player}!")

from brain_games.cli import welcome_user
import prompt

NUMBER_OF_QUESTIONS_IN_GAME = 3


def input_response_from_player():
    """The function reads the player's response from the console and returns it."""

    response = prompt.string("Your answer: ")
    return response


def print_wrong_answer_sentense(response_player, right_answer, name_player):
    """The function prints a message with the player's incorrect answer
    and correct answer."""

    print(f"'{response_player}' is wrong answer :(. Correct answer was '{right_answer}'")
    print(f"Let's try again, {name_player}!")


def run_game(game_rules, current_game):
    """Common function for all games.

    First parameter: The rules of the right game.

    Second parameter: The function that is implemented in the desired game,
    which returns the question condition for the player and the expected result
    from the user.

    This function also implements a greeting, a request for a player's response,
     a comparison with the expected result and the end of the game."""

    name_player = welcome_user()
    print(game_rules)

    for _ in range(NUMBER_OF_QUESTIONS_IN_GAME):
        question_to_player, right_answer = current_game()
        print(f"Question: {question_to_player}")
        response_player = input_response_from_player()

        if response_player != right_answer:
            print_wrong_answer_sentense(response_player, right_answer, name_player)
            return
        else:
            print('Correct!')

    print(f"Congratulations, {name_player}!")

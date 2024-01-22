from brain_games.cli import welcome_user
import prompt

NUMBER_OF_QUESTIONS_IN_GAME = 3


def input_response_from_player():
    """The function return response from console"""
    response = prompt.string("Your answer: ")
    return response


def print_wrong_answer_sentense(answer_player, right_answer, name_player):
    """The function accept a player's response and if it's wrong:
     print 'wrong answer'"""
    print(f"'{answer_player}' is wrong answer :(. Correct answer was '{right_answer}'")
    print(f"Let's try again, {name_player}")


def run_game(game_rules, current_game):
    name_player = welcome_user()
    print(game_rules)

    for _ in range(NUMBER_OF_QUESTIONS_IN_GAME):
        question_to_player, right_answer = current_game()
        print(f"Question: {question_to_player}")
        player_answer = input_response_from_player()

        if player_answer != right_answer:
            print_wrong_answer_sentense(player_answer, right_answer, name_player)
            return
        else:
            print('Correct!')
    print(f"Congratulations, {name_player}!")

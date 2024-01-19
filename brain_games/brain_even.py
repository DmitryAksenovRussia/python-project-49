import random
import prompt

NUMBER_OF_QUESTIONS_IN_GAME = 3


def generating_random_number_for_question():
    """The function generate a random number from 0 to 100"""
    return random.randint(0, 100)


def ask_player():
    """The function print the generated question to the console"""
    random_number = generating_random_number_for_question()
    print(f"Question: {random_number}")
    return random_number


def input_response_from_player():
    """The function return response from console"""
    response = prompt.string("Your answer: ")
    return response


def print_wrong_answer_sentense(answer_player, right_answer):
    """the function accept a player's response and if it's wrong:
     print 'wrong answer'"""
    print(f"'{answer_player}' is wrong answer :(. ", end='')
    print(f"Correct answer was '{right_answer}'")


def play_brain_even():
    number_of_questions_in_game = NUMBER_OF_QUESTIONS_IN_GAME
    flag_for_wrong_answer = False
    while number_of_questions_in_game > 0:
        randon_number = ask_player()
        answer_of_question = input_response_from_player()
        if randon_number % 2 == 0 and answer_of_question != 'yes':
            print_wrong_answer_sentense(answer_of_question, 'yes')
            flag_for_wrong_answer = True
        elif randon_number % 2 == 1 and answer_of_question != 'no':
            print_wrong_answer_sentense(answer_of_question, 'no')
            flag_for_wrong_answer = True
        if flag_for_wrong_answer:
            break
        print('Correct!')
        number_of_questions_in_game -= 1
    return flag_for_wrong_answer


if __name__ == '__main__':
    play_brain_even()

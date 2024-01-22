from brain_games.game_engine.game_engine import run_game
import random


GAME_RULES = 'Answer "yes" if the number is even, otherwise answer "no".'
MIN_RANDOM_NUMBER = 1
MAX_RANDOM_NUMBER = 100


def is_even(number):
    return number % 2 == 0


def get_number_and_even_answer():
    number = random.randint(MIN_RANDOM_NUMBER, MAX_RANDOM_NUMBER)
    question_to_player = str(number)
    right_answer = 'yes' if is_even(number) else 'no'

    return question_to_player, right_answer


def brain_even():
    run_game(GAME_RULES, get_number_and_even_answer)

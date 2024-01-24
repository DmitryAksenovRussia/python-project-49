from brain_games.game_engine import run_game
import random

GAME_RULES = 'Answer "yes" if given number is prime. Otherwise answer "no".'
MIN_RANDOM_NUMBER = 1
MAX_RANDOM_NUMBER = 100


def is_prime(number: int) -> bool:
    """The function checks whether the number is prime or not."""

    if number < 2:
        return False

    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False

    return True


def get_number_and_prime_answer() -> tuple:
    """The function returns a number and the answer
     is whether the number is prime."""

    number = random.randint(MIN_RANDOM_NUMBER, MAX_RANDOM_NUMBER)
    answer = 'yes' if is_prime(number) else 'no'

    return str(number), answer


def brain_prime():
    run_game(GAME_RULES, get_number_and_prime_answer)

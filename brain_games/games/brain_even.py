import random


RULES = 'Answer "yes" if the number is even, otherwise answer "no".'
MIN_RANDOM_NUMBER = 1
MAX_RANDOM_NUMBER = 100


def is_even(number: int) -> bool:
    """The function returns whether the number is even or not."""

    return number % 2 == 0


def get_number_and_even_answer() -> tuple:
    """The function returns a number and the answer
    is whether the number is even or not."""

    number = random.randint(MIN_RANDOM_NUMBER, MAX_RANDOM_NUMBER)
    right_answer = 'yes' if is_even(number) else 'no'

    return str(number), right_answer


def get_question_and_answer():
    return get_number_and_even_answer()

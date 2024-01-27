import random
import math

RULES = "Find the greatest common divisor of given numbers."
MIN_RANDOM_NUMBER = 1
MAX_RANDOM_NUMBER = 100


def get_nums_pair_and_gcd() -> tuple:
    """The function generates a pair of numbers
     and calculates gcd."""

    number_1 = random.randint(MIN_RANDOM_NUMBER, MAX_RANDOM_NUMBER)
    number_2 = random.randint(MIN_RANDOM_NUMBER, MAX_RANDOM_NUMBER)

    nums_pair = f'{number_1} {number_2}'
    gcd = math.gcd(number_1, number_2)

    return nums_pair, str(gcd)


def get_question_and_answer():
    return get_nums_pair_and_gcd()

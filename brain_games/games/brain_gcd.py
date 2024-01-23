from brain_games.game_engine.game_engine import run_game
import random
import math

GAME_RULES = "Find the greatest common divisor of given numbers"
MIN_RANDOM_NUMBER = 1
MAX_RANDOM_NUMBER = 100


def get_nums_pair_and_gcd():
    number_1 = random.randint(MIN_RANDOM_NUMBER, MAX_RANDOM_NUMBER)
    number_2 = random.randint(MIN_RANDOM_NUMBER, MAX_RANDOM_NUMBER)
    nums_pair = f'{number_1} {number_2}'
    gcd = math.gcd(number_1, number_2)

    return nums_pair, str(gcd)


def brain_gcd():
    run_game(GAME_RULES, get_nums_pair_and_gcd)

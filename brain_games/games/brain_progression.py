import random


RULES = 'What number is missing in the progression?'
MIN_LENGHT_PROGRESSION = 5
MAX_LENGHT_PROGRESSION = 10
MIN_RANDOM_NUMBER = 1
MAX_RANDON_NUMBER = 100
MAX_STEP_PROGRESSION = 10


def get_progression_and_missed_number() -> tuple:
    """The function generates an arithmetic progression, removes one element
     and returns them."""

    start = random.randint(MIN_RANDOM_NUMBER, MAX_RANDON_NUMBER)
    step = random.randint(MIN_RANDOM_NUMBER, MAX_STEP_PROGRESSION)
    size = random.randint(MIN_LENGHT_PROGRESSION, MAX_LENGHT_PROGRESSION)

    progression = list(range(start, step*size + start, step))
    missed_index = random.randint(0, size - 1)
    missed_number = progression[missed_index]
    progression[missed_index] = '..'

    return ' '.join(map(str, progression)), str(missed_number)


def get_question_and_answer():
    return get_progression_and_missed_number()

import random


RULES = 'What is the result of the expression?'
MATH_SIGNS = ('+', '-', '*')
MIN_RANDOM_NUMBER = 1
MAX_RANDOM_NUMBER = 100


def calculate_result(number_1: int, number_2: int, math_sign: str) -> int:
    """The function calculates the value between two numbers
    according to the passed sign."""

    if math_sign == '+':
        return number_1 + number_2
    elif math_sign == '-':
        return number_1 - number_2
    elif math_sign == '*':
        return number_1 * number_2


def get_math_expression_and_result() -> tuple:
    """The function returns the generated expression
    between two numbers and result of its calculation"""

    number_1 = random.randint(MIN_RANDOM_NUMBER, MAX_RANDOM_NUMBER)
    number_2 = random.randint(MIN_RANDOM_NUMBER, MAX_RANDOM_NUMBER)
    math_sign = random.choice(MATH_SIGNS)

    expression = f'{number_1} {math_sign} {number_2}'
    result = calculate_result(number_1, number_2, math_sign)

    return expression, str(result)


def get_question_and_answer():
    return get_math_expression_and_result()

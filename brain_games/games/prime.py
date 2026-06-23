"""Логика"""

import random


def get_rules():
    return 'Answer "yes" if given number is prime. Otherwise answer "no".'

def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    i = 3
    while i * i <= n:
        if n % i == 0:
            return False
        i += 2

    return True

def get_question_and_answer():
    num = random.randint(1, 25)
    if is_prime(num):
        answer = "yes"
    else:
        answer = "no"
    return str(num), answer

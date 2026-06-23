"""Логика"""

import random


def get_rules():
    return 'What number is missing in the progression?'

def get_question_and_answer():
    start = random.randint(1, 20)
    step = random.randint(2, 15)
    length = random.randint(10, 10)
    progression = []

    for i in range(length):
        num = start + i * step
        progression.append(num)

    index = random.randint(0, length - 1)
    answer = progression[index]
    progression[index] = ".."

    question = " ".join(map(str, progression))
    return question, str(answer)

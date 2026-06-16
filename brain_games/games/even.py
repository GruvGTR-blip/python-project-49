"""Логика игры"""

import random


def run_even(name):
    print('Answer "yes" if the number is even, otherwise answer "no".')
    index = 0
    while index  < 3:
        num = random.randint(1, 100)
        print(f'Question: {num}')
        answer_user = input("Your answer: ").lower()
        if num % 2 == 0:
            right_answer = 'yes'
        else:
            right_answer = 'no'
        if answer_user == right_answer:
            print('Correct!')
            index += 1
        else:
            print(f'"{answer_user}" is wrong answer ;(. Correct answer was "{right_answer}".')
            print(f'Let`s try again, {name}!')
            return

    print(f'Congratulations, {name}!')

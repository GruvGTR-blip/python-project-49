"""Логика Калькулятора"""

import random


def get_rules():
    """Правила"""
    return "What is the result of the expression?"


def get_question_and_answer():
    """Генерирует математическое выражение и ответ"""
    num1 = random.randint(1, 100)
    num2 = random.randint(1, 100)
    operation = random.choice(["+", "-", "*"])

    if "+" == operation:
        result = num1 + num2
    elif "-" == operation:
        result = num1 - num2
    else:
        result = num1 * num2

    question = f"{num1} {operation} {num2}"
    return question, str(result)

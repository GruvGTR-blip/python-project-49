#!/usr/bin/env python3

"""Приветствие запуск игры"""

from brain_games.cli import welcome_user
from brain_games.engine import run_game
from brain_games.games.calc import get_question_and_answer, get_rules


def main():
    name = welcome_user()
    run_game(get_question_and_answer, get_rules, name)


if __name__ == "__main__":
    main()

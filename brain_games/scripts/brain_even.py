#!/usr/bin/env python3
"""Фаил запуска. Он здоровается с игроком, после чего запускает игру."""

from brain_games.cli import welcome_user
from brain_games.games.even import run_even


def main():
    """Приветствие, запуск """
    name = welcome_user()
    run_even(name)

if __name__ == "__main__":
    main()

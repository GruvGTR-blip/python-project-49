"""Движок"""


def run_game(question_answer, rules, name):
    print(rules())
    count = 0
    while count < 3:
        question, answer = question_answer()
        print(f"Question: {question}")
        user_answer = input("Your answer: ").lower()
        if user_answer == answer:
            print("Correct!")
            count += 1
        else:
            print(
                f"'{user_answer}' is wrong answer ;(. Correct answer was '{answer}'."
            )
            print(f"Let's try again, {name}!")
            return
    print(f"Congratulations, {name}!")

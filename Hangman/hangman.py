""" The Hangman Project """
import random

print("""HANGMAN
The game will be available soon.
""")

programming_languages = ["python", "java", "javascript", "php"]
answer = random.choice(programming_languages)
answer_list = list(answer)
answer_print = "-" * (len(answer))
attempts_left = 8
guessed_letters = []


def check_answer():
    global answer_print
    for i in range(len(answer)):
        if answer_list[i] == user_answer:
            answer_print = answer_print[:i] + user_answer + answer_print[i + 1:]
            print(answer_print)


def check_guessed():
    if user_answer in guessed_letters:
        print("You already guessed this letter.")


while True:
    print('Type "play" to play the game, "exit" to quit:')
    user_choice = input()
    if user_choice == "play":
        while attempts_left > 0:
            print(answer_print)
            user_answer = input("Input a letter:")

            if not user_answer.isalpha() and user_answer.islower():
                print("Please enter a lowercase English letter")
                continue

            if len(user_answer) != 1:
                print("You should input a single letter")
                continue

            check_guessed()

            if user_answer in answer_list:
                guessed_letters.append(user_answer)
                check_answer()
                if "-" not in answer_print:
                    print("You guess the word! \n" + "You survived")
                    break
            else:
                attempts_left -= 1
                print("That letter doesn't appear in the word")
        else:
            print("You lost!")
    elif user_choice == "exit":
        break

"""The Dinnerparty project"""

import random

friends_joining = int(input("Enter the number of friends joining (including you):"))


def check_total_friends():
    while len(friends_dict) < friends_joining:
        friend_name = input()
        total_friends.append(friend_name)
        friends_dict[friend_name] = 0


def choose_lucky():
    while True:
        global lucky
        if lucky == "Yes":
            lucky_friend = random.choice(list(friends_dict.keys()))
            print(f"{lucky_friend} is the lucky one!")
            total_friends_length = len(total_friends) - 1
            friend_amount = total_amount / total_friends_length
            friend_amount = round(friend_amount, 2)
            for friend in friends_dict:
                if friend == lucky_friend:
                    friends_dict[friend] = 0
                else:
                    friends_dict[friend] = friend_amount
            print(friends_dict)
            break  # Exit the loop after choosing a lucky friend
        elif lucky == "No":
            print("No one is going to be lucky")
            friend_amount = total_amount / len(total_friends)
            friend_amount = round(friend_amount, 2)
            for friend in friends_dict:
                friends_dict[friend] = friend_amount
            print(friends_dict)
            break  # Exit the loop if no lucky friend
        else:
            if lucky not in ["Yes", "No", "Exit"]:
                print("Enter the correct value or type 'Exit' to exit.")
                lucky = input("Do you want to use the 'Who is lucky?' feature? Write Yes/No: \n ")
            elif lucky == "Exit":
                break


if friends_joining < 1:
    print("No one is joining for the party")
else:
    friends_dict = {}
    total_friends = []
    print("Enter the name of every friend (including you), each on a new line:")
    check_total_friends()
    total_amount = int(input("Enter the total amount: \n"))
    lucky = input("Do you want to use the 'Who is lucky?' feature? Write Yes/No: \n ")
    choose_lucky()

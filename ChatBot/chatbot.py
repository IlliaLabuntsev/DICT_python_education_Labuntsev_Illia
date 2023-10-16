""" ChatBot project """
# About ChatBot
bot_name = "ChatBot"
birth_year = "2023"
print("Hello my name is" + " " + str(bot_name) + "\n I was created in" + " " + str(birth_year))

# Name
print("Please, remind me your name.")
your_name = input()
print("What a great name you have," + " " + str(your_name))

# Age
print("Let me guess your age.")
print("Enter remainders of dividing your age by 3, 5 and 7.")
remainder3 = input()
remainder5 = input()
remainder7 = input()
age = (int(remainder3) * 70 + int(remainder5) * 21 + int(remainder7) * 15) % 105
print("Your age is" + " " + str(age) + ";" + " " + "that's good time to start programming!")

# Count number
print("Now I will prove to you that I can count to any number you want")
number_input = int(input())
for i in range (number_input + 1):
    print(i, "!")
# Questions
print("Let's test your programming knowledge.")
print("Why do we use methods?")
print("1. To repeat a statement multiple times.")
print("2. To decompose a program into several small subroutines.")
print("3. To determine the execution time of a program.")
print("4. To interrupt the execution of a program.")

while True:
    user_answer = int(input("Enter your answer:"))
    if user_answer == 2:
        print("Completed, have a nice day!")
        break
    print("Please, try again.")

print("Congratulations have a nice day!")

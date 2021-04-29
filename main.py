"""
Simulates a magic eight ball.
Prompts the user to type a yes or no question and gives
a random answer from a set of prefabricated responses.
"""
import random

ANSWER_1 = "As I see it, yes."
ANSWER_2 = "Ask again later."
ANSWER_3 = "Better not to tell you now."
ANSWER_4 = "Cannot predict now."
ANSWER_5 = "Concentrate and ask again."
ANSWER_6 = "Don't count on it."
ANSWER_7 = "It is certain."
ANSWER_8 = "It is decidedly so."
ANSWER_9 = "Most likely."
ANSWER_10 = "My reply is no."
ANSWER_11 = "My sources say no."
ANSWER_12 = "Outlook not so good."
ANSWER_13 = "Outlook good."
ANSWER_14 = "Reply hazy, try again."
ANSWER_15 = "Signs point to yes."
ANSWER_16 = "Very doubtful."
ANSWER_17 = "Without a doubt."
ANSWER_18 = "Yes."
ANSWER_19 = "Yes - definitely."
ANSWER_20 = "You may rely on it."

def main():
    question = input("Ask a yes or no question: ")
    while question != "":
        answer_the_question()
        question = input("Ask a yes or no question: ")
    else: # User enters no question
        print("No question")

# A function that produces a random response
def answer_the_question():
    random_number = random.randint(1, 20)
    if random_number == 1:
        print(ANSWER_1)
    elif random_number == 2:
        print(ANSWER_2)
    elif random_number == 3:
        print(ANSWER_3)
    elif random_number == 4:
        print(ANSWER_4)
    elif random_number == 5:
        print(ANSWER_5)
    elif random_number == 6:
        print(ANSWER_6)
    elif random_number == 7:
        print(ANSWER_7)
    elif random_number == 8:
        print(ANSWER_8)
    elif random_number == 9:
        print(ANSWER_9)
    elif random_number == 10:
        print(ANSWER_10)
    elif random_number == 11:
        print(ANSWER_11)
    elif random_number == 12:
        print(ANSWER_12)
    elif random_number == 13:
        print(ANSWER_13)
    elif random_number == 14:
        print(ANSWER_14)
    elif random_number == 15:
        print(ANSWER_15)
    elif random_number == 16:
        print(ANSWER_16)
    elif random_number == 17:
        print(ANSWER_17)
    elif random_number == 18:
        print(ANSWER_18)
    elif random_number == 19:
        print(ANSWER_19)
    elif random_number == 20:
        print(ANSWER_20)


if __name__ == "__main__":
    main()
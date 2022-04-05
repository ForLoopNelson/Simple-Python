from random import choice

questions = ["How far away is the sun?:  ",
                     "Why is the earth round?:  ",
                     "Do animals know they are alive?:  ",
                     "Why is the sky blue?: "]

question = choice(questions)
answer= input(question).strip().lower()

while answer != "just because":
    answer = input("why?: ").strip().lower()

print("Oh, Okay...")


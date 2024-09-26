from art import logo, vs
from dane import data
import random

print(logo)


def game():
    score = 0
    celebrity_a = random.choice(data)
    celebrity_b = random.choice(data)
    a_follows = celebrity_a["follower_count"]
    b_follows = celebrity_b["follower_count"]
    while True:
        print(f"Compare A: {celebrity_a["name"]}, {celebrity_a["description"]}, from {celebrity_a["country"]}")
        print(vs)
        print(f"Compare B: {celebrity_b["name"]}, {celebrity_b["description"]}, from {celebrity_b["country"]}")

        question1 = input("Who has more followers? Type 'A' or 'B' ").upper()
        if question1 == "A":
            if a_follows > b_follows:
                score += 1
                print(f"You're right! Your current score: {score}")
                celebrity_b = random.choice(data)
                b_follows = celebrity_b["follower_count"]
            else:
                print(f"You lose! Your score: {score}")
                break
        elif question1 == "B":
            if a_follows < b_follows:
                score += 1
                print(f"You're right! Your current score: {score}")
                celebrity_a = random.choice(data)
                a_follows = celebrity_a["follower_count"]
            else:
                print(f"You lose! Your score: {score}")
                break


game()
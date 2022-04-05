# Race game using dice

import random

dice = [1, 2, 3, 4, 5, 6]
your_steps = 0
computer_steps = 0
is_over = False
play_again = True
points = 0

print("Welcome to the race game!\n"
      "You'll be rolling a dice in order to move along the steps.\n"
      "You have between 30 and 35 steps to reach the finish line.")
play = input("Do you want to play the race game alone or against the computer? Type 'a' or 'c': ")


# Playing alone

if play == 'a':
    while play_again:
        difficulty = input("Enter difficulty level, 'hard' or 'easy': ")
        if difficulty == 'hard':
            moves = 8
        elif difficulty == 'easy':
            moves = 10

        while not is_over:
            roll_number = random.choice(dice)
            your_steps += roll_number
            moves -= 1
            print(f"You are at step {your_steps}, left with {moves} moves.")
            if moves == 0:
                is_over = True
                print("\nYou went out of moves.")
                if 30 <= your_steps <= 35:
                    points += 1
                    print(f"You arrived still, you win with {points} point.")
                else:
                    print("You lose")
            elif 30 <= your_steps <= 35:
                is_over = True
                points += 3
                print(f"\nYou arrived on time, you win with {points} points.")
        decision = input("Do you want to race again?")
        if decision == 'n':
            play_again = False
            print(f"Total points: {points}")
        else:
            is_over = False
            your_steps = 0


# Playing against computer
elif play == 'c':
    while not is_over:
        your_roll_number = random.choice(dice)
        computer_roll_number = random.choice(dice)
        your_steps += your_roll_number
        computer_steps += computer_roll_number
        print(f"You are at step {your_steps}, opponent at step {computer_steps}.")
        if (30 <= computer_steps <= 35) and (your_steps < 30 or your_steps > 35):
            is_over = True
            print("\nOpponent arrived before you, you lose")
        elif (30 <= your_steps <= 35) and (computer_steps < 30 or computer_steps > 35):
            is_over = True
            print("\nYou arrived before opponent, you win")
        elif 30 <= computer_steps <= 35 and 30 <= your_steps <= 35:
            is_over = True
            print("\nYou arrived at the same time, it's a draw.")

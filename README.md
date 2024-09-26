## Higher or Lower: Celebrity Followers Game
This is a command-line game where you compare two celebrities and guess who has more followers on social media. The goal is to keep guessing correctly to achieve the highest score.

## Features
    - Celebrity Comparison: The game shows two celebrities, and you must guess who has more followers.
    - Score Tracking: Each correct guess increases your score.
    - Random Celebrities: After each round, a new random celebrity is chosen for comparison.
    - Game Over: The game ends when you make an incorrect guess.
## How to Play
    Start: Two celebrities are shown with descriptions.
    Guess: Input 'A' or 'B' depending on who you think has more followers.
    Continue: If correct, your score increases, and a new comparison is made.
    Game Over: If wrong, the game ends, showing your final score.
## Example
    Compare A: Celebrity A - Singer, from the USA.
    VS
    Compare B: Celebrity B - Footballer, from Portugal.
    You need to choose who has more followers based on their profession and fame.

## Code Overview
    game(): Main function that runs the game. It randomly selects two celebrities, compares their follower counts, and prompts the player for input. The score increases with each correct guess.
    Data: Celebrity data is stored in the data list, containing information such as name, description, and follower count.
    Requirements
    Python 3.x
    art package for displaying logos and visual separators.
## Install the required package:
    pip install art
## Running the Game
    Run the game using the command:

    -python higher-lower.py
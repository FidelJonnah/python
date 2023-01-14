import time
from typing import Dict

level = 1
time_left = 20
score = 0

words = {1: {"python": "A popular programming language", 
             "programming": "The process of creating software", 
             "typing": "The process of entering text using a keyboard"},
         2: {"algorithm": "A set of instructions for solving a problem", 
             "debugging": "The process of finding and fixing errors in code", 
             "recursion": "A programming technique where a function calls itself"},
         3: {"interpreter": "A program that executes code written in a high-level language", 
             "compiler": "A program that converts source code into machine code", 
             "binary": "A system of numerical notation that uses only two symbols (0 and 1)"}}

while level <= len(words):
    print(f"Level {level}")
    for word in words[level].keys():
        print(f"Type the following word: {word}")
        start_time = time.time()
        typed_word = input()
        if typed_word == word:
            score += 10
            print("Correct!")
            print(f"Score: {score}")
            time_left = float('inf')
        else:
            end_time = time.time()
            elapsed_time = end_time - start_time
            if elapsed_time > time_left:
                print("Time's up! Game over. Final score: ", score)
                exit()
            else:
                print("Incorrect. Do you want to trade 10 points to continue? (yes or no)")
                choice = input().lower()
                if choice == "yes":
                    score -= 10
                    print(f"Time left: {time_left} seconds")
                    print(f"Score: {score}")
                else:
                    print("Game over. Final score: ", score)
                    exit()
    level += 1
    time_left -= (level - 1) * 2

print("Congratulations! You have completed all levels. Final score: ", score)

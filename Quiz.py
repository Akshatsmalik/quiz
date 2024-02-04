import time
#more simple and readable boss
questions = [
    "What is the largest mammal on earth?",
    "What is the tallest building in the world?",
    "How many periodic elements are there?",
    "Which programming language is used most in the world?"
]

options = [
    ["A. Elephant", "B. Giraffe", "C. Whale", "D. Dolphin"],
    ["A. Burj Khalifa", "B. Eiffel Tower", "C. Twin Towers", "D. Statue of Liberty"],
    ["A. 120", "B. 69", "C. 420", "D. 118"],
    ["A. Python", "B. Javascript", "C. C++", "D. C"]
]

answers = ["C", "A", "D", "B"]
guesses = []
score = 0

for i, question in enumerate(questions):
    print("--------------------------------------------")
    print(f"{i + 1}. {question}\n")
    
    for option in options[i]:
        print(option)

    guess = input("\nTAKE A GUESS --- (A, B, C, D): ").upper()
    guesses.append(guess)

    if guess == answers[i]:
        score += 1
        time.sleep(2)
        print("CORRECT!\n")
    else:
        print(f"INCORRECT. The correct answer is {answers[i]}.\n")

print(f"You scored {score} out of {len(questions)}!")

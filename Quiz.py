import time
questions = (("What is the largeest mammel on earth"),
             ("what is the tallest building in the world"),
             ("how many periodic elements are there"),
             ("Which programing language is used mosed in the world"))

options = (("A. ELEPHANT", "B. GIRAAFE","C. WHALE","D. DOLPHIN"),
          ("A. Burj khalifa", "B. Eifel tower","C. Twin towers","D. Statue of liberty"),
          ("A. 120", "B. 69","C. 420","D. 118"),
          ("A. Python", "B. Javascript","C. C++","D. C"))

answers = ("C","A","D","B")
guesses = []
score = 0
question_num = 0

for question in questions:
    print("--------------------------------------------")
    print(question, end=" ")
    print()
    for option in options[question_num]:
        print(option)

    guess = input("TAKE A GUESS --- (A, B, C, D)-------------    ").upper()
    guesses.append(guess)
    if guess == answers[question_num]:
        score =+ 1
        time.sleep(2)
        print("CORRECT")
    
    else:
        print("u are.......")

        
        time.sleep(2)
        print("INCORRECT")
        print(f"{answers[question_num]} is the corrent answer")
     

    question_num += 1

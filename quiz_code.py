print("==============================")
print("Welcome to 'Quiz Game'😛!!")

question_bank = [
    {
        "text": "who invented python","answer": "B"
    },
    {
        "text": "which of the following is correct syntax for functions ", "answer": "D"
    },
    {
        "text": "which symbol we use to write comments", "answer": "A"
    },
    {
        "text": "meaning of class", "answer": "B"
    },
    {
        "text": "which defines the block of statements", "answer": "C"
    }
]

options = [
    [
        "A. James goesling", "B. Gudio Van Rossum", "C. Dennis Ritchie", "D. Jhon McCharthy"
    ],
    [
        "A. func()", "B. def funcname()", "C. def()", "D. def funcname():"
    ],
    [
        "A. #", "B. //", "C. !==", "D. =="
    ],
    [
        "A. it is a function", "B. blue print of an object", "C. it is a parameter", "D. block of statements"
    ],
    [
        "A. loops", "B. functions", "C. indentation", "D. conditional statements"
    ]
]
score = 0
def check_answer(user_guess,correct_answer):
    if user_guess==correct_answer:
        return True
    else:
        return False
for question_num in range(len(question_bank)):
    print("======================================")
    print(question_bank[question_num]["text"])
    for i in (options[question_num]):
        print(i)
    guess=input("select the option(A/B/C/D): ").upper()
    is_correct = check_answer(guess,question_bank[question_num]["answer"])
    if is_correct:
        print("correct answer")
        score = score + 1
    else:
        print("incorrect answer")
        print(f"the correct answer is {question_bank[question_num]["answer"]}")
    print(f"your score is {score}/{question_num+1}")
print(f"you have given {score} correct answer")
print(f"your score is {(score/(len(question_bank))*100)}%")
print("==================================================")
print("Thanks for attending the quiz, Have a nice day!!😛")

questions = [{"prompt": "What is the capital of France? ",
             "options": ["A. Paris", "B. London", "C. Berlin", "D. Madrid"],
             "answer": "A"},

             {"prompt": "Which language is primarily spoken in brazil? ",
              "options": ["A. Spanish", "B. Protuguese", "C. English", "D. French"],
              "answer": "B"},
               
             {"prompt": "What is the smallest prime number? ",
              "options": ["A. 1", "B. 2", "C. 3", "D. 5"],
                "answer": "B"},

             {"prompt": "Who wrote 'to kill a mocking bird'? ",
               "options": ["A. Harper Lee", "B. Mark Twain", "C. J.K. Rowling", "D. Ernest Hemingway"],
               "answer": "A"}]

def run_quiz(questions):
    print("\n")
    print("Here is your quiz. Please type the letter of your choice, not the actual answer.")
    print("\n")
    score = 0 
    for question in questions:
        print(question["prompt"])
        for option in (question["options"]):
            print(option)
        answer = input("Enter your answer here: ").upper()
        if answer ==  (question["answer"]):
            print("Correct!")
            score += 1
        else:
            print("Incorrect!")
        print("\n")
    print("\n")
    print(f"You got {score}/4 Correct!!")           
run_quiz(questions)

questions = [
    "What is the capital of India?",
    "Which planet is called the Red Planet?",
    "Who invented Python?"
]

answers = ["b", "a", "c"]

options = [
    ["a) Mumbai", "b) Delhi", "c) Kolkata", "d) Chennai"],
    ["a) Mars", "b) Earth", "c) Venus", "d) Jupiter"],
    ["a) Elon Musk", "b) Bill Gates", "c) Guido van Rossum", "d) Mark Zuckerberg"]
]

score = 0

for i in range(len(questions)):
    print("\n", questions[i])
    
    for option in options[i]:
        print(option)

    user_answer = input("Enter your answer: ").lower()

    if user_answer == answers[i]:
        print("Correct!")
        score += 1
    else:
        print("Wrong!")

print("\nQuiz Finished")
print("Your Score:", score, "/", len(questions))

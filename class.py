class Quiz:
    def __init__(self, questions):
        self.questions = questions
        self.score = 0

    def display_question(self, question):
        print(question["question"])
        for i, option in enumerate(question["options"], 1):
            print(f"{i}. {option}")
        user_answer = input("Enter your answer (1, 2, 3, 4): ")
        return int(user_answer) - 1

    def check_answer(self, question, user_answer):
        correct_option = question["answer"]
        if user_answer == correct_option:
            print("Correct!")
            self.score += 1
        else:
            print("Incorrect. The correct answer is:", question["options"][correct_option])

    def run_quiz(self):
        print("Welcome to the Basic Quiz Game!\n")
        for question in self.questions:
            user_answer = self.display_question(question)
            self.check_answer(question, user_answer)
            print()  # Add a newline for readability
        print("Quiz completed!")
        print("Your final score is:", self.score)


# Define your questions and options here
questions = [
    {
        "question": "What is the capital of France?",
        "options": ["Paris", "Rome", "Berlin", "Madrid"],
        "answer": 0
    },
    {
        "question": "What is the largest mammal?",
        "options": ["Elephant", "Blue Whale", "Giraffe", "Polar Bear"],
        "answer": 1
    },
    {
        "question": "Which planet is known as the Red Planet?",
        "options": ["Mars", "Venus", "Jupiter", "Mercury"],
        "answer": 0
    }
]

# Create an instance of the Quiz class and start the quiz
quiz = Quiz(questions)
quiz.run_quiz()

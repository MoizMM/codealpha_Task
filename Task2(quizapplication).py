# class Quiz:
#     def __init__(self):
#         self.questions = []

#     def add_question(self, question, options, correct_option):
#         """
#         Add a question to the quiz.
#         :param question: The question text
#         :param options: A list of options
#         :param correct_option: The index of the correct option in the options list
#         """
#         self.questions.append({'question': question, 'options': options, 'correct_option': correct_option})

#     def display_questions(self):
#         """
#         Display all questions in the quiz.
#         """
#         for i, data in enumerate(self.questions, 1):
#             print(f"{i}. {data['question']}")
#             for j, option in enumerate(data['options'], 1):
#                 print(f"   {j}. {option}")
#             print()

#     def take_quiz(self):
#         """
#         Allow a user to take the quiz and calculate the score.
#         """
#         score = 0
#         for data in self.questions:
#             print(data['question'])
#             for i, option in enumerate(data['options'], 1):
#                 print(f"{i}. {option}")
#             user_answer = int(input("Your answer (enter the number): "))
#             if user_answer == data['correct_option']:
#                 print("Correct!\n")
#                 score += 1
#             else:
#                 print(f"Wrong! The correct answer was {data['correct_option']}\n")
#         print(f"You scored {score}/{len(self.questions)}")


# class Administrator:
#     @staticmethod
#     def create_quiz():
#         quiz = Quiz()
#         num_questions = int(input("Enter the number of questions for the quiz: "))
#         for _ in range(num_questions):
#             question_text = input("Enter the question: ")
#             options = input("Enter options separated by commas: ").split(',')
#             correct_option = int(input("Enter the correct option number: "))
#             quiz.add_question(question_text, options, correct_option)
#         return quiz


# def main():
#     print("Welcome to the Quiz Application!")

#     user_type = input("Are you an admin or a student? ").lower()

#     if user_type == 'admin':
#         quiz = Administrator.create_quiz()
#         print("\nQuiz created successfully!\n")
#         quiz.display_questions()
#     elif user_type == 'student':
#         admin_quiz = Administrator.create_quiz()
#         user_quiz = Quiz()
#         user_quiz.questions = admin_quiz.questions  # Use the questions created by the administrator
#         user_quiz.take_quiz()
#     else:
#         print("Invalid user type. Please choose 'admin' or 'student'")


# if __name__ == "__main__":
#     main()

import json

class Quiz:
    def __init__(self):
        self.questions = []

    def add_question(self, question, options, correct_option):
        self.questions.append({'question': question, 'options': options, 'correct_option': correct_option})

    def display_questions(self):
        for i, data in enumerate(self.questions, 1):
            print(f"{i}. {data['question']}")
            for j, option in enumerate(data['options'], 1):
                print(f"   {j}. {option}")
            print()

    def take_quiz(self):
        score = 0
        for data in self.questions:
            print(data['question'])
            for i, option in enumerate(data['options'], 1):
                print(f"{i}. {option}")
            user_answer = int(input("Your answer (enter the number): "))
            if user_answer == data['correct_option']:
                print("Correct!\n")
                score += 1
            else:
                print(f"Wrong! The correct answer was {data['correct_option']}\n")
        print(f"You scored {score}/{len(self.questions)}")


class Administrator:
    @staticmethod
    def create_quiz():
        quiz = Quiz()
        num_questions = int(input("Enter the number of questions for the quiz: "))
        for _ in range(num_questions):
            question_text = input("Enter the question: ")
            options = input("Enter options separated by commas: ").split(',')
            correct_option = int(input("Enter the correct option number: "))
            quiz.add_question(question_text, options, correct_option)
        return quiz

    @staticmethod
    def save_quiz(quiz, filename='quiz_data.json'):
        with open(filename, 'w') as file:
            json.dump(quiz.questions, file)


def load_quiz(filename='quiz_data.json'):
    with open(filename, 'r') as file:
        questions = json.load(file)
    quiz = Quiz()
    quiz.questions = questions
    return quiz


def main():
    print("Welcome to the Quiz Application!")

    user_type = input("Are you an admin or a student? ").lower()

    if user_type == 'admin':
        quiz = Administrator.create_quiz()
        print("\nQuiz created successfully!\n")
        Administrator.save_quiz(quiz)
        quiz.display_questions()
    elif user_type == 'student':
        try:
            user_quiz = load_quiz()
            user_quiz.take_quiz()
        except FileNotFoundError:
            print("No quiz found. Please ask the admin to create a quiz first.")
    else:
        print("Invalid user type. Please choose 'admin' or 'student'")


if __name__ == "__main__":
    main()

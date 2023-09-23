# Python Quiz README

This Python quiz project is a simple console-based application that tests your knowledge with a set of True/False questions. It includes four main files: `main.py`, `data.py`, `quiz_brain.py`, and `question_model.py`.

## Project Structure

### main.py

`main.py` is the entry point of the application. It does the following:

- Imports the necessary modules: `Question`, `question_data`, and `QuizBrain`.
- Creates a list of questions from the `question_data`.
- Initiates a quiz using the `QuizBrain` class.
- Runs the quiz loop, asking questions until there are no more questions.
- Displays the final score.

### data.py

`data.py` contains the list of True/False questions in the `question_data` list. Each question is represented as a dictionary with two keys: "text" (the question itself) and "answer" (the correct answer, either "True" or "False").

### quiz_brain.py

`quiz_brain.py` defines the `QuizBrain` class, responsible for managing the quiz. It includes the following methods:

- `__init__(self, q_list)`: Initializes the quiz with a list of questions.
- `still_has_questions(self)`: Checks if there are more questions to be asked.
- `next_question(self)`: Presents the next question to the user and checks the answer.
- `check_answer(self, user_answer, correct_answer)`: Compares the user's answer to the correct answer and updates the score.

### question_model.py

`question_model.py` defines the `Question` class, which represents an individual question. Each `Question` object has two attributes: `text` (the question text) and `answer` (the correct answer).

## Usage

To run the quiz, execute `main.py`. The quiz will interactively ask you each question, and you can respond with either "True" or "False." After completing all the questions, the quiz will display your final score.

## Example Questions

The provided `question_data` list includes a variety of True/False questions for testing purposes. You can modify this list to add your own questions.

## Dependencies

This project does not require any external libraries or dependencies beyond Python 3.

## Contributions

Contributions to this project are welcome! Feel free to improve the code, add new features, or report any issues you encounter.

Happy quizzing!

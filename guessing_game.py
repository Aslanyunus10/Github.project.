def success():
def success():
    print("EXCELLENT! Your knowledge is at a very high level.")

def failure():
    print("BE CAREFUL!!!  Your answer is wrong")

Open_questions_with_answer = [
    {
        "question": "What is the capital city of England?",
        "answer": "London",
        "points": 20,
    },
    {
        "question": "Whhich is the fastest animal in the world?",
        "answer": "cheetah",
        "points": 10,
    },
    {
        "question": "What is the result of 9999*0?",
        "answer": 0,
        "points": 10,
    },
    {
        "question": "which is the slowest animal in the world?",
        "answer":"turtle",
        "points": 10,
    },
    {
        "question": "How many weeks in each year?",
        "answer": 52,
        "points": 10,
    },
    {
        "question": "What is the name of the who assasinated former US President John Kennedy?",
        "answer": "Lee Harwey Oswald",
        "points": 100,
    }
                             ]


def play_quiz(questions):
    points = 0
    for question_data in questions:
        user_answer = input(f"{question_data['question']} ")
        if user_answer.lower() == question_data['answer'].lower():
            points += question_data['points']
    print(f"Your total score is {points}")


play_quiz = [
    {
        "questions": "According to 2023 data, what is the population in the USA?\n",
        "options": "A) 331,000,000\n"
                   "B) 321,000,000\n"
                   "C) 341,000,000\n"
                   "D) 311,000,000\n",
        "answer":  "A",
        "points": 30
    },
    {
        "questions": "Which is the 5th country that managed to land a vehicle on the moon recently?\n",
        "options": "A)Germany\n" 
                   "B)Japan\n"
                   "C)South Korea\n"
                   "D)France\n",
        "answer":  "B",
        "points": 50
    },
    {
        "questions":"According to December 2023 data, which country's passport is the most powerful in the world, which can enter 160 countries, leaving Singapore behind?\n",
        "options": "A)Japan\n"
                   "B)England\n"
                   "C)USA\n" 
                   "D)Spain\n",
        "answer":  "D",
        "points": 100
    },
    {
        "questions":"How many Ballon d'Or awards does Lionel Messi,who broke his own record by winning the 8th Ballon d'Or award last year,have than his closest rival,Cristiano Ronaldo?\n",
        "options": "A)3\n"
                   "B)4\n"
                   "C)2\n"
                   "D)1\n",
        "answer":  "A",
        "points": 60

    }
                 ]
total_points = 0

for question in play_quiz:
    print(question["questions"])
    print(question["options"])

    user_answer = input("Your answer (A/B/C/D): ").upper()

    if user_answer == question["answer"]:
        total_points += question["points"]

print("Total score is -->",total_points)

if total_points >= 80:
    print("Congratulations!, you did it:))))")
else:
    print("Sorry, your knowledge is not enough, please try again...")

print("Total point is -->", total_points)




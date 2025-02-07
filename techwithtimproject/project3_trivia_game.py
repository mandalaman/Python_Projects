#list of questions
#store the answers
#randomly pick quetions
#ask the quetions
#see if they are correct
#keep track of the score
#tell the user their score

import random

questions = {
    "What is the main temple of Shaktifarm no 4?": "Durga Mandir",
    "Where is the place of Subhash Chandra Bose statue?": "Market",
    "Who won the recently held Nagar Panchayat elections(Municipal council) from Shakti Farm?": "Sumit Mandal",
    "How many wards are there in the Shakti Farm Nagar Panchayat?": "7",
    "Where is your Tehsil Name?": "Sitarganj",
    "In which year did corona happen?": "2020",
    "What is the output of 5 * 7 is equal to?": "35",
    "What is your husband date of birth?": "2005",
    "What is your husband favourite dish?": "mutton or chicken",
    "What is your husband first girlfriend?": "krystal",
    "What is your husband favourite palce?": "Japan",
    "What is your husband current girlfriend?": "preti",

}

def python_trivia_game():
    questions_list = list(questions.keys())
    total_questions = 12
    score = 0

    selected_questions = random.sample(questions_list, total_questions)

    for idx, question in enumerate(selected_questions):
        print(f"{idx + 1}. {question}")
        user_answer = input("Your answer: ").lower().strip()

        correct_answer = questions[question]

        if user_answer == correct_answer.lower():
            print("Correct!\n")
            score += 1
        else:
            print(f"Wrong. The correct answer is:. \n")
    
    print(f"Game Over! your final score is: {score}/{total_questions}")


python_trivia_game()
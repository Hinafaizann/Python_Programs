from PromptandanswerForMCQS import ClassQuestion

question_prompt = [ #3 prompts
    "What is the color of apple? \n a)red \n b)blue \n c) purple \n",
    "What is the color of banana? \n a)red \n b)yellow \n c) purple \n",
    "What is the color of orange? \n a)red \n b)blue \n c)orange \n"
]
#array of question that we wanna ask on our test:
questions = [ #WE ARE CREATING THREE questions each one is getting different prompts and getting different answers
    ClassQuestion(question_prompt[0], "a"),
    ClassQuestion(question_prompt[1], "b"),
    ClassQuestion(question_prompt[2], "c")
]
#function that will ask questions to user

def run_test(questions): #questions is the array of question, we have passed array name as parameter
    score = 0
    for question in questions: #for each element(question) in array of questions i wanna do something
        answer =input(question.prompt) #storing of answer the user will enter
        if answer == question.answer: #answer is referreing to student answer
            score +=1
    print("you got " +str(score) + "/" +str(len(questions)) + " correct")


run_test(questions)
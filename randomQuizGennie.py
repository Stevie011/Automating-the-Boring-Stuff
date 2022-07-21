#! python3

#--------QUIZ-O-TRON--------------
#creates american capital quiz based on state capital names
#random order, along with answer key

import random

#quiz data- keys: state names, values: capitals

quizData = {'Alabama': 'Montgomery', 'Alaska': 'Juneau', 'Arizona': 'Phoenix',
   'Arkansas': 'Little Rock', 'California': 'Sacramento', 'Colorado': 'Denver',
   'Connecticut': 'Hartford', 'Delaware': 'Dover', 'Florida': 'Tallahassee',
   'Georgia': 'Atlanta', 'Hawaii': 'Honolulu', 'Idaho': 'Boise', 'Illinois':
   'Springfield', 'Indiana': 'Indianapolis', 'Iowa': 'Des Moines', 'Kansas':
   'Topeka', 'Kentucky': 'Frankfort', 'Louisiana': 'Baton Rouge', 'Maine':
   'Augusta', 'Maryland': 'Annapolis', 'Massachusetts': 'Boston', 'Michigan':
   'Lansing', 'Minnesota': 'Saint Paul', 'Mississippi': 'Jackson', 'Missouri':
   'Jefferson City', 'Montana': 'Helena', 'Nebraska': 'Lincoln', 'Nevada':
   'Carson City', 'New Hampshire': 'Concord', 'New Jersey': 'Trenton', 'New Mexico': 
   'Santa Fe', 'New York': 'Albany',
   'North Carolina': 'Raleigh', 'North Dakota': 'Bismarck', 'Ohio': 'Columbus', 'Oklahoma': 'Oklahoma City',
   'Oregon': 'Salem', 'Pennsylvania': 'Harrisburg', 'Rhode Island': 'Providence',
   'South Carolina': 'Columbia', 'South Dakota': 'Pierre', 'Tennessee':
   'Nashville', 'Texas': 'Austin', 'Utah': 'Salt Lake City', 'Vermont':
   'Montpelier', 'Virginia': 'Richmond', 'Washington': 'Olympia', 'West Virginia': 'Charleston', 
   'Wisconsin': 'Madison', 'Wyoming': 'Cheyenne'}

#gen 35 quiz files

for quizNum in range(35):
    #create quiz and answer key files
    quizFile = open(f"state_quiz{quizNum+1}.txt","w")
    answerKey = open(f"state_quiz_answers{quizNum+1}.txt", "w")

    #write header for quiz
    quizFile.write("Name :\n\nDate :\n\nPeriod :\n\n")
    quizFile.write((" "*20)+ f"USA state capital quiz (Form{quizNum+1})")
    quizFile.write("\n\n")

    #shuffle order of states

    stateNames = list(quizData.keys())
    random.shuffle(stateNames)

    #loop thru 50 states, making q for each

    for questionNum in range(50):
        #get the right ans by referencing the number
        rightAns = quizData[stateNames[questionNum]]
        #poss wrong answers are all the other values
        wrongAns = list(quizData.values())
        #take out the right answer
        del wrongAns[wrongAns.index(rightAns)]
        #choose 3 at random
        wrongAns = random.sample(wrongAns, 3)
        #answer options are these 3 plus the correct one
        ansOptions = wrongAns + [rightAns]
        random.shuffle(ansOptions)

        #write q and q options to file
        quizFile.write(f"{questionNum+1}. What is the capital of {stateNames[questionNum]}?\n")
        for i in range(4):
            quizFile.write(f"     {'ABCD'[i]}. {ansOptions[i]}\n")
        quizFile.write("\n")

        #write answer key to file
        answerKey.write(f"{questionNum+1}.{'ABCD'[ansOptions.index(rightAns)]}")
    quizFile.close()
    answerKey.close()

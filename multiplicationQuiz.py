#! python3

#--------silly multipication quiz

import pyinputplus as pyip
import random, time

numQuestions = 10
rightAnswers = 10

for questionNum in range(numQuestions):
    num1 = random.randint(0,9)
    num2 = random.randint(0,9)
    prompt = "question number %s --- %s x %s = " % (questionNum, num1, num2)
    #prompt = "question number " + str(questionNum) +"---"+str(num1)+ " x " + str(num2) + "="


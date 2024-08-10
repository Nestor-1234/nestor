from memo_card_layout import *
from memo_data1 import Question
from random import *

qst1 = Question("Дім","hous", "cat", "dog", "apple")
qst2 = Question("Кіт","cat", "hous", "dog", "apple")
qst3 = Question("Пес","dog", "cat", "hous", "apple")



list = [qst1, qst2, qst3]

def randomQuestion():
    global list
    question = choice(list)
    radio_list = [rbtn_1,rbtn_2,rbtn_3,rbtn_4]
    shuffle(radio_list)
    answerRB = radio_list[0]
    wrogen1 = radio_list[1]
    wrogen2 = radio_list[2]
    wrogen3 = radio_list[3]
    lb_Question.setText(question.question)
    answerRB.setText(question.answer)
    wrogen1.setText(question.wrong_answer1)
    wrogen2.setText(question.wrong_answer2)
    wrogen3.setText(question.wrong_answer3)

    rbtn_1.setText(question.answer)

def clickOk():
    show_result()




randomQuestion()

btn_OK.clicked.connect(clickOk)

app.exec_()
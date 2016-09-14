# -*- coding: utf-8 -*-

import csv
import sys
from PySide import QtGui
from random import shuffle

FILENAME = 'questions.csv'

class Question:
    def __init__(self,question,answer,question_type):
        self.question = question.decode('utf-8')
        self.answer = answer
        self.question_type =  question_type
    
    def check_answer(self,answer):
        return self.answer == answer.lower()

    def __str__(self):
        return 'Question:{}\nAnswer:{}'.format(self.question,self.answer)

def load_questions_from_csv(filename,questions):
    csv_file = open(filename,'r')
    reader = csv.reader(csv_file,delimiter=',')
    next(reader,None)
    for row in reader:
        questions.append(Question(row[0],row[1],row[2]))
    csv_file.close()

def show_question_dialog(gui,question_number,question):
    return QtGui.QInputDialog.getText(gui,'Question '.format(question_number),
            question.question)

def show_message_box(message,title='Message'):
    msgBox = QtGui.QMessageBox()
    msgBox.setText(message)
    msgBox.setWindowTitle(title)
    msgBox.exec_()

def main():
    app = QtGui.QApplication(sys.argv)
    gui = QtGui.QWidget()

    show_message_box(u'はじめまして私わ日本語テストです')
    
    n_questions,ok = QtGui.QInputDialog.getInt(gui,'Number of Questions',
            'Input number of questions:')
    questions = []

    load_questions_from_csv(FILENAME,questions)

    correct_answers = 0

    shuffle(questions)

    for i in range(0, n_questions):
        answer,ok = show_question_dialog(gui,i,questions[i])

        if ok:
            if questions[i].check_answer(answer):
                show_message_box('Correct!')
                correct_answers += 1
            else:
                show_message_box('Wrong! Right answer is: {}'.format(questions[i].answer))
        else:
            app.exit()
            

    show_message_box("You got: {} out of {}".format(correct_answers,n_questions))
    app.exit()
    

if __name__ == '__main__':
    main()

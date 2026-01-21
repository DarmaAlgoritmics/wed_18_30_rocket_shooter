from random import shuffle # type: ignore
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
        QApplication, QWidget, QButtonGroup,
        QHBoxLayout, QVBoxLayout, 
        QGroupBox, QRadioButton,  
        QPushButton, QLabel)
from random import randint


class Question():
    ''' contains the question, one correct answer and three incorrect answers'''
    def __init__(self, question, right_answer, wrong1, wrong2, wrong3):
        # all the lines must be given when creating the object, and will be recorded as properties
        self.question = question
        self.right_answer = right_answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3

app = QApplication([])

# Create question panel
btn_OK = QPushButton('Answer')
lb_Question = QLabel('The most difficult question in the world!')
RadioGroupBox = QGroupBox("Answer options")

rbtn_1 = QRadioButton('Option 1')
rbtn_2 = QRadioButton('Option 2')
rbtn_3 = QRadioButton('Option 3')
rbtn_4 = QRadioButton('Option 4')

RadioGroup = QButtonGroup() 
RadioGroup.addButton(rbtn_1)
RadioGroup.addButton(rbtn_2)
RadioGroup.addButton(rbtn_3)
RadioGroup.addButton(rbtn_4)

# Create a results panel
AnsGroupBox = QGroupBox("Test result")
lb_Result = QLabel('Are you correct or not?') # “Correct” or “Incorrect” text will be here
lb_Correct = QLabel('the answer will be here!') # correct answer text will be written here 

# Place all the widgets in the window:
layout_line1 = QHBoxLayout() # question
layout_line2 = QHBoxLayout() # answer options or test result
layout_line3 = QHBoxLayout() # “Answer” button
layout_ans1 = QHBoxLayout()   
layout_ans2 = QVBoxLayout()
layout_ans3 = QVBoxLayout()
layout_card = QVBoxLayout()
layout_res = QVBoxLayout()

layout_res.addWidget(lb_Result, alignment=(Qt.AlignLeft | Qt.AlignTop))
layout_res.addWidget(lb_Correct, alignment=Qt.AlignHCenter, stretch=2)
AnsGroupBox.setLayout(layout_res)

layout_ans2.addWidget(rbtn_1) # two answers in the first column
layout_ans2.addWidget(rbtn_2)
layout_ans3.addWidget(rbtn_3) # two answers in the second column
layout_ans3.addWidget(rbtn_4)

layout_ans1.addLayout(layout_ans2)
layout_ans1.addLayout(layout_ans3)
RadioGroupBox.setLayout(layout_ans1) 

layout_line1.addWidget(lb_Question, alignment=(Qt.AlignHCenter | Qt.AlignVCenter))
# Put both panels in the same line; one of them will be hidden and the other will be shown:
layout_line2.addWidget(RadioGroupBox)   
layout_line2.addWidget(AnsGroupBox)

layout_line3.addStretch(1)
layout_line3.addWidget(btn_OK, stretch=2) # the button should be large
layout_line3.addStretch(1)

# Now let’s put the lines we’ve created one under one another:
layout_card.addLayout(layout_line1, stretch=2)
layout_card.addLayout(layout_line2, stretch=8)
layout_card.addStretch(1)
layout_card.addLayout(layout_line3, stretch=1)
layout_card.addStretch(1)
layout_card.setSpacing(5) # spaces between content
AnsGroupBox.hide()  
RadioGroupBox.show() 

def show_result():
    ''' show answer panel '''
    RadioGroupBox.hide()
    AnsGroupBox.show()
    btn_OK.setText('Next question')

def show_question():
    ''' show question panel '''
    RadioGroupBox.show()
    AnsGroupBox.hide()
    btn_OK.setText('Answer')
    RadioGroup.setExclusive(False) # remove limits in order to reset radio button selection
    rbtn_1.setChecked(False)
    rbtn_2.setChecked(False)
    rbtn_3.setChecked(False)
    rbtn_4.setChecked(False)
    RadioGroup.setExclusive(True) # bring back the limits so only one radio button can be selected 



answers = [rbtn_1, rbtn_2, rbtn_3, rbtn_4]
def ask(q:Question):
    ''' the function writes the value of the question and answers into the corresponding widgets 
    while distributing the answer options randomly'''
    shuffle(answers)
    answers[0].setText(q.right_answer)
    answers[1].setText(q.wrong1)
    answers[2].setText(q.wrong2)
    answers[3].setText(q.wrong3)
    lb_Question.setText(q.question)
    lb_Correct.setText(q.right_answer) 
    show_question() 

def show_correct(res):
    ''' show result - put the written text into "result" and show the corresponding panel '''
    lb_Result.setText(res)
    show_result()

def check_answer():
    ''' if an answer option was selected, check and show answer panel '''
    if answers[0].isChecked():
        
        window.score +=1
        print('Statistics\n-Total questions: ', window.total, '\n-Right answers: ', window.score)
        print('Rating:', str((window.score/window.total)*100) +'%')
        show_correct('Benar!')
    else:
        if answers[1].isChecked() or answers[2].isChecked() or answers[3].isChecked():
            show_correct('Salah!')            
            print('Rating:', str((window.score/window.total)*100) +'%')



def click_ok():
    ''' a temporary function that makes it possible to press a button to call up alternating
    show_result() or show_question() '''
    if btn_OK.text() == 'Answer':
        check_answer()
    else:
        next_question()   
def next_question():
    #window.cur_question = window.cur_question + 1 # move on to the next question 

    window.total += 1 
    print('Statistics\n-Total questions: ', window.total, '\n-Right answers: ', window.score)
    cur_question = randint(0,len(questions_list)-1)

    #if window.cur_question >= len(questions_list):
    #   window.cur_question = 0 # if the list of questions has ended, start over 
    q = questions_list[cur_question] # take a question
    ask(q) # ask it


questions_list = [] 
questions_list.append(Question('Coba ditambahkan 1+1','2','3','4','5'))
questions_list.append(Question('Coba ditambahkan 2+3','5','3','4','2'))
questions_list.append(Question('Coba ditambahkan 2+2','4','3','2','5'))


window = QWidget()
btn_OK.clicked.connect(click_ok)
#window.cur_question = -1

window.score = 0
window.total = 0

next_question()

window.setLayout(layout_card)
window.setWindowTitle('Memory Card')
#menambahkan panjang layar
window.setFixedWidth(300)
window.show()

app.exec()

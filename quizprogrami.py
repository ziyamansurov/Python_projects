class Question:
    def __init__(self,text,choices,answer):
        self.text=text
        self.choices=choices
        self.answer=answer

    def cavab(self,cavab):
        return self.answer==cavab

class Quiz:

    def __init__(self,questions):
        self.questions=questions
        self.score=0
        self.questionIndex=0
    def sualgosderen(self):
       return self.questions[self.questionIndex]
    def ekrandagosderen(self):

            question = self.sualgosderen()
            print(f'Sual {self.questionIndex + 1}: {question.text}')

            for q in question.choices:
                print('-' + q)

            answer = input('Cavab: ')
            self.sualyoxluyan(answer)
            self.sualhazirliyan()

            # print(question.cavab(answer))
    def sualyoxluyan(self,answer):
        question=self.sualgosderen()

        if question.cavab(answer):
            self.score+=1
        self.questionIndex+=1


    def sualhazirliyan(self):
        if len(self.questions)==self.questionIndex:
            self.xalgosderen()

        else:
            self.siragosderen()
            self.ekrandagosderen()

    def xalgosderen(self):
        self.score+=1
        print('Quiz bitti ')
        print(f'{len(questions)} sualdan {self.score-1} dogru cavab')

    def siragosderen(self):
        totalQuestions=len(self.questions)
        questionNumber=self.questionIndex+1

        if questionNumber>totalQuestions:
            pass

        else:
            print(f'{totalQuestions}/{questionNumber}'.center(100,'*'))









q1=Question("ml ai ucun isdifade edlen en yaxsi programlama dili",['javascript','python','c++','c#','c','java'],'python')
q2=Question("en tez programlama dili",['javascript','python','c++','c#','c','java'],'c++')
q3=Question("en gelirli programlama dili",['javascript','python','c++','c#','c','java'],'python')
q4=Question("en sevilen programlama dili",['scala','python','c++','c#','c','java'],'python')
q5=Question("en sade programlama dili",['c#','python','c++','ruby','c','java'],'python')


questions=[q1,q2,q3,q4,q5]
quiz=Quiz(questions)

quiz.sualhazirliyan()
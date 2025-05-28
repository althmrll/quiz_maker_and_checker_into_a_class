class Quiz:
    def __init__(self, file_path, line):
        self.format_question_and_options=[]
        self.question_with_choice=[]
        self.file=file_path
        self.answer=[]
        self.find_word="Correct Answer:"
        self.questions_asked=[]
        self.asked_question=0
        self.question_counter=0
        self.score=0
        self.line=line

    def main_mechanics(self):
        while True:
            self.question_with_choice_formatting()
            self.ask_question_and_answer()


    def question_with_choice_formatting(self):
        for indiv_lines in self.line:
            if indiv_lines!="\n":
                if indiv_lines.startswith(self.find_word):
                    formatted_answer=str(indiv_lines)
                    formatted_answer=formatted_answer.replace(self.find_word,"").replace("\n","").upper().strip()
                    self.answer.append(formatted_answer)
                else:
                    self.format_question_and_options.append(indiv_lines)

            elif indiv_lines=="\n" or indiv_lines=="":
                formatted_question_and_option="".join(self.format_question_and_options)
                self.question_with_choice.append(formatted_question_and_option)
                self.format_question_and_options.clear()

        formatted_question_and_option="".join(self.format_question_and_options)
        self.question_with_choice.append(formatted_question_and_option)

    def ask_question_and_answer(self):    
        import random
        while self.asked_question!=len(self.answer):
            random_index=random.randint(0,len(self.answer)-1)
            fraction=self.asked_question/len(self.answer)
            percentage=fraction*100
            while True:
                if self.asked_question==len(self.answer):
                    passing=len(self.answer)/2
                    if self.score>=passing:
                        print(f"\n\nYou have finished the quiz and answered {self.score} questions out of {len(self.answer)}. Congrats!\n\n----------\n")
                        break
            
                    else:
                        print(f"\n\nYou have finished the quiz and answered {self.score} questions out of {len(self.answer)}. Better luck next time!\n\n----------\n")
                        break

                else:
                    if self.question_with_choice[random_index] in self.questions_asked:
                        break

                    else:
                        print(f"\n----------\n\n{self.question_counter} questions asked out of {len(self.answer)} ({percentage} % done)")
                        print(f"Score:{self.score}\n")
                        print(self.question_with_choice[random_index])
                        self.questions_asked.append(self.question_with_choice[random_index])
                        user_answer=input("Your answer:")
                        user_answer=user_answer.upper().strip()

                        if user_answer==self.answer[random_index]:
                            print("\nCorrect!!")
                            self.score=self.score+1
                            self.question_counter=self.question_counter+1
                            self.asked_question=self.asked_question+1
                            break
                        else:
                            print("\nWrong, the correct answer is", self.answer[random_index])
                            self.asked_question=self.asked_question+1
                            self.question_counter=self.question_counter+1
                            break
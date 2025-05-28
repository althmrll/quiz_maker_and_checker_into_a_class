import tkinter as tk_module
from tkinter import filedialog
import random

#LIST
question_with_choice=[]
answer=[]

#DEFINITIONS
def choose_file():
    question_with_choice.clear()
    answer.clear()
    global chosen_file
    chosen_file = filedialog.askopenfilename()
    if chosen_file:
        main_quiz()

def question_with_choice_formatting():
    find_word="Correct Answer:"
    format_question_and_options=[]
    lines = file.readlines()

    for indiv_lines in lines:
        if indiv_lines!="\n":
            if indiv_lines.startswith(find_word):
                formatted_answer=str(indiv_lines)
                formatted_answer=formatted_answer.replace(find_word,"").replace("\n","").upper().strip()
                answer.append(formatted_answer)
            else:
                format_question_and_options.append(indiv_lines)

        elif indiv_lines=="\n" or indiv_lines=="":
            formatted_question_and_option="".join(format_question_and_options)
            question_with_choice.append(formatted_question_and_option)
            format_question_and_options.clear()
    formatted_question_and_option="".join(format_question_and_options)
    question_with_choice.append(formatted_question_and_option)

def ask_question_and_answer():
    global score
    global questions_asked
    asked_question=0
    question_counter=0
    score=0
    questions_asked=[]
    while asked_question!=len(answer):
        random_index=random.randint(0,len(answer)-1)
        fraction=asked_question/len(answer)
        percentage=fraction*100
        while True:
            if asked_question==len(answer):
                finish()
            else:
                if question_with_choice[random_index] in questions_asked:
                    break
                else:
                    print(f"\n----------\n\n{question_counter} questions asked out of {len(answer)} ({percentage} % done)")
                    print(f"Score:{score}\n")
                    print(question_with_choice[random_index])
                    questions_asked.append(question_with_choice[random_index])
                    user_answer=input("Your answer:")
                    user_answer=user_answer.upper().strip()

                    if user_answer==answer[random_index]:
                        print("\nCorrect!!")
                        asked_question=asked_question+1
                        question_counter=question_counter+1
                        score=score+1 #Add 1 to number of corrects (if correct) and the number of questions answered over the total number of questions.
                        break
                    else:
                        print("\nWrong, the correct answer is", answer[random_index])
                        asked_question=asked_question+1
                        question_counter=question_counter+1
                        break

def finish():#Flash ending message, positive if passed, negative if failed.
    passing=len(answer)/2
    if score>=passing:
        print(f"\n\nYou have finished the quiz and answered {score} questions out of {len(answer)}. Congrats!\n\n----------\n")
        replay()
    else:
        print(f"\n\nYou have finished the quiz and answered {score} questions out of {len(answer)}. Better luck next time!\n\n----------\n")
        replay()

def replay():#Add choice wether to exit the program or answer another quiz.

    global replay_choice
    replay_choice=""
    while True:
        replay=input("Do you want to answer another quiz?(Y/N)")
        if replay=="Y" or replay=="y":
            choose_file()
        elif replay=="N" or replay=="n":
            print("Goodbye!")
            choose_file_window.destroy()
            exit()
        else:
            print("Invalid Output, Reasking Question...")
        
def main_quiz():
    global file
    choose_file_window.withdraw()
    file=open(chosen_file,"r")
    question_with_choice_formatting()
    ask_question_and_answer()
    finish()

#QUIZ CHECKER (main program)
choose_file_window = tk_module.Tk()
choose_file_window.title("QUIZ CHECKER")
choose_file_window.geometry("1000x100") 
opening_message = tk_module.Label(choose_file_window, text="QUIZ CHECKER\nThis program is used so you can answer the quiz you " \
"just created uisng basic quiz creator. You can also use this so other people can answer your created quiz.\n Note that" \
"this will not work if you use other quizzes, not created using basic quiz maker. Otherwise, click the button below to" \
"choose which quiz you want to answer.") #Ask user the quiz they want to answer.
opening_message.pack()

choose_quiz_button = tk_module.Button(choose_file_window, text="Choose Quiz", command=choose_file)
choose_quiz_button.pack()

choose_file_window.mainloop()
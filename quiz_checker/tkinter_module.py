import tkinter as tk_module
from tkinter import filedialog
from quiz_mechanics import Quiz
from replay_mechanics import Replay

class MainWindow:
    def __init__(self):
        self.choose_file_window=None

    def starting_window(self):
        self.choose_file_window = tk_module.Tk()
        self.choose_file_window.title("QUIZ CHECKER")
        self.choose_file_window.geometry("1000x100") 
        opening_message = tk_module.Label(self.choose_file_window, text="QUIZ CHECKER\nThis program is used so you can answer the quiz you " \
        "just created uisng basic quiz creator. You can also use this so other people can answer your created quiz.\n Note that" \
        "this will not work if you use other quizzes, not created using basic quiz maker. Otherwise, click the button below to" \
        "choose which quiz you want to answer.") #Ask user the quiz they want to answer.
        opening_message.pack()

        choose_quiz_button = tk_module.Button(self.choose_file_window, text="Choose Quiz", command=self.choose_file)
        choose_quiz_button.pack()

        self.choose_file_window.mainloop()
    
    def choose_file(self):
        chosen_file = filedialog.askopenfilename()
        if chosen_file:
            with open(chosen_file, 'r') as file:
                line = file.readlines() 
            self.choose_file_window.withdraw()
            chosen_quiz=Quiz(chosen_file, line)
            chosen_quiz.main_mechanics()
            replay_game= Replay()
            replay_game.replay_process()
            self.choose_file_window.deiconify()
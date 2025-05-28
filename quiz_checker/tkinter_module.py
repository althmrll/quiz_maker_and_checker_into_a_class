import tkinter as tk_module
from tkinter import filedialog
from quiz_mechanics import quiz
from results import results_mechanics
from replay_mechanics import replay

class main_window:
    def __init__(self, choose_file_window):
        self.choose_file_window=choose_file_window

    def main_window(self, choose_file_window):
        self.choose_file_window = tk_module.Tk()
        self.choose_file_window.title("QUIZ CHECKER")
        self.choose_file_window.geometry("1000x100") 
        opening_message = tk_module.Label(choose_file_window, text="QUIZ CHECKER\nThis program is used so you can answer the quiz you " \
        "just created uisng basic quiz creator. You can also use this so other people can answer your created quiz.\n Note that" \
        "this will not work if you use other quizzes, not created using basic quiz maker. Otherwise, click the button below to" \
        "choose which quiz you want to answer.") #Ask user the quiz they want to answer.
        opening_message.pack()

        choose_quiz_button = tk_module.Button(choose_file_window, text="Choose Quiz", command=self.choose_file)
        choose_quiz_button.pack()

        self.choose_file_window.mainloop()
    
    def choose_file(self, choose_file_window):
        chosen_file = filedialog.askopenfilename()
        if chosen_file:
            self.choose_file_window.withdraw()
            chosen_quiz=quiz(chosen_file)
            chosen_quiz.main_mechanics()
            results=results_mechanics()
            results.finish()
            replay_game= replay()
            replay_game.replay_mechanics()

if __name__=="__main__":
    start_quiz_checker=main_window()
    start_quiz_checker.main_window()
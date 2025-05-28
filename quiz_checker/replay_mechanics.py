import tkinter_module
from tkinter_module import main_window

class replay(tkinter_module):
    def __init__(self, replay_choice):
        super().__init__()
        self.choose_file_window=main_window.choose_file_window()
        self.choose_file=main_window.choose_file()
        self.replay_choice=replay_choice

    def replay_mechanics(self):
        while True:
            replay=self.replay_choice(input("Do you want to answer another quiz?(Y/N)"))
            if replay.lower()=="y":
                self.choose_file()
            elif replay.lower()=="n":
                print("Goodbye!")
                self.choose_file_window.destroy()
                exit()
            else:
                print("Invalid Output, Reasking Question...")
                return False
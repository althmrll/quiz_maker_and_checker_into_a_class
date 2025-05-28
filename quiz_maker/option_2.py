from option_1 import option_one

class option_two(option_one):
    def __init__(self):
        super().__init__()
    
    def create_new_quiz(self):
        file = open("Untitled Quiz.txt", "w")
        file.write("(IMPORTANT NOTE: Please change the filename of this quiz after checking as it may be deleted when creating"
                   " a new one. Delete this notice after. Thank you!)\n\n")

    def __init__(self, filename):
        self.filename = filename + '.txt'
        self.options = []
        self.question_with_choice = ""

    def open_filename(self):
        file = open(self.filename, "a")
        file.write("\n(This is the start of your editing using quiz maker. Delete this after checking. Thank you!)\n\n")

        while True:
            self.ask_question(file)
            answer = input("Input correct answer: ")
            file.write("Correct Answer: " + answer + "\n")



            if not self._ask_to_continue(file):
                file.close()
                import os
                os.startfile(self.filename)
                break

    def input_question_with_choice(self):
        self.options.clear()
        self.question_with_choice = ""
        question = input("Question: ")
        self.question_with_choice += question + "\n"

    def input_options(self):
        while option_count!=4:#So user will be asked for 4 options
            option = input("Add option:")#Ask user for option
            self.options.append(option)#Adds user's input into 'options' list
            option_count = option_count + 1 #Adds one count to inputted options to keep tract how any are added.

    def format_options(self, file):
        for options_item_index, option in enumerate(self.options):
            question_with_choice += f"{chr(ord('a')+options_item_index)}. {option} \n"
        file.write(question_with_choice)

        for i, option in enumerate(self.options):
            self.question_with_choice += f"{chr(ord('a') + i)}. {option}\n"

        file.write(self.question_with_choice)

    def add_more(self, file):
        while True:
            ask = input("\nAdd another question? (Y/N): ")
            if ask.lower() == "y":
                file.write("\n")
                print("\n----------\n")
                return True
            elif ask.lower() == "n":
                print("\nThank you for using quiz editor. Your file will now open.\n")
                return False
            else:
                print(".\n.\n.\nYou can only answer Y or N\n----------\n")
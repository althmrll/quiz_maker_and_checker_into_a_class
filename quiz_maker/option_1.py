class option_one:
    def __init__(self):
        self.options = []
        self.question_with_choice=""
        self.option_count = 0
    
    def create_new_quiz(self):
        file = open("Untitled Quiz.txt", "w")
        file.write("(IMPORTANT NOTE: Please change the filename of this quiz after checking as it may be deleted when creating"
                   " a new one. Delete this notice after. Thank you!)\n\n")
        
        while True:
            self.input_question(file)
            self.input_and_format_options(file)
            answer = input("Input correct answer: ")
            file.write("Correct Answer: " + answer + "\n")
            self.add_more(file)

            if not self.add_more(file):
                file.close()
                import os
                os.startfile("Untitled Quiz.txt")
                break

    def input_question(self):
        while True:
            question=input("Question:") #Asks user for input
            self.question_with_choice+=question+"\n"#Adds new line so choices will be written below the question"
            self.options.clear() #clears items in options list, so the number from preceding numbers re not printed
                            #again in the following numbers.

    def input_and_format_options(self, file):
        while option_count!=4:#So user will be asked for 4 options
            option = input("Add option:")#Ask user for option
            self.options.append(option)#Adds user's input into 'options' list
            option_count = option_count + 1 #Adds one count to inputted options to keep tract how any are added.

        for options_item_index, option in enumerate(self.options):
            question_with_choice += f"{chr(ord('a')+options_item_index)}. {option} \n"
        file.write(question_with_choice)

    def add_more(self, file):
        while True:
            ask = input("\nAdd another question?(Y/N)")
            if ask == "Y" or ask == "y":
                new_line="\n"
                print("\n----------\n")
                file.write(new_line)
                self.question_with_choice=""
                self.options.clear
                self.option_count=0
                return True

            elif ask == "N" or ask == "n":
                print("\nThank you for using basic quiz maker. Be sure to rename your file or else it will"
                        "be replaced if you make a new quiz.FOr now, a notepad file will open which contians all the"
                      "questions that you have inputted. Thank you!\n")
                return False

            else:
                print(".\n.\n.\nyou can only answer Y or N\n----------\n")
                continue
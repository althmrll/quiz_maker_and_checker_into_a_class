class option_one:
    def __init__(self, file):
        self.options = []
        self.question_with_choice=""
        self.option_count=0
        self.file = file

    def option_mechanics(self, file):
        file=open("Untitled Quiz.txt", "w")
        file.write("(IMPORTANT NOTE: Please change the filename of this quiz after checking as it may be deleted when creating"
                " a new one. Delete this notice after. Thank you!)\n\n")
        
        while True:
            option_one.input_question()
            option_one.input_and_format_options
            answer=input("Input correct answer:")
            file.write("Correct Answer: "+answer+"\n")

            if not option_one.add_more(self, file):
                import os
                file.close()
                os.startfile('Untitled Quiz.txt')
                break

    def input_question(self, options):
        while True:
            question=input("Question:") #Asks user for input
            question_with_choice+=question+"\n"#Adds new line so choices will be written below the question"
            options.clear() #clears items in options list, so the number from preceding numbers re not printed
                            #again in the following numbers.

    def input_and_format_options(self, options, file):
        while option_count!=4:#So user will be asked for 4 options
            option = input("Add option:")#Ask user for option
            options.append(option)#Adds user's input into 'options' list
            option_count = option_count + 1 #Adds one count to inputted options to keep tract how any are added.

        for options_item_index, option in enumerate(options):
            question_with_choice += f"{chr(ord('a')+options_item_index)}. {option} \n"
            file.write(question_with_choice)
    
    def add_more(self, file):
        while True:
            ask = input("\nAdd another question?(Y/N)")
            if ask == "Y" or ask == "y":
                new_line="\n"
                print("\n----------\n")
                file.write(new_line)
                question_with_choice=""
                break

            elif ask == "N" or ask == "n":
                print("\nThank you for using basic quiz maker. Be sure to rename your file or else it will"
                        "be replaced if you make a new quiz.FOr now, a notepad file will open which contians all the"
                      "questions that you have inputted. Thank you!\n")
                return False

            else:
                print(".\n.\n.\nyou can only answer Y or N\n----------\n")
                continue
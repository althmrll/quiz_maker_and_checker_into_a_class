class option_2:
    def __init__(self, filename):
        self.options = []
        self.question_with_choice=""
        self.option_count=0
        self.filename = filename

    def option_mechanics(self):
        file = open(self.filename, "a")
        space="\n"
        file.write(space)
        file.write("(This is the start of your editing using quiz maker. Delete this after checking. Thank you!)\n\n")
        
        while True:
            self.input_question()
            self.input_and_format_options(file)
            answer=input("Input correct answer:")
            file.write("Correct Answer: "+answer+"\n")

            if not self.add_more(file):
                import os
                file.close()
                os.startfile(self.filename)
                break

    def input_question(self):
        while True:
            question=input("Question:") #Asks user for input
            self.question_with_choice+=question+"\n"#Adds new line so choices will be written below the question"
            self.options.clear() #clears items in options list, so the number from preceding numbers re not printed
                            #again in the following numbers.
            break

    def input_and_format_options(self, file):
        while self.option_count!=4:#So user will be asked for 4 options
            option = input("Add option:")#Ask user for option
            self.options.append(option)#Adds user's input into 'options' list
            self.option_count = self.option_count + 1 #Adds one count to inputted options to keep tract how any are added.

        for options_item_index, option in enumerate(self.options):
            self.question_with_choice += f"{chr(ord('a')+options_item_index)}. {option} \n"
            
        file.write(self.question_with_choice)
    
    def add_more(self, file):
        while True:
            ask = input("\nAdd another question?(Y/N)")
            if ask.lower()=="y":
                new_line="\n"
                print("\n----------\n")
                file.write(new_line)
                self.question_with_choice=""
                self.option_count=0
                return True

            elif ask.lower() == "n":
                print("\nThank you for using basic quiz maker. The file you have edited will now be opened so you can"
                      "check the changes.\n")
                return False

            else:
                print(".\n.\n.\nyou can only answer Y or N\n----------\n")
                continue
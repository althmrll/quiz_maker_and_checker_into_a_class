import option_one

class option_two(option_one):
    def __init__(self, options, question_with_choice, option_count, filename):
        self.filename=filename
        super.__init__(options, question_with_choice, option_count)
    
    def option_mechanics(self, filename):
        file = open(filename, "a")
        space="\n"
        file.write(space)
        file.write("(This is the start of your editing using quiz maker. Delete this after checking. Thank you!)\n\n")
        
        while True:
            option_one.input_question(self)
            option_one.input_and_format_options
            answer=input("Input correct answer:")
            file.write("Correct Answer: "+answer+"\n")

            if not option_one.add_more(self, file):
                import os
                file.close()
                os.startfile(filename)
                break
    
    def add_more(self, file):
        while True:
            ask = input("\nAdd another question?(Y/N)")
            if ask == "Y" or ask == "y":
                
                new_line="\n"
                file.write(new_line)
                print("\n----------\n")
                question_with_choice=""
                break

            elif ask == "N" or ask == "n":
                print("\nThank you for using basic quiz maker. The file you have edited will now be opened so you can"
                      "check the changes.\n")
                return False

            else:
                print(".\n.\n.\nyou can only answer Y or N\n----------\n")
                continue
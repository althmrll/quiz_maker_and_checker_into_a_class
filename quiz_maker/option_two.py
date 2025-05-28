import option_one

class option_two(option_one):
    def __init__(self, filename):
        self.filename=filename
        super.__init__()
    
    def option_mechanics(self, filename):
        file = open(filename, "a")
        space="\n"
        file.write(space)
        file.write("(This is the start of your editing using quiz maker. Delete this after checking. Thank you!)\n\n")
        
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
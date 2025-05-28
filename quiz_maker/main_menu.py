import option_one
import option_two

class main_menu:
    def __init__(self, choice):
        self.choice=choice

    def menu_mechanics(self, choice):
        print("BASIC QUIZ MAKER")
        print("\nTo get started\n"
            "1:Create Quiz\n"
            "2:Edit Existing Quiz\n"
            "3:Exit\n")
        
        while True:
            try:
                choice = (int(input("What do you want to do? Pick 1, 2, or, 3:")))
                if choice==1:
                    print("\n----------\n\nYou have chosen 'CREATE QUIZ'\n")
                    new_quiz=option_one(open("Untitled Quiz.txt", "w"))
                    new_quiz.option_mechanics(self)

                if choice==2:
                    print("\n----------\n\nYou have chosen 'EDIT EXISTING QUIZ'")
                    filename=input("\nInput filename of quiz you want to edit(be mindful with the cases and spaces):")
                    print("\n")
                    filename=option_two(filename+'.txt')
                    filename.option_mechanics(self, filename)

                elif choice==3:
                    print("\n----------\n\nYou have chosen 'EXIT'\n\n\nGoodbye!")
                    break

                else:
                    print(".\n.\n.\nYou can only pick between 1, 2, and 3.\n\n----------\n")

            except ValueError:
                print(".\n.\n.\nYou can only pick between 1, 2, and 3.\n\n----------\n")

if __name__ == "__main__":
    main_menu.menu_mechanics()
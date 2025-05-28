from option_1 import option_one
from option_2 import option_two

class main_menu:
    def run(self):
        print("BASIC QUIZ MAKER")
        print("\nTo get started\n"
              "1: Create Quiz\n"
              "2: Edit Existing Quiz\n"
              "3: Exit\n")

        while True:
            try:
                choice = int(input("What do you want to do? Pick 1, 2, or 3: "))
                if choice == 1:
                    print("\n----------\n\nYou have chosen 'CREATE QUIZ'\n")
                    option_one().create_new_quiz()
                    break
                elif choice == 2:
                    print("\n----------\n\nYou have chosen 'EDIT EXISTING QUIZ'")
                    filename = input("\nInput filename of quiz to edit (without .txt): ")
                    print("\n")
                    option_two(filename).edit_existing_quiz()
                    break
                elif choice == 3:
                    print("\n----------\n\nYou have chosen 'EXIT'\n\n\nGoodbye!")
                    break
                else:
                    print(".\n.\n.\nYou can only pick between 1, 2, and 3.\n\n----------\n")
            except ValueError:
                print(".\n.\n.\nYou can only pick between 1, 2, and 3.\n\n----------\n")

if __name__ == "__main__":
    main_menu().run()

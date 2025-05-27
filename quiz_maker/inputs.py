class inputs:
    def __init__(self, choice):
        question=input("Question:") #Asks user for input
        question_with_choice+=question+"\n"#Adds new line so choices will be written below the question"
        option_count = 0
        options.clear() #clears items in options list, so the number from preceding numbers re not printed
                        #again in the following numbers.

        while option_count!=4:#So user will be asked for 4 options
            option = input("Add option:")#Ask user for option
            options.append(option)#Adds user's input into 'options' list
            option_count = option_count + 1 #Adds one count to inputted options to keep tract how any are added.

        for options_item_index, option in enumerate(options):
            question_with_choice += f"{chr(ord('a')+options_item_index)}. {option} \n"
        file.write(question_with_choice)

        answer=input("Input correct answer:")
        file.write("Correct Answer: "+answer+"\n")

        while True:
            ask = input("\nAdd another question?(Y/N)")
            if ask == "Y" or ask == "y":
                new_line="\n"
                print("\n----------\n")
                file.write(new_line)
                question_with_choice=""
                break

            choice = (int(input("What do you want to do? Pick 1, 2, or, 3:")))
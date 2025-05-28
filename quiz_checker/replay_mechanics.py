#Replay
def replay():#Add choice wether to exit the program or answer another quiz.

    global replay_choice
    replay_choice=""
    while True:
        replay=input("Do you want to answer another quiz?(Y/N)")
        if replay=="Y" or replay=="y":
            choose_file()
        elif replay=="N" or replay=="n":
            print("Goodbye!")
            choose_file_window.destroy()
            exit()
        else:
            print("Invalid Output, Reasking Question...")
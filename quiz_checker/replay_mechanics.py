class Replay:
    def __init__(self):
        pass

    def replay_process(self):
        while True:
            replay=input("Do you want to answer another quiz?(Y/N)")
            if replay.lower()=="y":
                break
            elif replay.lower()=="n":
                print("Goodbye!")
                exit()
            else:
                print("Invalid Output, Reasking Question...")
                return False
class Replay:
    def __init__(self, replay_choice):
        self.replay_choice=replay_choice

    def replay_mechanics(self):
        while True:
            replay=self.replay_choice(input("Do you want to answer another quiz?(Y/N)"))
            if replay.lower()=="y":
                break
            elif replay.lower()=="n":
                print("Goodbye!")
                exit()
            else:
                print("Invalid Output, Reasking Question...")
                return False
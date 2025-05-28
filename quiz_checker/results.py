from replay_mechanics import replay
from quiz_mechanics import quiz
import quiz_mechanics

class results_mechanics(quiz_mechanics):
    def __init__(self):
        super().__init__()
        self.answer=quiz_mechanics.answer()
        self.score=quiz_mechanics.score()
        self.replay=replay

    def finish(self):#Flash ending message, positive if passed, negative if failed.
        passing=len(self.answer)/2
        if self.score>=passing:
            print(f"\n\nYou have finished the quiz and answered {self.score} questions out of {len(self.answer)}. Congrats!\n\n----------\n")
            
        else:
            print(f"\n\nYou have finished the quiz and answered {self.score} questions out of {len(self.answer)}. Better luck next time!\n\n----------\n")
            self.replay
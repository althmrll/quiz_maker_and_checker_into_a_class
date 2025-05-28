#Results
def finish():#Flash ending message, positive if passed, negative if failed.
    passing=len(answer)/2
    if score>=passing:
        print(f"\n\nYou have finished the quiz and answered {score} questions out of {len(answer)}. Congrats!\n\n----------\n")
        replay()
    else:
        print(f"\n\nYou have finished the quiz and answered {score} questions out of {len(answer)}. Better luck next time!\n\n----------\n")
        replay()
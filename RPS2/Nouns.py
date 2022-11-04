#Write a function that prints a string depending on the correct singular or plural noun

def Nouns(Wins: int, Rounds: int):
        if Wins == 1:
                print(f"You won {Wins} round out of {Rounds}")
        else:
                print(f"You won {Wins} rounds out of {Rounds}")


Nouns(2,3)
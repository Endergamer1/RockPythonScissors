#Write a function that

def horz_bar():
  print("+" + "-+" * 20)

def end_banner(Game =(int,int)):
 print("Thanks for playing Rock Paper Scissors!")
 if Game[0] > 0:
    print(f">>> You won {Game[0]} rounds out of {Game[1]}. <<<")
    horz_bar()

end_banner((1,3))
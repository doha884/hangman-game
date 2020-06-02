import imdb
import random
def hangman():
    ia = imdb.IMDb()
    top = ia.get_top250_movies()

    turns=10
    guesses=""

    num = random.randint(1, 250)
    print(num)
    strmv = str(top[num])
    while len(strmv)>0:
        missed=0
        outputwrd=""
        for char in strmv.lower():
            if char in guesses:
                outputwrd=outputwrd+char
            else:
                outputwrd=outputwrd+"_"+""
        print(outputwrd)
        if outputwrd==strmv.lower():
            print(outputwrd)
            print("you won.i hope u didnt cheat ")
            break
        guess=input("enter guess:")
        guesses=guesses+guess

        if guess not in strmv.lower():
            turns=turns-1
            if turns==9:
                print("9 turns left")
                print("________")
            if turns==8:
                print("8 turns left")
                print("________")
                print(' o ')
            if turns == 7:
                print("7 turns left")
                print("_______")
                print(" 0 ")
                print(" | ")
            if turns == 6:
                print(" 6 turns left")
                print("_______")
                print(" 0 ")
                print(" | ")
                print("/")
            if turns == 5:
                print(" 5 turns left")
                print("_______")
                print(" 0 ")
                print(" | ")
                print('/ \ ')
            if turns == 4:
                print("4 turns left")
                print("_______")
                print(" 0 ")
                print("/| ")
                print("/ \ ")
            if turns == 3:
                print("3 turns left")
                print("_______")
                print(" 0 ")
                print("/|\ ")
                print("/ \ ")
            if turns == 2:
                print("2 turns left")
                print("  --------  ")
                print("   \ O /|   ")
                print("     |      ")
                print("    / \     ")
            if turns == 1:
                print("1 turns left")
                print("Last breaths counting, Take care!")
                print("  --------  ")
                print("   \ O_|/   ")
                print("     |      ")
                print("    / \     ")
            if turns == 0:
                print("You loose")
                print("You let a kind man die")
                print("  --------  ")
                print("     O_|    ")
                print("    /|\      ")
                print("    / \     ")
                break



    return outputwrd
name=input("please enter your name: ")
print("hello "+name)
print("____________")
print("this is a hangman game.dont let it hang to death.")
print("u will also have to guess any punctuation and all in smaller case")
print("try guessin in 10 attempts")


hangman()









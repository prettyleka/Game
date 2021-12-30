import CurrencyRouletteGame as crg
import GuessGame as gg
import MemoryGame as mg
import Score.Package_functions as packageF
import Utils as u




class Live:
    def welcome(self):
        name = input("Your name is ")
        print(f"Hello {name} and welcome to the World of Games (WoG).Here you can find many cool games to play.")

    def load_game(self):
        self.welcome()
        numOfGame = self.numOfGame()
        diff = self.difficultyOfGame()
        if numOfGame == str(1):
            self.m = mg.MemoryGame()
            resultM=self.m.play(diff)
            if resultM:
                packageF.add_score(difficalty=int(diff))
            else:
                pass
        elif numOfGame == str(2):
            self.g = gg.GuessGame()
            resultG = self.g.play(diff)
            if resultG:
                packageF.add_score(difficalty=int(diff))
            else:
                pass
        elif numOfGame == str(3):
            self.cr = crg.CurrencyRouletteGame()
            resultCR=self.cr.play(diff)
            if resultCR:
                packageF.add_score(difficalty=int(diff))
            else:
                pass
        x=1
        while x>0:
            self.wantToPlayMore()
            self.wantToClearTheScreen()
            numOfGame = self.numOfGame()
            diff = self.difficultyOfGame()
            if numOfGame == str(1):
                self.m = mg.MemoryGame()
                resultM = self.m.play(diff)
                if resultM:
                    packageF.add_score(difficalty=int(diff))
                else:
                    pass
            elif numOfGame == str(2):
                self.g = gg.GuessGame()
                resultG = self.g.play(diff)
                if resultG:
                    packageF.add_score(difficalty=int(diff))
                else:
                    pass
            elif numOfGame == str(3):
                self.cr = crg.CurrencyRouletteGame()
                resultCR = self.cr.play(diff)
                if resultCR:
                    packageF.add_score(difficalty=int(diff))
                else:
                    pass

            x+=1


    def numOfGame(self):
        print(
            "Please choose a game to play:\n 1. Memory Game - a sequence of numbers will appear for 1 second and you have to "
            "guess it back\n 2. Guess Game - guess a number and see if you chose like the computer\n 3. Currency Roulette - try and guess the value of a random amount of USD in ILS")
        numOFGame = input("What game do you prefer to play? ")
        while numOFGame.isdigit() == False or int(numOFGame) > 3 or int(numOFGame) == 0:
            numOFGame = input("Please, enter the number of the game (only from 1 to 3) ")
        return numOFGame

    def difficultyOfGame(self):
        difficulty = input("Please choose game difficulty from 1 to 5: ")
        while difficulty.isdigit() == False or int(difficulty) > 5 or int(difficulty) == 0:
            difficulty = input("Please choose game difficulty from 1 to 5: ")
        return difficulty

    def wantToPlayMore(self):
        print("Do you want to play more?")
        answer = input("please, answer Y or N ")
        if answer == "Y":
            pass
        elif answer =="N":
            print("Bye")
            quit()

    def wantToClearTheScreen(self):
        print("Do you want to clear the screen?")
        answer = input("please, answer Y or N ")
        if answer == "Y":
            self.util = u.Utils()
            self.util.Screen_cleaner()
        elif answer == "N":
            pass





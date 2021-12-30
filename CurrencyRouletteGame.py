import random
import requests


class CurrencyRouletteGame:
    def get_money_interval(self, tUSD, d):
        print(f"The random number of USD is {tUSD}")
        rateILS = self.getILSrate()
        tILS = tUSD* float(rateILS)
        startPoint = tILS - (5 - int(d))
        sndPoint = tILS + (5 - int(d))
        interval=[startPoint, sndPoint]
        return interval

    def getRandomUSDAmount(self):
        return random.randint(1,100)

    def get_guess_from_user(self, tUSD):
        answer = input(f"If the USD amount is {tUSD}, what you think will be the ILS amount? ")
        return answer

    def play(self, d):
        tUSD=self.getRandomUSDAmount()
        interval = self.get_money_interval(tUSD=tUSD, d=d)
        answer = self.get_guess_from_user(tUSD)
        if int(interval[0])<=int(answer)<=int(interval[1]):
            print("YOU WIN!")
            return True
        else:
            print("YOU LOSE!")
            return False

    def getILSrate(self):
        response = requests.get('https://openexchangerates.org/api/latest.json?app_id=bf86c4e995534d4fa56f9ac815d04a43')
        rates = response.json()['rates']
        return rates['ILS']





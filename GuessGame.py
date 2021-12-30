import random


class GuessGame:

    def generate_number(self, difficalty):
        secret_number = random.randint(1,int(difficalty))
        return secret_number

    def get_guess_from_user(self, difficalty):
        num = input(f"Please guess the number between 1 to {difficalty} ")
        return num

    def compare_results(self, secret_number, num):
        if int(secret_number)==int(num):
            print("True")
            return True
        else:
            print("False")
            return False

    def play(self, difficalty):
        secret_number = self.generate_number(difficalty)
        num = self.get_guess_from_user(difficalty)
        return self.compare_results(secret_number=secret_number, num=num)







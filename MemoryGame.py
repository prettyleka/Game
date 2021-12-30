import random

class MemoryGame:

    def generate_sequence(self, difficalty):
        randomlist = random.sample(range(1, 101), int(difficalty))
        with open("randomlist.txt", "w+") as w:
            w.write(str(randomlist))
            w.close()
        return randomlist

    def get_list_from_user(self, difficalty):
        usersList = []
        while len(usersList)<int(difficalty):
            num = input("Please, enter the number you remember ")
            usersList.append(int(num))
        return usersList

    def is_list_equal(self, randomList, usersList):
        if randomList == usersList:
            print("You Win :)")
            return True
        else:
            print("You Lose :(")
            return False

    def play(self, difficalty):
        randomlist = self.generate_sequence(difficalty)
        print(randomlist)
        usersList = self.get_list_from_user(difficalty)
        r = self.is_list_equal(randomList=randomlist, usersList=usersList)
        return r








import Live

class MainGame:
    def play(self):
        self.l =Live.Live()
        self.l.load_game()

if __name__ == '__main__':
    m=MainGame()
    m.play()
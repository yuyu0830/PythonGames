import random as rd

class game:
    def __init__(self):
        self.state = 1 # 1 start 2 ingame 3 gameover 4 clear
        pass

    def run(self):
        if self.state == 1:
            self.start_screen()

        elif self.state == 2:
            self.game()

    def game(self):
        
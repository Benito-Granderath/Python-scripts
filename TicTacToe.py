class gameboard:
    def __init__(self):
        self.situation = [0, 0, 0, 0, 0, 0, 0, 0, 0]

    def turn(self, cell, player):
        if self.valid_turn(cell):
            self.situation[cell] = player.Character
            return True
        return False
    def valid_turn(self, cell):
        if self.situation[cell] == 0:
            return True
        else:
            return False
    def check_for_win(self, player):
        s = player.Character
        if self.situation[0] == s and self.situation[1] == s and self.situation[2] == s:
            return True
        elif self.situation[3] == s and self.situation[4] == s and self.situation[5] == s:
            return True
        elif self.situation[6] == s and self.situation[7] == s and self.situation[8] == s:
            return True

        elif self.situation[0] == s and self.situation[4] == s and self.situation[8] == s:
            return True
        elif self.situation[2] == s and self.situation[4] == s and self.situation[6] == s:
            return True

        elif self.situation[0] == s and self.situation[3] == s and self.situation[6] == s:
            return True
        elif self.situation[1] == s and self.situation[4] == s and self.situation[7] == s:
            return True
        elif self.situation[2] == s and self.situation[5] == s and self.situation[8] == s:
            return True

    def is_full(self):
        for i in self.situation:
            if i == 0:
                return False
        return True


    def situation_to_visualization(self, convert):
        if convert == 0:
            return " "
        elif convert == 1:
            return "X"
        else:
            return "O"

    def board_visualization(self):
        print(" " + self.situation_to_visualization(self.situation[0]) + " | " + self.situation_to_visualization(self.situation[1]) + " | " + self.situation_to_visualization(self.situation[2]) + "\n" +
              " " + self.situation_to_visualization(self.situation[3]) + " | " + self.situation_to_visualization(self.situation[4]) + " | " + self.situation_to_visualization(self.situation[5]) + "\n" +
              " " + self.situation_to_visualization(self.situation[6]) + " | " + self.situation_to_visualization(self.situation[7]) + " | " + self.situation_to_visualization(self.situation[8]))
class Player:
    def __init__(self, Character):
        self.Character = Character

if __name__ == '__main__':
    player_1 = Player(1)
    player_2 = Player(-1)
    Board = gameboard()
    active_player = player_1
    while not Board.is_full():
        Board.board_visualization()
        try:
            cell = int(input("It's your turn. Where do you want to place your character? [1-9]: "))
        except ValueError:
            continue
        cell = cell - 1
        if cell < 0 or cell > 8:
            print("Please enter a valid integer [1-9]")
            continue
        if not Board.turn(cell, active_player):
            print("Error: Invalid Move")
            continue
        if Board.check_for_win(active_player):
            print("Congratulations. You win!!!")
            break
        if active_player == player_1:
            active_player = player_2
        else:
            active_player = player_1
    if Board.is_full():
        print("It's a Tie!!!")


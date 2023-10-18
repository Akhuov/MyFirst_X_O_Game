from os import system

class x_o:
    def __init__(self):
        self.a = [[10 for i in range(3)] for i in range(3)]
        self.show()
        self.free = 9
        self.player = 0

    def game_loop(self):
        while self.free:
            if not self.check():
                self.turn()
                self.free-=1
                if self.check():
                    print ('"X" Wins!!!!')
                    break
                if self.free==0:
                    self.free-=1
                    break
            else:
                print ('"O" Wins!!!!')
                break

            if not self.check():
                self.turn()
                self.free-=1
            else:
                print ('"X" Wins!!!!')
                break
        if self.free == -1:
            print (")))Draw(((")
    
    def show(self):
        system('cls')
        print("+---"*3+'+')

        for layer in self.a:
            for i in layer:
                print(f"| {'X' if not i else ' ' if i == 10 else 'O'} ", end="")
            print("|")
            print("+---"*3+'+')

        # for i in range(9):
        #      print(f"| {self.a[i]}",end=' |\n' if i%3==2 else ' ')
        #      if (i+1)%3==0:
        #         print("+---"*3+'+')

    def turn(self):
        player_character = 'O' if self.player else 'X'
        pos = input(f"{player_character}'s turn: ")

        if not pos.isdigit():
            print("Error! Try Again!")
            return self.turn()

        pos = int(pos)
        
        y = pos % 10 - 1
        x = (pos - (y + 1)) // 10 - 1

        if x not in range(0, 3) or y not in range(0, 3) or self.a[x][y] != 10:
            print("Error! Try Again!")
            return self.turn()

        self.a[x][y] = self.player
            
        self.show()
        self.player = not self.player

    def check(self):
        return self.check_rows() or self.check_cols() or self.check_dias()
        
    def check_rows(self):
        for row in self.a:
            if sum(row) == 0 or sum(row) == 3:
                return True
        return False
    
    def check_cols(self):
        for i in range(0, 3):
            col_sum = 0
            for j in range(0, 3):
                col_sum += self.a[j][i]

            if col_sum == 0 or col_sum == 3:
                return True
        return False
    
    def check_dias(self):
        dias = [0, 0]
        for i in range(0,3):
            dias[0] += self.a[i][i]
            dias[1] += self.a[i][2 - i]
        
        if 0 in dias or 3 in dias:
            return True
        return False


if __name__=='__main__':
    x_o().game_loop()
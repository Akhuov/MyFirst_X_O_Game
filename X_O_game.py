from os import system

class x_o:
    def __init__(self):
        self.a = [' ',' ',' ',' ',' ',' ',' ',' ',' '] 
        self.show()
        self.free = 9
        self.player = 0
        while self.free:
            if self.check()!=0:
                self.turn()
                self.free-=1
                if self.check()==0:
                    print ('"X" Wins!!!!')
                    break
                if self.free==0:
                    self.free-=1
                    break
            else:
                print ('"O" Wins!!!!')
                break
            if self.check()!=0:
                self.turn()
                self.free-=1
            else:
                print ('"X" Wins!!!!')
                break
        if self.free==-1:
            print (")))Draw(((")
    
    def show(self):
        system('cls')
        print("+---"*3+'+')
        for i in range(9):
             print(f"| {self.a[i]}",end=' |\n' if i%3==2 else ' ')
             if (i+1)%3==0:
                print("+---"*3+'+')

    def turn(self):
        player_character = 'O' if self.player else 'X'
        pos = input(f"{player_character}'s turn: ")

        if not pos.isdigit():
            print("Error! Try Again!")
            self.turn

        pos = int(pos)

        if pos not in range(1, 10):
            print("Error! Try Again!")

        self.a[pos - 1] = player_character
        self.show()
        self.player = not self.player
        
    # def step_x(self):
    #     x = int(input("\nX`s step: "))
    #     if x==0 or x > 9 > 0 or self.a[x-1] !=' ':
    #         print ("Error\nTry again")
    #         self.step_x()
    #     else:
    #         self.a[x-1] = 'X'
    #     self.show()

    # def step_o(self):
    #     x = int(input("\nO`s step: "))
    #     if   x==0 or x > 9 > 0 or self.a[x-1] !=' ':
    #         print ("Error\nTry again:")
    #         self.step_o()
    #     else:
    #         self.a[x-1] = 'O'
    #     self.show()

    def check(self):
        if self.a[0] == self.a[1] == self.a[2] != " " or  self.a[0] == self.a[4] == self.a[8] !=' ' or self.a[0] == self.a[3] == self.a[6] !=" ":
            return 0
        elif self.a[3] == self.a[4] == self.a[5]!=' ' or self.a[2] == self.a[4] == self.a[6]!=" " or self.a[1] == self.a[4] == self.a[7]!=" ":
            return 0
        elif self.a[6] == self.a[7] == self.a[8]!=" " or self.a[2] == self.a[5] == self.a[8]!=" ":
            return 0
        else:
            return 1

if __name__=='__main__':
    x_o()
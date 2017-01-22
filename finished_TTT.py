from Tkinter import *
import tkMessageBox
import tkSimpleDialog
import tkFont
import random

xscore = 0
oscore = 0
button_clicks = 0


class Application(Frame):

    def __init__(self, master):
        Frame.__init__(self, master)
        tkMessageBox.showinfo("Welcome", "Presenting Tic Tac Toe")
        self.create_game_mode()
        self.pack()
        master.mainloop()
    
    def create_game_mode(self):
        global xscore
        global oscore
        helv63 = tkFont.Font(size=24)
        self.scorex = Label(self, text = "X = %s" %(xscore))
        self.scorex.grid(row = 4, column = 4)
        self.scoreo = Label(self, text= "O = %s" %(oscore))
        self.scoreo.grid(row= 4, column = 3)
        self.playervsConsole = Button(self, text = "Player Vs Console", command = self.pvc)
        self.playervsplayer = Button(self, text = "Player Vs Player", command = self.pvp)
        
        self.playervsConsole.grid(row= 3, column= 0)
        self.playervsplayer.grid(row= 3, column=1)
        
    def pvp(self):
        self.name = tkSimpleDialog.askstring("Name", "Name of Person 1:")
        self.name2 = tkSimpleDialog.askstring("Name", "Name of Person 2:")
        self.nals = [self.name, self.name2]
        self.rand_names = self.nals[random.randrange(len(self.nals))]
        if self.rand_names == self.name:
            tkMessageBox.showinfo("Welcome", "hello %s is 'X' and %s is 'O' 'X' goes first!"% (self.name, self.name2))
            self.playerx = self.name
            self.playero = self.name2
        else:
            tkMessageBox.showinfo("Welcome", "hello %s is 'X' and %s is 'O' 'X' goes first!"% (name2, name))
            self.playerx = self.name2
            self.playero= self.name

        helv36 = tkFont.Font(size=18)

        self.square1=Button(self, text="", command=self.square1_label, width=10, height=5, font = helv36)
        self.square2=Button(self, text="", command=self.square2_label, width=10, height=5, font = helv36)
        self.square3=Button(self, text="", command=self.square3_label, width=10, height=5, font = helv36)                
        self.square4=Button(self, text="", command=self.square4_label, width=10, height=5, font = helv36)                
        self.square5=Button(self, text="", command=self.square5_label, width=10, height=5, font = helv36)                
        self.square6=Button(self, text="", command=self.square6_label, width=10, height=5, font = helv36)                
        self.square7=Button(self, text="", command=self.square7_label, width=10, height=5, font = helv36)                
        self.square8=Button(self, text="", command=self.square8_label, width=10, height=5, font = helv36)                              
        self.square9=Button(self, text="", command=self.square9_label, width=10, height=5, font = helv36)                

        self.square1.grid(row=0, column=0)
        self.square2.grid(row=0, column=1)
        self.square3.grid(row=0, column=2)
        self.square4.grid(row=1, column=0)
        self.square5.grid(row=1, column=1)
        self.square6.grid(row=1, column=2)
        self.square7.grid(row=2, column=0)
        self.square8.grid(row=2, column=1)
        self.square9.grid(row=2, column=2)

    def pvc(self): 
        self.machine = "computer"
        self.user_name = tkSimpleDialog.askstring("Player Name","Name of Humanoid")
        self.players = [self.user_name, self.machine]
        self.rand_names = self.players[random.randrange(len(self.players))]
        helv36 = tkFont.Font(size=18)
        self.square1=Button(self, text="", command= self.pvc_square1_label, width=10, height=5, font = helv36)
        self.square2=Button(self, text="", command= self.pvc_square2_label, width=10, height=5, font = helv36)
        self.square3=Button(self, text="", command= self.pvc_square3_label, width=10, height=5, font = helv36)                
        self.square4=Button(self, text="", command= self.pvc_square4_label, width=10, height=5, font = helv36)
        self.square5=Button(self, text="", command= self.pvc_square5_label, width=10, height=5, font = helv36)                
        self.square6=Button(self, text="", command= self.pvc_square6_label, width=10, height=5, font = helv36)                
        self.square7=Button(self, text="", command= self.pvc_square7_label, width=10, height=5, font = helv36)                
        self.square8=Button(self, text="", command= self.pvc_square8_label, width=10, height=5, font = helv36)                              
        self.square9=Button(self, text="", command= self.pvc_square9_label, width=10, height=5, font = helv36)

        self.square1.grid(row=0, column=0)
        self.square2.grid(row=0, column=1)
        self.square3.grid(row=0, column=2)
        self.square4.grid(row=1, column=0)
        self.square5.grid(row=1, column=1)
        self.square6.grid(row=1, column=2)
        self.square7.grid(row=2, column=0)
        self.square8.grid(row=2, column=1)
        self.square9.grid(row=2, column=2)
        if self.rand_names == self.machine:
            self.playerx = self.machine
            self.playero = self.user_name
            tkMessageBox.showinfo("Welcome", "hello %s is 'X' and %s is 'O' 'X' goes first!"% (self.machine, self.user_name))
            self.machine_block_sequence()
        else:
            self.playerx = self.user_name
            self.playero = self.machine
            tkMessageBox.showinfo("Welcome", "hello %s is 'X' and %s is 'O'. 'X' goes first!"% (self.user_name, self.machine))
    
    def machine_turn(self):
        global button_clicks
        self.winning_sequence()
        self.turn_label()
        if self.playerx == self.user_name:
            self.playero = self.machine
        else:
            self.playerx = self.machine
            self.playero = self.user_name
        if self.square5["text"] == "": #priority: Center
            if self.playero == self.machine:
                self.square5["text"] = "O"
                button_clicks += 1
            else:
                self.square5["text"] = "X"
                button_clicks +=1
        elif self.square1["text"] == "": #priority: Corners
            if self.playero == self.machine:
                self.square1["text"] = "O"
                button_clicks += 1
            else:
                self.square1["text"] = "X"
                button_clicks += 1
        elif self.square3["text"] == "":
            if self.playero == self.machine:
                self.square3["text"] = "O"
                button_clicks += 1
            else:
                self.square3["text"] = "X"
                button_clicks += 1
        elif self.square7["text"] == "":
            if self.playero == self.machine:
                self.square7["text"] = "O"
                button_clicks += 1
            else:
                self.square7["text"] = "X"
                button_clicks += 1
        elif self.square9["text"] == "":
            if self.playero == self.machine:
                self.square9["text"] = "O"
                button_clicks += 1
            else:
                self.square9["text"] = "X"
                button_clicks += 1

        elif self.square2["text"] == "": #else: Edges   
            if self.playero == self.machine:
                self.square2["text"] = "O"
                button_clicks += 1
            else:
                self.square2["text"] = "X"
                button_clicks += 1
        elif self.square6["text"] == "":
            if self.playero == self.machine:
                self.square6["text"] = "O"
                button_clicks += 1
            else:
                self.square6["text"] = "X"
                button_clicks +=1
        elif self.square8["text"] == "":
            if self.playero == self.machine:
                self.square8["text"] = "O"
                button_clicks += 1
            else:
                self.square8["text"] = "X"
                button_clicks += 1
        else:
            if self.square4["text"] == "":
                if self.playero == self.machine:
                    self.square4["text"] = "O"
                    button_clicks += 1
                else:
                    self.square4["text"] = "X"
                    button_clicks += 1
    def machine_block_sequence(self):
        self.winning_sequence()
        self.turn_label()
        global button_clicks
        if self.playerx == self.user_name:
            if self.square1["text"]== "X" and self.square2["text"]== "X" and self.square3["text"]== "":
                self.square3["text"] = "O"
                button_clicks += 1

            elif self.square4["text"]== "X" and self.square5["text"] == "X" and self.square6["text"]== "":
                self.square6["text"] = "O"
                button_clicks += 1

            elif self.square7["text"]== "X" and self.square8["text"] == "X" and self.square9["text"]== "":
                self.square9["text"]= "O"
                button_clicks += 1

            elif self.square1["text"]== "X" and self.square4["text"]== "X" and self.square7["text"]== "":
                self.square7["text"] = "O"
                button_clicks += 1

            elif self.square2["text"]== "X" and self.square5["text"]== "X" and self.square8["text"]== "":
                self.square8["text"] = "O"
                button_clicks += 1

            elif self.square3["text"]== "X" and self.square6["text"]== "X" and self.square9["text"]== "":
                self.square9["text"] = "O"
                button_clicks += 1

            elif self.square1["text"]== "X" and self.square5["text"]== "X" and self.square9["text"]== "":
                self.square9["text"] = "O"
                button_clicks += 1

            elif self.square3["text"]== "X" and self.square5["text"]== "X" and self.square7["text"]== "":
                self.square7["text"] = "O"
                button_clicks +=1 

            elif self.square1["text"]== "X" and self.square3["text"]== "X" and self.square2["text"]== "":
                self.square2["text"] = "O"
                button_clicks +=1 

            elif self.square4["text"]== "X" and self.square6["text"] == "X" and self.square5["text"]== "":
                self.square5["text"] = "O"
                button_clicks +=1 

            elif self.square7["text"]== "X" and self.square9["text"] == "X" and self.square8["text"]== "":
                self.square8["text"]= "O"
                button_clicks +=1

            elif self.square1["text"]== "X" and self.square7["text"]== "X" and self.square4["text"]== "":
                self.square4["text"] = "O"
                button_clicks+=1

            elif self.square2["text"]== "X" and self.square8["text"]== "X" and self.square5["text"]== "":
                self.square5["text"] = "O"
                button_clicks+=1

            elif self.square3["text"]== "X" and self.square9["text"]== "X" and self.square6["text"]== "":
                self.square6["text"] = "O"
                button_clicks+=1

            elif self.square1["text"]== "X" and self.square9["text"]== "X" and self.square5["text"]== "":
                self.square5["text"] = "O"
                button_clicks+=1

            elif self.square3["text"]== "X" and self.square7["text"]== "X" and self.square5["text"]== "":
                self.square5["text"] = "O"
                button_clicks +=1

            elif self.square2["text"]== "X" and self.square3["text"]== "X" and self.square1["text"]== "":
                self.square1["text"] = "O"
                button_clicks +=1

            elif self.square5["text"]== "X" and self.square6["text"]== "X" and self.square4["text"]== "":
                self.square4["text"] = "O"
                button_clicks +=1

            elif self.square8["text"]== "X" and self.square9["text"]== "X" and self.square7["text"]== "":
                self.square7["text"] = "O"
                button_clicks +=1

            elif self.square4["text"]== "X" and self.square7["text"]== "X" and self.square1["text"]== "":
                self.square1["text"] = "O"
                button_clicks +=1

            elif self.square5["text"]== "X" and self.square8["text"]== "X" and self.square2["text"]== "":
                self.square2["text"] = "O"
                button_clicks +=1

            elif self.square6["text"]== "X" and self.square9["text"]== "X" and self.square3["text"]== "":
                self.square3["text"] = "O"
                button_clicks +=1

            elif self.square5["text"]== "X" and self.square9["text"]== "X" and self.square1["text"]== "":
                self.square1["text"] = "O"
                button_clicks +=1
            elif self.square5["text"]== "X" and self.square7["text"]== "X" and self.square3["text"]== "":
                self.square3["text"] = "O"
                button_clicks +=1
            else:
                self.machine_turn()

        if self.playero == self.user_name:
            if self.square1["text"]== "O" and self.square2["text"]== "O" and self.square3["text"]== "":
                self.square3["text"] = "X"
                button_clicks +=1

            elif self.square4["text"]== "O" and self.square5["text"] == "O" and self.square6["text"]== "":
                self.square6["text"] = "X"
                button_clicks +=1

            elif self.square7["text"]== "O" and self.square8["text"] == "O" and self.square9["text"]== "":
                self.square9["text"]= "X"
                button_clicks +=1

            elif self.square1["text"]== "O" and self.square4["text"]== "O" and self.square7["text"]== "":
                self.square7["text"] = "X"
                button_clicks +=1

            if self.square2["text"]== "O" and self.square5["text"]== "O" and self.square8["text"]== "":
                self.square8["text"] = "X"
                button_clicks +=1

            elif self.square3["text"]== "O" and self.square6["text"]== "O" and self.square9["text"]== "":
                self.square9["text"] = "X"
                button_clicks+=1

            elif self.square1["text"]== "O" and self.square5["text"]== "O" and self.square9["text"]== "":
                self.square9["text"] = "X"
                button_clicks+=1

            elif self.square3["text"]== "O" and self.square5["text"]== "O" and self.square7["text"]== "":
                self.square7["text"] = "X"
                button_clicks +=1

            elif self.square1["text"]== "O" and self.square3["text"]== "O" and self.square2["text"]== "":
                self.square2["text"] = "X"
                button_clicks+=1

            elif self.square4["text"]== "O" and self.square6["text"] == "O" and self.square5["text"]== "":
                self.square5["text"] = "X"
                button_clicks+=1

            elif self.square7["text"]== "O" and self.square9["text"] == "O" and self.square8["text"]== "":
                self.square8["text"]= "X"
                button_clicks+=1

            elif self.square1["text"]== "O" and self.square7["text"]== "O" and self.square4["text"]== "":
                self.square4["text"] = "X"
                button_clicks+=1

            elif self.square2["text"]== "O" and self.square8["text"]== "O" and self.square5["text"]== "":
                self.sqaure5["text"] = "X"
                button_clicks+=1

            elif self.square3["text"]== "O" and self.square9["text"]== "O" and self.square6["text"]== "":
                self.square6["text"] = "X"
                button_clicks+=1

            elif self.square1["text"]== "O" and self.square9["text"]== "O" and self.square5["text"]== "":
                self.square5["text"] = "X"
                button_clicks+=1

            elif self.square2["text"]== "O" and self.square3["text"]== "O" and self.square1["text"]== "":
                self.square1["text"] = "X"
                button_clicks+=1

            elif self.square5["text"]== "O" and self.square6["text"]== "O" and self.square4["text"]== "":
                self.square4["text"] = "X"
                button_clicks+=1

            elif self.square8["text"]== "O" and self.square9["text"]== "O" and self.square7["text"]== "":
                self.square7["text"] = "X"
                button_clicks+=1

            elif self.square4["text"]== "O" and self.square7["text"]== "O" and self.square1["text"]== "":
                self.square1["text"] = "X"
                button_clicks+=1

            elif self.square5["text"]== "O" and self.square8["text"]== "O" and self.square2["text"]== "":
                self.square2["text"] = "X"
                button_clicks+=1

            elif self.square6["text"]== "O" and self.square9["text"]== "O" and self.square3["text"]== "":
                self.square3["text"] = "X"
                button_clicks+=1

            elif self.square5["text"]== "O" and self.square9["text"]== "O" and self.square1["text"]== "":
                self.square1["text"] = "X"
                button_clicks+=1

            elif self.square5["text"]== "O" and self.square7["text"]== "O" and self.square3["text"]== "":
                self.square3["text"] = "X"
                button_clicks+=1
            else:
                self.machine_turn()
        self.winning_sequence()
        
    def turn_label(self):
        global button_clicks
        helv12 = tkFont.Font(size=18)
        if button_clicks >=1:
            self.turn = ["X","O"]
            if button_clicks % 2 == 0:
                self.label = Label(self, text = "Turn = O", font = helv12)
                self.label.grid(row=3, column = 2)
            else:
                self.label = Label(self, text = "Turn = X", font = helv12)
                self.label.grid(row=3, column=2)
    
    def pvc_square1_label(self):
        global button_clicks
        self.turn_label()
        helv36 = tkFont.Font(size=18)
        if self.playero == self.machine:
            self.playerx = self.user_name
        self.square1['font'] = helv36
        while self.square1["text"] == "":
            if self.playerx == self.user_name:
                self.square1["text"]="X"
                button_clicks += 1
                self.machine_block_sequence()
            else:
                self.square1["text"]="O"
                button_clicks += 1
                self.machine_block_sequence()
        self.winning_sequence()
    
    def pvc_square2_label(self):
        global button_clicks
        self.turn_label()
        helv36 = tkFont.Font(size=18)
        if self.playero == self.machine:
            self.playerx = self.user_name
        self.square2['font'] = helv36
        while self.square2["text"] == "":
            if self.playerx == self.user_name:
                self.square2["text"]="X"
                button_clicks += 1
                self.machine_block_sequence()
            else:
                self.square2["text"]="O"
                button_clicks += 1
                self.machine_block_sequence()
        self.winning_sequence()

    def pvc_square3_label(self):
        global button_clicks
        self.turn_label()
        helv36 = tkFont.Font(size=18)
        if self.playero == self.machine:
            self.playerx = self.user_name
        self.square3['font'] = helv36
        while self.square3["text"] == "":
            if self.playerx == self.user_name:
                self.square3["text"]="X"
                button_clicks += 1
                self.machine_block_sequence()
            else:
                self.square3["text"]="O"
                button_clicks += 1
                self.machine_block_sequence()
        self.winning_sequence()

    def pvc_square4_label(self):
        global button_clicks
        self.turn_label()
        helv36 = tkFont.Font(size=18)
        global button_clicks
        if self.playero == self.machine:
            self.playerx = self.user_name
        self.square4['font'] = helv36

        while self.square4["text"] == "":
            if self.playerx == self.user_name:
                self.square4["text"]="X"
                button_clicks += 1
                self.machine_block_sequence()
            else:
                self.square4["text"]="O"
                button_clicks += 1
                self.machine_block_sequence()
        self.winning_sequence()
                                    
    def pvc_square5_label(self):
        global button_clicks
        self.turn_label()
        helv36 = tkFont.Font(size=18)
        if self.playero == self.machine:
            self.playerx = self.user_name
        self.square5['font'] = helv36

        while self.square5["text"] == "":
            if self.playerx == self.user_name:
                self.square5["text"]="X"
                button_clicks += 1
                self.machine_block_sequence()
            else:
                self.square5["text"]="O"
                button_clicks += 1
                self.machine_block_sequence()
        self.winning_sequence()

    def pvc_square6_label(self):
        global button_clicks
        self.turn_label()
        helv36 = tkFont.Font(size=18)
        if self.playero == self.machine:
            self.playerx = self.user_name
        self.square6['font'] = helv36
        while self.square6["text"] == "":
            if self.playerx == self.user_name:
                self.square6["text"]="X"
                button_clicks += 1
                self.machine_block_sequence()
            else:
                self.square6["text"]="O"
                button_clicks += 1
                self.machine_block_sequence()
        self.winning_sequence()

    def pvc_square7_label(self):
        global button_clicks
        self.turn_label()
        helv36 = tkFont.Font(size=18)
        if self.playero == self.machine:
            self.playerx = self.user_name
        self.square7['font'] = helv36
        while self.square7["text"] == "":
            if self.playerx == self.user_name:
                self.square7["text"]="X"
                button_clicks += 1
                self.machine_block_sequence()
            else:
                self.square7["text"]="O"
                button_clicks += 1
                self.machine_block_sequence()
        self.winning_sequence()

    def pvc_square8_label(self):
        global button_clicks
        self.turn_label()
        helv36 = tkFont.Font(size=18)
        if self.playero == self.machine:
            self.playerx = self.user_name
        self.square8['font'] = helv36
        while self.square8["text"] == "":
            if self.playerx == self.user_name:
                self.square8["text"]="X"
                button_clicks += 1
                self.machine_block_sequence()
            else:
                self.square8["text"]="O"
                button_clicks += 1
                self.machine_block_sequence()
        self.winning_sequence()

    def pvc_square9_label(self):
        global button_clicks
        self.turn_label()
        helv36 = tkFont.Font(size=18)
        if self.playero == self.machine:
            self.playerx = self.user_name
        self.square9['font'] = helv36
        while self.square9["text"] == "":
            if self.playerx == self.user_name:
                self.square9["text"]="X"
                button_clicks += 1
                self.machine_block_sequence()
            else:
                self.square9["text"]="O"
                button_clicks += 1
                self.machine_block_sequence()
        self.winning_sequence()
    def square1_label(self):
        global button_clicks
        self.turn_label()
        helv36 = tkFont.Font(size=18)
        self.square1['font'] = helv36

        while self.square1["text"] == "":
            if button_clicks % 2 == 0:
                self.square1["text"]="X"
                button_clicks += 1
                
            else:
                self.square1["text"]="O"
                button_clicks += 1   
        self.winning_sequence()

    def square2_label(self):
        global button_clicks
        self.turn_label()
        helv36 = tkFont.Font(size=18)
        self.square2['font'] = helv36

        while self.square2["text"] == "":
            if button_clicks % 2 ==0:
                self.square2["text"]="X"
                button_clicks += 1
            else:
                self.square2["text"]="O"
                button_clicks += 1
        self.winning_sequence()

    def square3_label(self):
        global button_clicks
        self.turn_label()
        helv36 = tkFont.Font(size=18)
        self.square3['font'] = helv36
        while self.square3["text"] == "":
            if button_clicks % 2 ==0:
                self.square3["text"]="X"
                button_clicks += 1
            else:
                self.square3["text"]="O"
                button_clicks += 1
        self.winning_sequence()

    def square4_label(self):
        global button_clicks
        self.turn_label()
        helv36 = tkFont.Font(size=18)       
        self.square4['font'] = helv36
        while self.square4["text"] == "":
            if button_clicks % 2 ==0:
                self.square4["text"]="X"
                button_clicks += 1
            else:
                self.square4["text"]="O"
                button_clicks += 1
        self.winning_sequence()
                                    
    def square5_label(self):
        global  button_clicks
        self.turn_label()
        helv36 = tkFont.Font(size=18)
        self.square5['font'] = helv36
        while self.square5["text"] == "":
            if button_clicks % 2 ==0:
                self.square5["text"]="X"
                button_clicks += 1
            else:
                self.square5["text"]="O"
                button_clicks += 1
        self.winning_sequence()

    def square6_label(self):
        global button_clicks
        self.turn_label()
        helv36 = tkFont.Font(size=18)        
        self.square6['font'] = helv36
        while self.square6["text"] == "":
            if button_clicks % 2 ==0:
                self.square6["text"]="X"
                button_clicks += 1
            else:
                self.square6["text"]="O"
                button_clicks += 1
        self.winning_sequence()

    def square7_label(self):
        global button_clicks
        self.turn_label()
        helv36 = tkFont.Font(size=18)        
        self.square7['font'] = helv36
        while self.square7["text"] == "":
            if button_clicks % 2 ==0:
                self.square7["text"]="X"
                button_clicks += 1
            else:
                self.square7["text"]="O"
                button_clicks += 1
        self.winning_sequence()

    def square8_label(self):
        global button_clicks
        self.turn_label()
        helv36 = tkFont.Font(size=18)
        self.square8['font'] = helv36
        while self.square8["text"] == "":
            if button_clicks % 2 ==0:
                self.square8["text"]="X"
                button_clicks += 1
            else:
                self.square8["text"]="O"
                button_clicks += 1
        self.winning_sequence()

    def square9_label(self):
        global button_clicks
        self.turn_label()
        helv36 = tkFont.Font(size=18)
        self.square9['font'] = helv36
        while self.square9["text"] == "":
            if button_clicks % 2 ==0:
                self.square9["text"]="X"
                button_clicks += 1
            else:
                self.square9["text"]="O"
                button_clicks += 1
        self.winning_sequence()

    def winning_sequence(self):
        global button_clicks
        if self.square1["text"] == "X" and self.square2["text"] == "X" and self.square3["text"] == "X":
            self.square1.configure(fg="red")
            self.square2.configure(fg="red")
            self.square3.configure(fg="red")
            self.winner_found("X")

        if self.square4["text"] == "X" and self.square5["text"] == "X" and self.square6["text"]== "X":
            self.square4.configure(fg="red")
            self.square5.configure(fg="red")
            self.square6.configure(fg="red")
            self.winner_found("X")
        
        if self.square7["text"] == "X" and self.square8["text"] == "X" and self.square9["text"]== "X":
            self.square7.configure(fg="red")
            self.square8.configure(fg="red")
            self.square9.configure(fg="red")
            self.winner_found("X")
                                                    #HORIZONTAL WINS
        if self.square1["text"] == "X" and self.square4["text"] == "X" and self.square7["text"]== "X":
            self.square1.configure(fg="red")
            self.square4.configure(fg="red")
            self.square7.configure(fg="red")
            self.winner_found("X")
        if self.square2["text"] == "X" and self.square5["text"] == "X" and self.square8["text"]== "X":
            self.square2.configure(fg="red")
            self.square5.configure(fg="red")
            self.square8.configure(fg="red")
            self.winner_found("X")

        if self.square3["text"] == "X" and self.square6["text"] == "X" and self.square9["text"]== "X":
            self.square3.configure(fg="red")
            self.square6.configure(fg="red")
            self.square9.configure(fg="red")
            self.winner_found("X")

        if self.square1["text"] == "X" and self.square5["text"] == "X" and self.square9["text"]== "X":
            self.square1.configure(fg="red")
            self.square5.configure(fg="red")
            self.square9.configure(fg="red")
            self.winner_found("X")

        if self.square3["text"] == "X" and self.square5["text"] == "X" and self.square7["text"]== "X":
            self.square3.configure(fg="red")
            self.square5.configure(fg="red")
            self.square7.configure(fg="red")
            self.winner_found("X")

        if self.square1["text"] == "O" and self.square2["text"] == "O" and self.square3["text"] == "O":
            self.square1.configure(fg="red")
            self.square2.configure(fg="red")
            self.square3.configure(fg="red")
            self.winner_found("O")

        if self.square4["text"] == "O" and self.square5["text"] == "O" and self.square6["text"]== "O":
            self.square4.configure(fg="red")
            self.square5.configure(fg="red")
            self.square6.configure(fg="red")
            self.winner_found("O")

        if self.square7["text"] == "O" and self.square8["text"] == "O" and self.square9["text"]== "O":
            self.square7.configure(fg="red")
            self.square8.configure(fg="red")
            self.square9.configure(fg="red")
            self.winner_found("O")

        if self.square1["text"] == "O" and self.square4["text"] == "O" and self.square7["text"]== "O":
            self.square1.configure(fg="red")
            self.square4.configure(fg="red")
            self.square7.configure(fg="red")
            self.winner_found("O")

        if self.square2["text"] == "O" and self.square5["text"] == "O" and self.square8["text"]== "O":
            self.square2.configure(fg="red")
            self.square5.configure(fg="red")
            self.square8.configure(fg="red")
            self.winner_found("O")

        if self.square3["text"] == "O" and self.square6["text"] == "O" and self.square9["text"]== "O":
            self.square3.configure(fg="red")
            self.square6.configure(fg="red")
            self.square9.configure(fg="red")
            self.winner_found("O")
                                                        #VERTICAL WINS
        if self.square1["text"] == "O" and self.square5["text"] == "O" and self.square9["text"]== "O":
            self.square1.configure(fg="red")
            self.square5.configure(fg="red")
            self.square9.configure(fg="red")
            self.winner_found("O")

        if self.square3["text"] == "O" and self.square5["text"] == "O" and self.square7["text"]== "O":
            self.square3.configure(fg="red")
            self.square5.configure(fg="red")
            self.square7.configure(fg="red")
            self.winner_found("O")
        
        if button_clicks == 9:
            self.cats_game()
    def winner_found(self, symbol):
        global xscore
        global oscore
        if symbol == "X":
            xscore += 1
            tkMessageBox.showinfo('Winner', symbol + ' Won!')
            answer = tkMessageBox.askquestion('Congratulations!', 'Play Again?')
            self.resetGame(answer)
        else:
            oscore += 1
            tkMessageBox.showinfo('Winner', symbol + ' Won!')
            answer = tkMessageBox.askquestion('Congratulations!', 'Play Again?')
            self.resetGame(answer)
    def resetGame(self, answer):
        global button_clicks
        self.turn_label()
        button_clicks = 0
        if answer == 'yes':
            self.square1["text"] = " "
            self.square2["text"] = " "
            self.square3["text"] = " "
            self.square4["text"] = " "
            self.square5["text"] = " "
            self.square6["text"] = " "
            self.square7["text"] = " "
            self.square8["text"] = " "
            self.square9["text"] = " "
            self.square1.grid_remove()
            self.square2.grid_remove()
            self.square3.grid_remove()
            self.square4.grid_remove()
            self.square5.grid_remove()
            self.square6.grid_remove()
            self.square7.grid_remove()
            self.square8.grid_remove()
            self.square9.grid_remove()
            self.square1.configure(fg="black")
            self.square2.configure(fg="black")
            self.square3.configure(fg="black")
            self.square4.configure(fg="black")
            self.square5.configure(fg="black")
            self.square6.configure(fg="black")
            self.square7.configure(fg="black")
            self.square8.configure(fg="black")
            self.square9.configure(fg="black")
            self.create_game_mode()
        else:
            self.master.destroy()

    def cats_game(self):
        tkMessageBox.showinfo('Cats Game','Cats Game!')
        answer = tkMessageBox.askquestion('Cats Game', 'Play Again?')
        if answer == "yes":
            self.resetGame(answer)
        else:
            self.master.destroy()

if __name__ == "__main__":
    master = Tk()
    Application(master)
    master.mainloop()

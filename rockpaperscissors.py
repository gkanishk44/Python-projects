from tkinter import *
import random

root = Tk()
root.geometry('400x400')
root.resizable(0,0)
root.title('DataFlair-Rock,Paper,Scissors')
root.config(bg ='seashell3')


Label(root, text = 'Rock, Paper ,Scissors' , font='calibri 20 bold', bg = 'violet').pack()


user_take = StringVar()
Label(root, text = 'choose any one: rock, paper ,scissors' , font='arial 11 bold', bg = 'yellow').place(x = 30,y=70)
Entry(root, font = 'arial 15', textvariable = user_take , bg = 'white').place(x=70 , y = 130)


comp_pick = random.randint(1,3)
if comp_pick == 1:
    comp_pick = 'rock'
elif comp_pick ==2:
    comp_pick = 'paper'
else:
    comp_pick = 'scissors'
    

Result = StringVar()

def play():
    user_pick = user_take.get()
    if user_pick == comp_pick:
        Result.set('tie,you both select same')
    elif user_pick == 'rock' and comp_pick == 'paper':
        Result.set('you lose,computer selected paper')
    elif user_pick == 'rock' and comp_pick == 'scissors':
        Result.set('you win,computer selected scissors')
    elif user_pick == 'paper' and comp_pick == 'scissors':
        Result.set('you lose,computer selected scissors')
    elif user_pick == 'paper' and comp_pick == 'rock':
        Result.set('you win,computer selected rock')
    elif user_pick == 'scissors' and comp_pick == 'rock':
        Result.set('you lose,computer selected rock')
    elif user_pick == 'scissors' and comp_pick == 'paper':
        Result.set('you win ,computer selected paper')
    else:
        Result.set('invalid: choose any one -- rock, paper, scissors')
    
        
  
def Reset():
    Result.set("") 
    user_take.set("")

def Exit():
    root.destroy()


Entry(root, font = 'arial 10 bold', textvariable = Result, bg ='white',width = 50,).place(x=10, y = 250)

Button(root, font = 'arial 13 bold', text = 'PLAY'  ,padx =5,bg ='Green' ,command = play).place(x=150,y=190)

Button(root, font = 'arial 13 bold', text = 'RESET'  ,padx =5,bg ='blue' ,command = Reset).place(x=70,y=310)

Button(root, font = 'arial 13 bold', text = 'EXIT'  ,padx =5,bg ='Red' ,command = Exit).place(x=230,y=310)

root.mainloop()
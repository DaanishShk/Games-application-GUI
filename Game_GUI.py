from tkinter import *
from tkinter import Menu
from tkinter import messagebox
import os


def developers():
    messagebox.showinfo('Developers', 'Member1\t\t\t- Street Racer\nMember2\t\t\t- Snake\nMember3'
                                      '\t\t\t- Pac Man\nMember4\t\t\t- Falling Skies\nDaanish Shaikh\t\t\t- '
                                      'UI\n')


def version():
    messagebox.showinfo('Version', '\n\tVerion 1.0\t\n\n')

def race():
    os.startfile('Race.py')

def pac():
    os.startfile('Pac_man.py')

def skies():
    os.startfile('Falling_skies.py')

def memory():
    os.startfile('Memory.py')



main = Tk()
main.title('Game Launcher')
main.geometry('800x600')
main.wm_iconbitmap('Controller.ico')
main.resizable(0, 0)

canvas = Canvas(main, bg='#BE0909')
canvas.place(relwidth=1, relheight=1)

ftitle = LabelFrame(canvas)
title = Label(ftitle, text='GAME ZONE', font=('ROG FONTS', 40))
ftitle.place(relx=0.5, rely=0.05, relwidth=0.55, relheight=0.14, anchor='n')
title.pack(fill=BOTH)

window1 = Canvas(canvas, bg='white', bd=0, highlightthickness=1, highlightbackground='black')
window1.place(relx=0.05, rely=0.25, relheight=0.34, relwidth=0.445)
image1 = PhotoImage(file='Car Race.png')
Label(window1, text='    Avoid the oncoming traffic on the\n highway and score high.', font=('ERAS Medium ITC', 15),
      anchor='nw',image=image1,compound=BOTTOM).place(relx=0.005, rely=0.005, relheight=0.989, relwidth=0.989)
Button(window1, text='PLAY', font=('Bauhaus 93', 20), relief=GROOVE, bd=1.5,command=race).place(relx=0.77, rely=0.7)

window2 = Canvas(canvas, bg='white', bd=0, highlightthickness=1, highlightbackground='black')
window2.place(relx=0.5, rely=0.25, relheight=0.34, relwidth=0.445)
image2=PhotoImage(file='Pac.png')
Label(window2, text='    Collect the yellow dots while\n avoiding the enemies.', font=('ERAS Medium ITC', 15),
      anchor='nw',image=image2,compound=BOTTOM).place(relx=0.005, rely=0.005, relheight=0.989, relwidth=0.989)
Button(window2, text='PLAY', font=('Bauhaus 93', 20), relief=GROOVE, bd=1.5,command=pac).place(relx=0.77, rely=0.7)

window3 = Canvas(canvas, bg='white', bd=0, highlightthickness=1, highlightbackground='black')
window3.place(relx=0.05, rely=0.6, relheight=0.34, relwidth=0.445)
image3=PhotoImage(file='Falling.png')
Label(window3, text='    Collect blue dots to increase your \n score.', font=('ERAS Medium ITC', 15),
      anchor='nw',image=image3,compound=BOTTOM).place(relx=0.005, rely=0.005, relheight=0.989, relwidth=0.989)
Button(window3, text='PLAY', font=('Bauhaus 93', 20), relief=GROOVE, bd=1.5,command=skies).place(relx=0.77, rely=0.7)

window4 = Canvas(canvas, bg='white', bd=0, highlightthickness=1, highlightbackground='black')
window4.place(relx=0.5, rely=0.6, relheight=0.34, relwidth=0.445)
image4=PhotoImage(file='Tiles.png')
Label(window4, text='    Collect the green squares\n using the snake.', font=('ERAS Medium ITC', 15),
      anchor='nw',image=image4,compound=BOTTOM).place(relx=0.005, rely=0.005, relheight=0.989, relwidth=0.989)
Button(window4, text='PLAY', font=('Bauhaus 93', 20), relief=GROOVE, bd=1.5,command=memory).place(relx=0.77, rely=0.7)

menu = Menu(main)
Developers = menu.add_cascade(label='Developers', command=developers)
Version = menu.add_cascade(label='Version', command=version)
main.config(menu=menu)

main.mainloop()

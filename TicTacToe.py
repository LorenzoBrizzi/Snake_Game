#TicTacToe Game

from tkinter import *
from tkinter import ttk
import time



root = Tk()                                                                                                                     #inserisco una finestra vuota che ho chiamato root
#root.geometry("500x500")
root.resizable(False, False)
root.wm_title("TicTacToe")                                                                                        #modifico il titolo della finestra
root.iconbitmap("tris.ico")


Contendente_1 = PhotoImage(file="Franco.png")
Contendente_2 = PhotoImage(file="Cervello.png")


def set_move(event):
    time.sleep(0.2)
    label = Label(Frame_0, image=Contendente_1)
    label.grid()
    return




header = ttk.Label(root, text="Benvenuto su TicTacToe!", font='Helvetica 14 bold')                              #metto un header top
header.grid(row=0, column=0)

#frame vuoti per caselle

Frame_0 = Frame(root, width=250, height=250, bg="white")
Frame_0.bind("<Button-1>", set_move)
Frame_0.bind("<Button-3>",)
Frame_0.grid(row=1, column=0)

Frame_1 = Frame(root, width=250, height=250, bg="white")
Frame_1.bind("<Button-1>",)#qui metto il nome della funzione da eseguire
Frame_1.bind("<Button-3>",)#qui metto il nome della funzione da eseguire
Frame_1.grid(row=1, column=2)

Frame_2 = Frame(root, width=250, height=250, bg="white")
Frame_2.bind("<Button-1>",)#qui metto il nome della funzione da eseguire
Frame_2.bind("<Button-3>",)#qui metto il nome della funzione da eseguire
Frame_2.grid(row=1, column=4)

Frame_3 = Frame(root, width=250, height=250, bg="white")
Frame_3.bind("<Button-1>",)#qui metto il nome della funzione da eseguire
Frame_3.bind("<Button-3>",)#qui metto il nome della funzione da eseguire
Frame_3.grid(row=3, column=0)

Frame_4 = Frame(root, width=250, height=250, bg="white")
Frame_4.bind("<Button-1>",)#qui metto il nome della funzione da eseguire
Frame_4.bind("<Button-3>",)#qui metto il nome della funzione da eseguire
Frame_4.grid(row=3, column=2)

Frame_5 = Frame(root, width=250, height=250, bg="white")
Frame_5.bind("<Button-1>",)#qui metto il nome della funzione da eseguire
Frame_5.bind("<Button-3>",)#qui metto il nome della funzione da eseguire
Frame_5.grid(row=3, column=4)

Frame_6 = Frame(root, width=250, height=250, bg="white")
Frame_6.bind("<Button-1>",)#qui metto il nome della funzione da eseguire
Frame_6.bind("<Button-3>",)#qui metto il nome della funzione da eseguire
Frame_6.grid(row=5, column=0)

Frame_7 = Frame(root, width=250, height=250, bg="white")
Frame_7.bind("<Button-1>",)#qui metto il nome della funzione da eseguire
Frame_7.bind("<Button-3>",)#qui metto il nome della funzione da eseguire
Frame_7.grid(row=5, column=2)

Frame_8 = Frame(root, width=250, height=250, bg="white")
Frame_8.bind("<Button-1>",)#qui metto il nome della funzione da eseguire
Frame_8.bind("<Button-3>",)#qui metto il nome della funzione da eseguire
Frame_8.grid(row=5, column=4)


#separatori orizzontali

#prima fila di separatori
Separator_0 = Frame(root, width=5, height=250, bg="black")
Separator_0.grid(row=1, column=1)

Separator_1 = Frame(root, width=5, height=250, bg="black")
Separator_1.grid(row=1, column=3)

Separator_2 = Frame(root, width=5, height=250, bg="black")
Separator_2.grid(row=3, column=1)

Separator_3 = Frame(root, width=5, height=250, bg="black")
Separator_3.grid(row=3, column=3)

Separator_4 = Frame(root, width=5, height=250, bg="black")
Separator_4.grid(row=5, column=1)

Separator_5 = Frame(root, width=5, height=250, bg="black")
Separator_5.grid(row=5, column=3)


#separatori orizzontali

#prima fila di separatori e giunti
separator_0 = Frame(root, width=250, height=5, bg="black")
separator_0.grid(row=2, column=0)

separator_1 = Frame(root, width=5, height=5, bg="black")
separator_1.grid(row=2, column=1)

separator_2 = Frame(root, width=250, height=5, bg="black")
separator_2.grid(row=2, column=2)

separator_3 = Frame(root, width=5, height=5, bg="black")
separator_3.grid(row=2, column=3)

separator_4 = Frame(root, width=250, height=5, bg="black")
separator_4.grid(row=2, column=4)

#seconda fila di separatori e giunti
separator_5 = Frame(root, width=250, height=5, bg="black")
separator_5.grid(row=4, column=0)

separator_6 = Frame(root, width=5, height=5, bg="black")
separator_6.grid(row=4, column=1)

separator_7 = Frame(root, width=250, height=5, bg="black")
separator_7.grid(row=4, column=2)

separator_8 = Frame(root, width=5, height=5, bg="black")
separator_8.grid(row=4, column=3)

separator_9 = Frame(root, width=250, height=5, bg="black")
separator_9.grid(row=4, column=4)


root.mainloop()
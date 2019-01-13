#TicTacToe Game

from tkinter import *
from tkinter import ttk
import time



root = Tk()
root.resizable(False, False)
root.wm_title("TicTacToe")                                                                                        #modifico il titolo della finestra
root.iconbitmap("tris.ico")
Contendente_1 = PhotoImage(file="Franco.png")
Contendente_2 = PhotoImage(file="Cervello.png")

#funzione prima casella
def set_move_contendente_1_1(event):
    time.sleep(0.2)
    label = Label(Frame_0, image=Contendente_1)
    label.grid()
    return
def set_move_contendente_2_1(event):
    label = Label(Frame_0, image=Contendente_2)
    label.grid()
    return

#funzione seconda casella
def set_move_contendente_1_2(event):
    time.sleep(0.2)
    label = Label(Frame_1, image=Contendente_1)
    label.grid()
    return
def set_move_contendente_2_2(event):
    label = Label(Frame_1, image=Contendente_2)
    label.grid()
    return

#funzione terza casella
def set_move_contendente_1_3(event):
    time.sleep(0.2)
    label = Label(Frame_2, image=Contendente_1)
    label.grid()
    return
def set_move_contendente_2_3(event):
    label = Label(Frame_2, image=Contendente_2)
    label.grid()
    return

#funzione quarta casella
def set_move_contendente_1_4(event):
    time.sleep(0.2)
    label = Label(Frame_3, image=Contendente_1)
    label.grid()
    return
def set_move_contendente_2_4(event):
    label = Label(Frame_3, image=Contendente_2)
    label.grid()
    return

#funzione quinta casella
def set_move_contendente_1_5(event):
    time.sleep(0.2)
    label = Label(Frame_4, image=Contendente_1)
    label.grid()
    return
def set_move_contendente_2_5(event):
    label = Label(Frame_4, image=Contendente_2)
    label.grid()
    return

#funzione sesta casella
def set_move_contendente_1_6(event):
    time.sleep(0.2)
    label = Label(Frame_5, image=Contendente_1)
    label.grid()
    return
def set_move_contendente_2_6(event):
    label = Label(Frame_5, image=Contendente_2)
    label.grid()
    return

#funzione settima casella
def set_move_contendente_1_7(event):
    time.sleep(0.2)
    label = Label(Frame_6, image=Contendente_1)
    label.grid()
    return
def set_move_contendente_2_7(event):
    label = Label(Frame_6, image=Contendente_2)
    label.grid()
    return

#funzione ottava casella
def set_move_contendente_1_8(event):
    time.sleep(0.2)
    label = Label(Frame_7, image=Contendente_1)
    label.grid()
    return
def set_move_contendente_2_8(event):
    label = Label(Frame_7, image=Contendente_2)
    label.grid()
    return

#funzione nona casella
def set_move_contendente_1_9(event):
    time.sleep(0.2)
    label = Label(Frame_8, image=Contendente_1)
    label.grid()
    return
def set_move_contendente_2_9(event):
    label = Label(Frame_8, image=Contendente_2)
    label.grid()
    return



header = ttk.Label(root, text="Benvenuto su TicTacToe!", font='Helvetica 14 bold')                              #metto un header top
header.grid(row=0, column=0)

#frame vuoti per caselle

Frame_0 = Frame(root, width=250, height=250, bg="white")
Frame_0.bind("<Button-1>", set_move_contendente_1_1)
Frame_0.bind("<Button-3>", set_move_contendente_2_1)
Frame_0.grid(row=1, column=0)

Frame_1 = Frame(root, width=250, height=250, bg="white")
Frame_1.bind("<Button-1>", set_move_contendente_1_2)
Frame_1.bind("<Button-3>", set_move_contendente_2_2)
Frame_1.grid(row=1, column=2)

Frame_2 = Frame(root, width=250, height=250, bg="white")
Frame_2.bind("<Button-1>", set_move_contendente_1_3)
Frame_2.bind("<Button-3>", set_move_contendente_2_3)
Frame_2.grid(row=1, column=4)

Frame_3 = Frame(root, width=250, height=250, bg="white")
Frame_3.bind("<Button-1>", set_move_contendente_1_4)
Frame_3.bind("<Button-3>", set_move_contendente_2_4)
Frame_3.grid(row=3, column=0)

Frame_4 = Frame(root, width=250, height=250, bg="white")
Frame_4.bind("<Button-1>", set_move_contendente_1_5)
Frame_4.bind("<Button-3>", set_move_contendente_2_5)
Frame_4.grid(row=3, column=2)

Frame_5 = Frame(root, width=250, height=250, bg="white")
Frame_5.bind("<Button-1>", set_move_contendente_1_6)
Frame_5.bind("<Button-3>", set_move_contendente_2_6)
Frame_5.grid(row=3, column=4)

Frame_6 = Frame(root, width=250, height=250, bg="white")
Frame_6.bind("<Button-1>", set_move_contendente_1_7)
Frame_6.bind("<Button-3>", set_move_contendente_2_7)
Frame_6.grid(row=5, column=0)

Frame_7 = Frame(root, width=250, height=250, bg="white")
Frame_7.bind("<Button-1>", set_move_contendente_1_8)
Frame_7.bind("<Button-3>", set_move_contendente_2_8)
Frame_7.grid(row=5, column=2)

Frame_8 = Frame(root, width=250, height=250, bg="white")
Frame_8.bind("<Button-1>", set_move_contendente_1_9)
Frame_8.bind("<Button-3>", set_move_contendente_2_9)
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
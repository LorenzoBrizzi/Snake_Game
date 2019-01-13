#TicTacToe Game

from tkinter import *
from tkinter import ttk

root = Tk()                                                                                                                     #inserisco una finestra vuota che ho chiamato root
#root.geometry("500x500")                                                                                                        #do una dimensione alla mia finestra chiamate root
root.wm_title("TicTacToe")                                                                                        #modifico il titolo della finestra
root.iconbitmap("tris.ico")


header = ttk.Label(root, text="Benvenuto su TicTacToe!", font='Helvetica 20 bold')                              #metto un header top
header.grid(row=0, column=0)


Frame_0 = Frame(root, width=30, height=30, bg="green")
Frame_0.grid(row=1, column=0)
#tkinter.ttk.Separator.grid(column=1, row=2, rowspan=3, sticky=NS)

Frame_1 = Frame(root, width=30, height=30, bg="red")
Frame_1.grid(row=1, column=1)
#tkinter.ttk.Separator.grid(column=1, row=2, rowspan=3, sticky=NS)

Frame_2 = Frame(root, width=30, height=30, bg="green")
Frame_2.grid(row=1, column=2)
#tkinter.ttk.Separator.grid(column=1, row=2, rowspan=3, sticky=NS)

Frame_3 = Frame(root, width=30, height=30, bg="red")
Frame_3.grid(row=2, column=0)
#tkinter.ttk.Separator.grid(column=1, row=2, rowspan=3, sticky=NS)

Frame_4 = Frame(root, width=30, height=30, bg="green")
Frame_4.grid(row=2, column=1)
#tkinter.ttk.Separator.grid(column=1, row=2, rowspan=3, sticky=NS)

Frame_5 = Frame(root, width=30, height=30, bg="red")
Frame_5.grid(row=2, column=2)
#tkinter.ttk.Separator.grid(column=1, row=2, rowspan=3, sticky=NS)

Frame_6 = Frame(root, width=30, height=30, bg="green")
Frame_6.grid(row=3, column=0)
#tkinter.ttk.Separator.grid(column=1, row=2, rowspan=3, sticky=NS)

Frame_7 = Frame(root, width=30, height=30, bg="red")
Frame_7.grid(row=3, column=1)
#tkinter.ttk.Separator.grid(column=1, row=2, rowspan=3, sticky=NS)

Frame_8 = Frame(root, width=30, height=30, bg="green")
Frame_8.grid(row=3, column=2)
#tkinter.ttk.Separator.grid(column=1, row=2, rowspan=3, sticky=NS)




root.mainloop()
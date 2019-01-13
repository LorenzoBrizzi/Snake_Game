#TicTacToe Game

from tkinter import *
from tkinter import ttk

root = Tk()                                                                                                                     #inserisco una finestra vuota che ho chiamato root
#root.geometry("500x500")                                                                                                        #do una dimensione alla mia finestra chiamate root
root.wm_title("TicTacToe")                                                                                        #modifico il titolo della finestra
root.iconbitmap("tris.ico")


header = ttk.Label(root, text="Benvenuto su TicTacToe!", font='Helvetica 20 bold')                              #metto un header top
header.grid(row=0, column=0)


Frame_0 = Frame(root)
Frame_0.grid(row=1, column=0, columnspan=10, rowspan=10)
#tkinter.ttk.Separator(root, orient=VERTICAL).grid(column=1, row=2, rowspan=3, sticky=NS)

Frame_1 = Frame(root)
Frame_1.grid(row=1, column=1, columnspan=10, rowspan=10)
#tkinter.ttk.Separator(root, orient=VERTICAL).grid(column=1, row=2, rowspan=3, sticky=NS)

Frame_2 = Frame(root)
Frame_2.grid(row=1, column=2, columnspan=10, rowspan=10)
#tkinter.ttk.Separator(root, orient=VERTICAL).grid(column=1, row=2, rowspan=3, sticky=NS)

Frame_3 = Frame(root)
Frame_3.grid(row=2, column=0, columnspan=10, rowspan=10)
#tkinter.ttk.Separator(root, orient=VERTICAL).grid(column=1, row=2, rowspan=3, sticky=NS)

Frame_4 = Frame(root)
Frame_4.grid(row=2, column=1, columnspan=10, rowspan=10)
#tkinter.ttk.Separator(root, orient=VERTICAL).grid(column=1, row=2, rowspan=3, sticky=NS)

Frame_5 = Frame(root)
Frame_5.grid(row=2, column=2, columnspan=10, rowspan=10)
#tkinter.ttk.Separator(root, orient=VERTICAL).grid(column=1, row=2, rowspan=3, sticky=NS)

Frame_6 = Frame(root)
Frame_6.grid(row=3, column=0, columnspan=10, rowspan=10)
#tkinter.ttk.Separator(root, orient=VERTICAL).grid(column=1, row=2, rowspan=3, sticky=NS)

Frame_7 = Frame(root)
Frame_7.grid(row=3, column=1, columnspan=10, rowspan=10)
#tkinter.ttk.Separator(root, orient=VERTICAL).grid(column=1, row=2, rowspan=3, sticky=NS)

Frame_8 = Frame(root)
Frame_8.grid(row=3, column=2, columnspan=10, rowspan=10)
#tkinter.ttk.Separator(root, orient=VERTICAL).grid(column=1, row=2, rowspan=3, sticky=NS)




root.mainloop()
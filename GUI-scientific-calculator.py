from tkinter import *
import random
import time

root = Tk()
root.geometry("1600x700+0+0")
root.title("Calculator app")

Tops = Frame(root,bg="Black",width = 1600,height=50,relief=SUNKEN)
Tops.pack(side=TOP)

f1 = Frame(root,width = 900,height=700,relief=SUNKEN)
f1.pack(side=LEFT)
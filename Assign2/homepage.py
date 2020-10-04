import wqi
import tkinter as tk
from tkinter import ttk 
from tkinter import * 
from tkinter.ttk import *
from tkinter import filedialog
import pandas as pd


def add_home(home):
    label = tk.Label(home, text = "Water Quality Estimation Tool", font = ("Verdana", 30))
    label.place(x = 120, y = 40)
    instructions = []
    instructions.append(tk.Label(home, text = "Welcome to the Water Quality Estimation Tool. ", font = ("Verdana", 15)))
    instructions.append(tk.Label(home, text = "The tab TASK 1 calculates the Water Quality Index using the weighted mean strategy.", font = ("Verdana", 15)))
    instructions.append(tk.Label(home, text = "The tab TASK 2 calculates the Overall Index of Pollution in Indian Context.", font = ("Verdana", 15)))
    instructions.append(tk.Label(home, text = "The tab TASK 3 calculates the Water Quality Index using ML given input as a time series", font = ("Verdana", 15)))
    instructions.append(tk.Label(home, text = " of parameters.", font = ("Verdana", 15)))
    instructions[0].place(x = 10, y = 100)
    instructions[1].place(x = 10, y = 130)
    instructions[2].place(x = 10, y = 160)
    instructions[3].place(x = 10, y = 190)
    instructions[4].place(x = 10, y = 220)

    tk.Button(home, text='QUIT', command=home.quit).grid(row=50, column=50, sticky=tk.W, pady=500, padx=400)
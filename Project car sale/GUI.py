from fileinput import close
import PySimpleGUI as sg
import _tkinter
import numpy as np
from sklearn.preprocessing import MinMaxScaler
from keras.models import Sequential
import pandas as pd
from keras.layers import Dense
from ast import main
from tkinter import *
from optparse import Values
layout= [



[sg.Text("Testing")],

[sg.Text("Gender")],

[sg.Input("")],

[sg.Text("Age")],

[sg.Input("")],

[sg.Text("Annual Salary")],

[sg.Input("")],

[sg.Text("credit card debt")],

[sg.Input("")],

[sg.Text("Net Worth")],

[sg.Input("")],

[sg.Button("Ok")],

[sg.Button("Cancel")]

]




window = sg.Window("Exam", layout)

while True:

    event, Values = window.read()

    if event == "Ok":

        print('Ok')

        userValues=Values

        break

    elif event == "Cancel" or event == sg.WIN_CLOSED:              

        break




window.close()
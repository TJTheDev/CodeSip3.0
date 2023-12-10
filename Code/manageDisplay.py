# -*- coding: utf-8 -*-
"""
Spyder Editor

author - Richard Richardson

This is a file to define the class for managing the scoreboard display.
"""

import tkinter as tk
from tkinter import *
from tkinter import ttk
import dataTypes
import importData


class ManageScoreboard():
    def __init__(self):
        
        #Create an instance of the scoreboard object and list of display objects
        self.scoreboard = dataTypes.scoreboard()
        
    def createMainWindow(self):
        #Configure the root window of the scoreboard. When using tk package every display has to be contained within a main window
        self.mainWindow = tk.Tk()
        
        #Set the title of the main window
        self.mainWindow.title("Code Sip Repeat - Live Interactive Scoreboard")

        self.mainWindow.geometry('780x340')

        self.mainWindow.configure(bg="silver")
        
    #Create a frame container to hold the display. This container resides within the main window
    def createFrame(self):
        self.frame = ttk.Frame(self.mainWindow)
        self.frame.pack(padx=10, pady=10)

    #Add scrollbar to right side of the frame    
    def addScrollbar(self):
        #Create a scrollbar for the display
        self.scrollbar = ttk.Scrollbar(self.frame)
        self.scrollbar.pack(side=RIGHT, fill=BOTH)
    
    #Add a drop down menu to select which sports scores to display
    def addDropDownMenu(self):
        self.variable = StringVar(self.frame)
        self.menu = ttk.OptionMenu(self.frame, self.variable, "Sports", "NFL", "NBA", "NCAAF", "NCAAB", "NHL")
        self.menu.pack()
    
    #Create the display area where the actual scores will be displayed
    def createDisplay(self):
        
        # Creating Treeview text widget. This is where the scores will be shown 
        self.display = ttk.Treeview(self.frame, 
                                    yscrollcommand=self.scrollbar.set,
                                    selectmode='none',
                                    show=["headings"],
                                    columns=("1", "2", "3", "4"),
                                    displaycolumns=("1", "2", "3", "4")) 

        self.scrollbar.config(command=self.display.yview)
        
        #Set column widths
        self.display.column("1", width=140, stretch=NO)
        self.display.column("2", width=40, stretch=NO)
        self.display.column("3", width=50, stretch=NO)
        self.display.column("4", width=60, stretch=NO)

        self.display.heading("1", text="Game")
        self.display.heading("2", text="Score")
        self.display.heading("3", text="Time")
        self.display.heading("4", text="Period")

        # Calling pack method w.r.to treeview
        self.display.pack(expand=True)
        
        style = ttk.Style()
        style.configure("Treeview", 
                        background="black",
                        foreground="white",
                        font=('Arial Bold', 10))
        

    #Start the main display and continue to update display based on timer
    def start(self):
        #Create the main window and the display area where the scores are displayed
        self.createMainWindow()
        self.createFrame()
        self.addScrollbar()
        self.addDropDownMenu()
        self.createDisplay()
        
        #Add the initial list of games
        self.update()
       
    #Get scores and refresh window every 10 seconds
    def update(self):
        #Get the current game data
        importData.populateScoreboard(self.scoreboard, self.variable.get())
        
        for i in self.display.get_children():
            self.display.delete(i)
            
        y = 0
        for i in self.scoreboard.games:
            self.display.insert('', y,values=(i.team1.name,  i.team1.score, i.time, i.period))
            self.display.insert('', y+1,values=(i.team2.name,  i.team2.score))
            self.display.insert('', y+2,values=("",  ""))
            
            #Move display pointer to next game location
            y += 3
        
        #Update display every 5 seconds
        self.display.after(500, self.update)




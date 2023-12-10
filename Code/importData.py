# -*- coding: utf-8 -*-
"""
Created on Sun Oct  1 20:59:50 2023

@author: - R. Richardson
"""

#This file is used to get the data for each game from a csv file
import csv
import dataTypes

def populateScoreboard(tempScoreboard, sport):
    
    match sport:
        case "NBA":
            dataFile = "nba_scores.csv"
        case "NFL":
            dataFile = "nfl_scores.csv"
        case "NCAAF":
            dataFile = "ncaaf_scores.csv"
        case _:
            dataFile = "Not Selected"
    
    if dataFile != "Not Selected":
        
        tempScoreboard.deleteGames()
        
        #Get the data for each game from the data source and add to the scoreboard
        with open(dataFile) as csv_file:
            #Return to top of csv file
            csv_file.seek(0)
        
            csv_reader = csv.reader(csv_file, delimiter=',')
        
            #Get all of the games from the data source and determine which games need to 
            #be shown. Add and remove games as dictated by the data source
            for row in csv_reader:
                newGame = dataTypes.game(row[1], row[3])
                newGame.updateScore(row[2], row[4])
                newGame.updateTime(row[5], row[6])

                #If this game is to be displayed then add it to the list of games
                if row[0] == "Y":
                
                    #Make sure it is not already in the list before adding
                    if tempScoreboard.findGame(newGame) is False:
                        tempScoreboard.addGame(newGame)
                    else:
                        tempScoreboard.updateGame(newGame)
                else:
                    #If the game is not be displayed then check to see if it is in the
                    #list and remove it
                    if tempScoreboard.findGame(newGame) is True:
                        tempScoreboard.removeGame(newGame)




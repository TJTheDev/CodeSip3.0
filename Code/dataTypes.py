# -*- coding: utf-8 -*-
"""
Created on Fri Sep 29 20:23:34 2023

@author: - R. Richardson
"""

#Create the data types for all of the objects to be used to create the scoreboard

#This datatype defines all of the data associated with a team
class team:
    def __init__(self, name, score):
        self.name = name
        self.score = score

#This datatype defines all the data required for a game       
class game:

    def __init__(self, name1, name2):
        self.team1 = team(name1, 0)
        self.team2 = team(name2, 0)
        self.period = ""
        self.time = ""

    #Method to update the score
    def updateScore(self, score1, score2):
        self.team1.score = score1
        self.team2.score = score2
    
    #Method to udate the time left in the game
    def updateTime(self, period, time):
        self.period = period
        self.time = time
        
    #Define a method to determine if 2 instances of this class object are equal
    def __eq__(self, other):
        if not isinstance(other, game):
            return NotImplemented
        
        #Returns true if the name of both teams are the same and false otherwise
        return self.team1.name == other.team1.name and self.team2.name == other.team2.name
    
#The scoreboard datatype contains a list of games and methods to update list       
class scoreboard:
    def __init__(self):
        self.games = []
    
    #Add a new game to the scoreboard object
    def addGame(self, match):
            self.games.append(match)

    #remove a game from the scoreboard
    def removeGame(self, match):
            self.games.remove(match)

    def getGame(self, i):
        return self.games[i]

    #Delete all of the games in the list
    def deleteGames(self):
        self.games.clear()
                
    #Update a game that is already in the list
    def updateGame(self, match):
        z = 0
        for i in self.games:
            if match == i:
                self.games[z] = match
            z += 1
    
    #Check to see if the game is already in the list
    def findGame(self, match):
        for i in self.games:
            if match == i:
                return True

        return False
    
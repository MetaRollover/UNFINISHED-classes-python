'''
This is a program I created, but never finished, as we were exploring
classes in Python, in my COP 1000 class. 

Created By: Austin Garrett (MetaRollover)
'''


#Common Properties and Methods

#Player Prop and Methods

#NPC Prop and Methods

#Enemy Prop and Methods

class Character():
    name = ""
    def PrintName(self):
        print(self.name)

class Player(Character):

    def __init__(self,n):
        self.name = n


class Enemy():

    def __init__(self,n):
        self.name = n

class RangedEnemy(Enemy):

    distance = 0

    def __init__(self,n,dist):
        Enemy.__init__(self,n)
        distance = dist


class NPC():
    pass

player = Player("Joe Link")
player.PrintName()

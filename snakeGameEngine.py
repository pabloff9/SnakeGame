#!/usr/bin/env python

import pygame, random
from pygame.locals import *

"""Constants"""
RIGHT, DOWN = 1, 2
LEFT, UP = 3, 4


class Food(object):
    
    def __init__(self, snake):
        
        self.snake = snake
        randomGenerator = random.Random()
        self.positionX = randomGenerator.randint(0, self.snake.boardSize - 1)
        self.positionY = randomGenerator.randint(0, self.snake.boardSize - 1)
        
        while ((self.positionX, self.positionY) in snake.body):
            self.positionX = randomGenerator.randint(0, self.snake.boardSize - 1)
            self.positionY = randomGenerator.randint(0, self.snake.boardSize - 1)
        
        self.lastPosition = (-30, -30) # Any position off-screen
        self.color = (255, 0, 0) # Hard coded a red color for the sake of simplicity
        
    def draw(self):
        
        squareWidth = self.snake.surface.get_width()//self.snake.boardSize
        rectangle = Rect(self.positionX*squareWidth, self.positionY*squareWidth, squareWidth, \
                             squareWidth)
        pygame.draw.rect(self.snake.surface, self.color, rectangle, 0)
        
        lastRectangle = Rect(self.lastPosition[0]*squareWidth, \
                             self.lastPosition[1]*squareWidth, \
                             squareWidth, squareWidth)
        
        pygame.draw.rect(self.snake.surface, (0, 0, 0), lastRectangle, 0)
        pygame.display.flip()
        
    def wasEaten(self):
        
        if ((self.positionX, self.positionY) == self.snake.head()):
            return True
        else:
            return False
    
    def erase(self):
        squareWidth = self.snake.surface.get_width()//self.snake.boardSize
        rectangle = Rect(self.positionX*squareWidth, self.positionY*squareWidth, squareWidth, \
                             squareWidth)
        pygame.draw.rect(self.snake.surface, (0, 0, 0), rectangle, 0)
    
class Snake(object):
    
    def __init__(self, surface, boardSize):
        
        self.body = [] # A queue will be kept for the body pieces of the snake
        self.body.append((0, 0))
        self.body.append((1, 0))
        self.body.append((2, 0))
        self.directionX = 1
        self.directionY = 0
        self.color = (255, 255, 255)
        self.surface = surface
        self.lastPreviouslyOccupiedPosition = (-1, 0)
        self.crashed = False
        self.willGrow = False
        self.boardSize = boardSize

        
    def draw(self):
        
        for positionX, positionY in self.body:
            squareWidth = self.surface.get_width()//self.boardSize
            rectangle = Rect(positionX*squareWidth, positionY*squareWidth, squareWidth, \
                             squareWidth)
            pygame.draw.rect(self.surface, self.color, rectangle, 0)
        
        lastRectangle = Rect(self.lastPreviouslyOccupiedPosition[0]*squareWidth, \
                             self.lastPreviouslyOccupiedPosition[1]*squareWidth, \
                             squareWidth, squareWidth)
        pygame.draw.rect(self.surface, (0, 0, 0), lastRectangle, 0)
                
        pygame.display.flip()
            
        
            
    def move(self):
        
        headX, headY = self.head()
        nextPosition = (headX + self.directionX, headY+ self.directionY)
        
        if (nextPosition in self.body or not 0 <= nextPosition[0] <= self.boardSize-1  \
                        or not 0 <= nextPosition[1] <= self.boardSize-1):
            self.crashed = True
        else:
            self.body.append(nextPosition)
            
            if (not self.willGrow):
                self.lastPreviouslyOccupiedPosition = self.body.pop(0)    
            else:
                self.willGrow = False       
        
        self.draw()
        
    def head(self):
        return self.body[-1]
        
            
    def grow(self):
        self.willGrow = True
        
            

#! /usr/bin/env python

from snakeGameEngine import *
from pygame.locals import *

if __name__ == "__main__":
    
    screenSize = 480
    backgroundColor = (0, 0, 0)
    screen = pygame.display.set_mode((screenSize, screenSize))
    screen.fill(backgroundColor)
    running = True
    clock = pygame.time.Clock()
    
    snake = Snake(screen, 15)
    food = Food(snake)
    
    while (running):
                
        if (snake.crashed):
            running = False
        
        events = pygame.event.get()
                
        for event in events:
            if (event.type == QUIT):
                running = False
            elif (event.type == KEYDOWN):
                if (event.key == K_RIGHT and snake.directionX != -1):
                    snake.directionX = 1
                    snake.directionY = 0
                elif (event.key == K_LEFT and snake.directionX != 1):
                    snake.directionX = -1
                    snake.directionY = 0
                elif (event.key == K_DOWN and snake.directionY != -1):
                    snake.directionY = 1
                    snake.directionX = 0
                elif (event.key == K_UP and snake.directionY != 1):
                    snake.directionY = -1
                    snake.directionX = 0
                    
        
        snake.draw()
        food.draw()    
        snake.move()
        
        if (food.wasEaten()):
            food.erase()
            food = Food(snake)
            snake.grow()
            
        clock.tick(7)
        
    
    

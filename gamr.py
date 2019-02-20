import pygame
import time
import random

pygame.init()

# screen intialization is here nigga

display_width = 800
display_height = 600

white = (255, 255,255)
d_white = (250, 250, 250)
black = (0, 0, 0)
teal = (0, 128, 128)
blue_black = (50, 50, 50)

game_display = pygame.display.set_mode((display_width, display_height))

factor = 10

clock = pygame.time.Clock()

#saap ka structure

class snakebody:

    def __init__(self, x, y):
        self.x, self.y = x, y


    def __repr__(self):
        return "snakebody({self.x}, {self.y})".format(self=self)

class Snake(list):
    def __init__(self, start_x, start_y, n):
        list.__init__(self, [snakebody(start_x, start_y + i * factor)
                             for i in range(n)])
        
    def move_head(self, dx, dy):
        self[0].x += dx
        self[0].y += dy

    def update(self, score):
        for i in range(len(self) -1, 0, -1):
            self[i].x = self[i-1].x
            self[i].y = self[i-1].y

    def check_death(self):
        if not (1 <= self[0].x <= display_width and 1 <= self[0].y <= display_height):
            return True
        return any(body_part.x == self[0].x and body_part.y == self[0].y for body_part in self[1:])

    def draw(self):
        for body_part in self:
            pygame.draw.rect(game_display, teal, 
                            (body_part.x, body_part.y, factor, factor))

#game logic


def main():
    food_x = random.randrange(5, display_width -5)
    food_y = random.randrange(5, display_height -5)
    print(food_x, food_y)
    score = 60
    
    snake = Snake(20, 20, 16)
    
    x = 0
    y = 0
    x_change = 0
    y_change = 0
    first_time = True
    eat = True

    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                first_time = False
                if event.key == pygame.K_a:
                    if x_change != 10:
                        x_change = -10
                        y_change = 0
                elif event.key == pygame.K_d:
                    if x_change != -10:
                        x_change = 10
                        y_change = 0
                elif event.key == pygame.K_w:
                    if y_change != 10:
                        x_change = 0
                        y_change = 10
                elif event.key == pygame.K_s:
                    if y_change != -10:
                        x_change = 0
                        y_change = -10
                elif event.key == pygame.K_c: 
                        x_change = 0
                        y_change = 0

                    
        if not first_time:
            snake.update(score)
        if score % 10 == 0 and eat:
            snake.append(snakebody(
                snake[len(snake) - 1].x, snake[len(snake) - 1].y))
            print(len(snake))
            eat = False
            snake.move_head(x_change, y_change) 
                        
        if snake[0].x < food_x +10 and snake[0].x > food_x -10 and snake[0].y < food_y +10 and snake[0].y > food_y -10:
                        score += 10
                        food_x = random.randrange(5, display_width -5)
                        food_y = random.randrange(5, display_height -5)
                        eat = True
        if snake.check_death():
                        pygame.quit()
                        quit()

        game_display.fill(white)

        pygame.draw.rect(game_display, black, (food_x, food_y, factor, factor))
        snake.draw()

        pygame.display.flip()
        time.sleep(0.035)
        clock.tick(60)

if __name__ == "__main__":
    main()

                        


                
            
                


    

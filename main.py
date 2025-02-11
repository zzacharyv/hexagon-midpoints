import pygame
import sys
import math
import random

def get_color(index):
    color = (255, 0, 0)
    if index == 0:
        color = (255, 0, 0)
    elif index == 1:
        color = (255, 255, 0)
    elif index == 2:
        color = (255, 0, 255)
    elif index == 3:
        color = (0, 0, 255)
    elif index == 4:
        color = (0, 255, 0)
    elif index == 5:
        color = (255, 255, 255)
    return color

def draw_midlines(screen, points, depth):
    midpoints = []
    for i in range(len(points)):
        j = i+1
        if j >= len(points): j = 0
        color = get_color(i)  
        pygame.draw.line(screen, color, (points[i][0],points[i][1]), (points[j][0],points[j][1]), 2)
        midpoints.append((((points[i][0] + points[j][0])/2), ((points[i][1] + points[j][1])/2)))
    if(depth < 6):
        draw_midpoints(screen, midpoints, depth+1)

def draw_midpoints(screen, points, depth):   
    line_points = []
    for i in range(len(points)):
        color = get_color(i)  
        pygame.draw.circle(screen, color,(points[i][0],points[i][1]),5)
    draw_midlines(screen, points, depth)

def draw_lines(screen, line_points):
    midpoints = []
    for i in range(len(line_points)):
        j = i+1
        if j >= len(line_points): j = 0
        color = get_color(i)  
        pygame.draw.line(screen, color, (line_points[i][0],line_points[i][1]), (line_points[j][0],line_points[j][1]), 3)
        midpoints.append((((line_points[i][0] + line_points[j][0])/2), ((line_points[i][1] + line_points[j][1])/2)))
    draw_midpoints(screen,midpoints,1)

def draw_points(screen, points, thetas, radius):  
    line_points = []
    for i in range(len(points)):
        cx = points[i][0]
        cy = points[i][1]
        theta = math.pi * thetas[i] / 180   
        x = cx + radius * math.cos(theta)
        y = cy - radius * math.sin(theta)
        color = get_color(i)    
        pygame.draw.circle(screen, color, (x,y), 10)
        line_points.append((int(x),int(y)))
    draw_lines(screen, line_points)

def main():
    # Initialize Pygame
    pygame.init()

    # Set up the display
    screen = pygame.display.set_mode((800,800))
    pygame.display.set_caption("approaching a regular polygon")
    points = [(273, 181),(527, 181),(654, 400),(527, 619),(273, 619),(146, 400)]
    thetas = [random.randint(0,360),random.randint(0,360),random.randint(0,360),random.randint(0,360),random.randint(0,360),random.randint(0,360)]
    radius = 80

    # Main loop
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Fill the screen with a color (RGB)
        screen.fill((0, 128, 255))

        # Draw a circle (surface, color, center, radius)
        pygame.draw.circle(screen, (255, 0, 0), (273, 181), radius, 5)
        pygame.draw.circle(screen, (255, 255, 0), (527, 181), radius, 5)
        pygame.draw.circle(screen, (255, 0, 255), (654, 400), radius, 5)
        pygame.draw.circle(screen, (0, 0, 255), (527, 619), radius, 5)
        pygame.draw.circle(screen, (0, 255, 0), (273, 619), radius, 5)
        pygame.draw.circle(screen, (255, 255, 255), (146, 400), radius, 5)
      
        draw_points(screen, points, thetas, radius)

        # Update the display
        pygame.display.flip()
        pygame.time.wait(15)
        for i in range(len(thetas)):
            thetas[i] += 1

    # Quit Pygame
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()

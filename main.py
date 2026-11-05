import pygame
import conway


screen_width = 631
screen_height = 631
square_size = 10
grid_width = 1
grid_color = (75,75,75)
square_color = (255,255,255)


rows = int((screen_height - grid_width)/(square_size + grid_width))
cols = int((screen_width - grid_width)/(square_size + grid_width))


automata = conway.Conway(rows, cols)
#automata.initGlider(5, 5)
automata.initRandom()

pygame.init()

screen = pygame.display.set_mode((screen_width,screen_height))
clock = pygame.time.Clock()

player_pos = pygame.Vector2(screen_width/2, screen_height/2)

delta_time = 0.1

running = True
pause = False
count = 0
while running:

    screen.fill((0,0,0,0))
    pygame.draw.circle(screen, "red", player_pos, 40)
    s = square_size + grid_width
    for i in range(rows+1):
        for j in range(cols+1):
            pygame.draw.line(screen, grid_color, (s*j,0), (s*j,screen_height), 1)
            if i == rows or j == cols:
                continue
            elif automata.grid[i][j][automata.current] == 1:
                pygame.draw.rect(screen, square_color, pygame.Rect((s*j+1, s*i+1), (square_size, square_size)), 0)
        pygame.draw.line(screen, grid_color, (0,s*i), (screen_width,s*i), 1)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                mouse_x, mouse_y = event.pos
                col = (mouse_x - grid_width)//(square_size + grid_width)
                row = (mouse_y - grid_width)//(square_size + grid_width)
                automata.grid[row][col][automata.current] = 1  
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                pause = not pause
            elif event.key == pygame.K_ESCAPE:
                running = False 

    keys = pygame.key.get_pressed()

    if keys[pygame.K_w]:
        player_pos.y -= 300 * delta_time
    if keys[pygame.K_s]:
        player_pos.y += 300 * delta_time
    if keys[pygame.K_a]:
        player_pos.x -= 300 * delta_time
    if keys[pygame.K_d]:
        player_pos.x += 300 * delta_time

    pygame.display.flip()
    if not pause:
        count += 1
        if (count % 6 == 0):
            automata.updateGrid()
    delta_time = clock.tick(60)/1000
    delta_time = max(0.001, min(0.1, delta_time))

pygame.quit()





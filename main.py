import pygame
import sys

pygame.init()

#ekranı ayarlıyoruz
WIDTH = 800
HEIGHT = 600

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Physics Engine V1.0")

clock = pygame.time.Clock()

#topumuzu tanımlıyoruz x ve y değerlerini başlangıç için veriyoruz
ball_x = WIDTH // 2
ball_y = 100

radius = 20
# yer çekimi,ivme değerlerini veriyoruz
velocity_y = 0
gravity = 0.5
bounce = 0.8

ground = 500

running = True

while running:

   
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # asıl 
    velocity_y += gravity
    ball_y += velocity_y

    # Zemine çarptı mı?
    if ball_y + radius >= ground:
        ball_y = ground - radius
        velocity_y *= -bounce

        if abs(velocity_y) < 1:
            velocity_y = 0

    # -----------------------------
    # Çizim
    # -----------------------------
    screen.fill((30, 30, 30))

    pygame.draw.line(screen, (255, 255, 255), (0, ground), (WIDTH, ground), 4)

    pygame.draw.circle(
        screen,
        (255, 0, 0),
        (int(ball_x), int(ball_y)),
        radius
    )

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
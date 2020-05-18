import pygame
from helpers import rP, CircleIntersection
from colors import RED, GREEN, BLUE, PINK
from circle import Circle


def VoronoiBruteForce(ms, width, n):
    pygame.init()
    clock = pygame.time.Clock()
    SCREEN_SURFACE = pygame.display.set_mode((width, width))
    pygame.display.set_caption("Voronoi Algorithm")

    # Changing Variables
    RADIUS = 1

    # Lists to keep track of
    CIRCLES = []
    POINTINTERSECTIONS = []

    # Generate Origin Points data #
    originCir = rP(50, 550, n)

    # Create Circles with Origin Points
    for i in range(len(originCir)):
        origin = originCir[i]
        CIRCLES.append(Circle("c" + str(i), origin))

    # PyGame Start

    running = True
    while running:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Fill background
        SCREEN_SURFACE.fill((255, 255, 255))

        # Calculate Circle Intersections with each other
        for c1 in CIRCLES:
            pygame.draw.circle(SCREEN_SURFACE, (0, 0, 0, 0), c1.origin, RADIUS, 1)

            for c2 in CIRCLES:
                if c1 == c2:
                    continue

                # Calculate
                intInfo = CircleIntersection(c1, c2, RADIUS)
                # print(intInfo)

                for p in intInfo:
                    isPValid = True

                    for c in CIRCLES:

                        if c == c1 or c == c2:
                            continue
                        if c.PointIsInside(p[0], p[1], RADIUS):
                            isPValid = False

                    if isPValid:
                        POINTINTERSECTIONS.append(p)

        for INTPOINT in POINTINTERSECTIONS:
            pygame.draw.circle(SCREEN_SURFACE, RED, INTPOINT, 4)

        # Flip the display
        pygame.display.flip()
        RADIUS += 1
        clock.tick(ms)

        if RADIUS > 1000:
            break


start = VoronoiBruteForce(144, 1000, 10)
# pygame.quit()

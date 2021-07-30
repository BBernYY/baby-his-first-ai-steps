import pygame
pygame.init()
WX, WY = 900, 500
FPS = 60
WIN = pygame.display.set_mode((WX, WY))
BG = pygame.image.load(os.path.join("assets", "bg.png"))
VEL = 10
pygame.display.set_caption("Title")
gameIcon = pygame.image.load(os.path.join("assets", "icon.png"))
pygame.display.set_icon(gameIcon)
class character:
    FACTOR = 0.25
    WIDTH, HEIGHT = round(16 / FACTOR), round(16 / FACTOR)
    RECT = pygame.Rect(100, 300, WIDTH, HEIGHT)
    RAW = pygame.image.load(getpath(os.path.join("assets", "lvl" + str(LVL), "character.png")))
class draw:
    WINTYPE = "MENU"
    def GAME():
        WIN.blit(BG, (0, 0))
        pygame.display.update()
    def MENU():
        WIN.blit(BG, (0, 0))
        menufont = pygame.font.SysFont('couriernew', 50)
        WIN.blit(menufont.render("Title", False, (255, 255, 255)), (WX // 2 - 150, WY // 2 - 100))
        menufont = pygame.font.SysFont('couriernew', 20)
        WIN.blit(menufont.render("Press space to start", False, (255, 255, 255)), (WX // 2 - 125, WY // 2 + 200))
        pygame.display.update()
def keycheck():
    keys_pressed = pygame.key.get_pressed()
    if keys_pressed[pygame.K_a]:
        character.RECT.x -= VEL
    if keys_pressed[pygame.K_d]:
        character.RECT.x += VEL
    if keys_pressed[pygame.K_w]:
        character.RECT.y -= VEL
    if keys_pressed[pygame.K_s]:
        character.RECT.y += VEL
    if keys_pressed[pygame.K_SPACE] and draw.WINTYPE == "MENU":
        draw.WINTYPE = "GAME"
def init():
    clock = pygame.time.Clock()
    main = True
    while main:
        clock.tick(FPS)
        if draw.WINTYPE == "GAME":
            draw.GAME()
        else:
            draw.MENU()
        keycheck()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                main = False
    pygame.quit()
if __name__ == "__main__":
    init()
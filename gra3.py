import pygame
from random import randint

pygame.init()

window = pygame.display.set_mode((1200, 720))


class Player:
    def __init__(self):
        self.x_cord = 0  #wspolrzedna x
        self.y_cord = 360  #wspolrzedna y
        self.image = pygame.image.load("gracz.png")  #wczytuje grafike
        self.width = self.image.get_width()   #szerokosc
        self.height = self.image.get_height()  #wysokosc
        self.speed = 6 #predkosc
        self.hitbox = pygame.Rect(self.x_cord, self.y_cord, self.width, self.height)
    
    def tick(self, keys):  #wykonuje sie raz na powtorzenie petli
        if keys[pygame.K_w]:
            self.y_cord -= self.speed
        if keys[pygame.K_a]:
            self.x_cord -= self.speed
        if keys[pygame.K_d]:
            self.x_cord += self.speed
        if keys[pygame.K_s]:
            self.y_cord += self.speed

        self.hitbox = pygame.Rect(self.x_cord, self.y_cord, self.width, self.height)

    def draw(self):
        window.blit(self.image, (self.x_cord, self.y_cord))

class Tresure:
    def __init__(self):
        self.x_cord = randint(0, 1200)
        self.y_cord = randint(0, 720)
        self.image = pygame.image.load("skarb.png")
        self.width = self.image.get_width()   #szerokosc
        self.height = self.image.get_height()  #wysokosc
        self.hitbox = pygame.Rect(self.x_cord, self.y_cord, self.width, self.height)

    def tick(self):
        self.hitbox = pygame.Rect(self.x_cord, self.y_cord, self.width, self.height)
    
    def draw(self):
        window.blit(self.image, (self.x_cord, self.y_cord))


def main():
    run = True
    player = Player()
    clock = 0
    wynik = 0
    skarby = []
    background = pygame.image.load("gratlo.png")
    #tekst = pygame.font.Font.render(pygame.font.SysFont("Pagul", 50), "Score: ", True, (48,12,1))
    while run:
        clock += pygame.time.Clock().tick(60) / 1000 #maksymalnie 200 powtorzen na sekunde (200 fps)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  #gdy gracz zamknie okienko
                run = False
        keys = pygame.key.get_pressed()
        if clock >= 3:
            clock = 0
            Tresure()
            skarby.append(Tresure())

        player.tick(keys)
        for skarb in skarby:
            skarb.tick()

        score_text = pygame.font.Font.render(pygame.font.SysFont("Pagul", 50), f"Score: {wynik}", True, (48,12,1))


        for skarb in skarby:
            if player.hitbox.colliderect(skarb.hitbox):
                skarby.remove(skarb)
                wynik += 1

        window.blit(background,(0, 0))  #rysowanie tla
        window.blit(score_text,(400, 0))  #rysowanie tekstu
        player.draw()
        for skarb in skarby:
            skarb.draw()

        pygame.display.update()


    print(wynik)
        


if __name__ == "__main__":
    main()

from puzzleclass import *
from Stats.example_generator import *

import pygame
from pygame.locals import *
import random
import time
import math
import numpy as np

"""
A scriptet futatva elindul a jatek
A lépésekhez mind a billentyűzet nyilai, mind a mozgatni kívánt mezőre való kattintás lehetséges input
Az új gomb megnyomására egy új táblát kapunk véletlenszerűen
A megold gomb megnyomására az algoritmus kirakja a táblát
A visszaállít gomb megnyomására az általunk megtett lépéseket visszavonja és kezdhetjük újra ugyanazt a táblát
"""

# szín változók beállítása RGB kódjuk szerint
PIROS = (255, 0, 0)
FEHER = (255, 255, 255)
FEKETE = (0, 0, 0)
ZOLD = (0, 255, 0)

pygame.init()
ablak = pygame.display.set_mode((600, 600))
ablak.fill(FEKETE)
pygame.display.set_caption("15-ös tologatós játék")
font = pygame.font.Font(pygame.font.match_font('bitstreamverasans'), 35)
clock = pygame.time.Clock()


class Mezo(object):
    def __init__(self, szam, x, y):
        self.szam = szam
        self.x = x
        self.y = y
        self.szelesseg = 99
        self.magassag = 99

    def rajzol(self):
        pygame.draw.rect(ablak, PIROS, (self.x, self.y, self.szelesseg, self.magassag), 0)
        # téglalapot rajzol: az ablakra,szín, méretezés(honnan,mekkora), szegély
        szoveg = font.render(str(self.szam), True, FEHER)  # a saját számát kiírja (true-->lekerekített számok)
        szövegdoboz = szoveg.get_rect(center=((2 * self.x + self.szelesseg) / 2, (
                2 * self.y + self.magassag) / 2))  # középre rakja a szöveget a négyzeten belül
        ablak.blit(szoveg, szövegdoboz)  # a ablak-re kirajzolja a szögeget a szövegdobozba

    def mozgat(self, tavolsag):  # téglalap mozgatása
        hova_x = self.x + tavolsag[0]  # meddig kell mozgatni
        hova_y = self.y + tavolsag[1]

        while self.x != hova_x or self.y != hova_y:  # amíg nincs ott
            ablak.fill(FEHER, [self.x, self.y, 99, 99])  # a jelenlegi helyét fehérre kitöltjük
            self.x += int(tavolsag[0] / 20)  # odébbrakjuk, majd lerajzoljuk
            self.y += int(tavolsag[1] / 20)  # 20 jelentése, hogy 20 db képkockából áll össze a mozgás
            self.rajzol()
            pygame.display.update()
            # frissítjük a képernyőt
            clock.tick(240)

        for event in pygame.event.get(pygame.QUIT):
            pygame.quit()
        for event in pygame.event.get(pygame.KEYDOWN):
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
            pygame.event.post(event)


def lepesszamlalo(jelenlegilepeszam):
    szoveg = font.render(jelenlegilepeszam, True, FEHER)
    szövegdoboz = szoveg.get_rect(center=(299, 550))
    ablak.blit(szoveg, szövegdoboz)


def gratulacio(üres_x, üres_y):
    szoveg = font.render("Gratulálok! Megcsináltad!", True, ZOLD)
    szövegdoboz = szoveg.get_rect(center=(300, 300))
    ablak.blit(szoveg, szövegdoboz)
    tizenhatosmezo = Mezo(16, üres_x, üres_y)
    tizenhatosmezo.rajzol()
    pygame.display.update()


nyero_allas = [[100, 100, 1], [200, 100, 2], [300, 100, 3], [400, 100, 4], [100, 200, 5], [200, 200, 6], [300, 200, 7],
               [400, 200, 8], [100, 300, 9], [200, 300, 10], [300, 300, 11], [400, 300, 12], [100, 400, 13],
               [200, 400, 14], [300, 400, 15]]  # ha ezt az állást elérjük akkor nyertünk


def nyeroallas(allas):
    for mezo in allas:
        jelenlegi_allas = [mezo.x, mezo.y, mezo.szam]
        if jelenlegi_allas not in nyero_allas:
            return False
    return True


def megold(jelen_allas, allas, üres_x, üres_y):
    # jelen_allas 4x4 2dim numpy array
    jatek = TologatosJatek(jelen_allas)
    jatek.kirakas()
    lepessorozat = jatek.lepesek
    lepesszam = 0
    for i in lepessorozat:
        if i == 'le':
            xy_tavolsag = [0, -100]
        if i == 'fel':
            xy_tavolsag = [0, 100]
        if i == 'balra':
            xy_tavolsag = [100, 0]
        if i == 'jobbra':
            xy_tavolsag = [-100, 0]
        for mezo in allas:
            if mezo.x + xy_tavolsag[0] == üres_x and mezo.y + xy_tavolsag[1] == üres_y:
                lepesszam += 1
                üres_x = mezo.x
                üres_y = mezo.y
                mezo.mozgat(xy_tavolsag)
                break
        ablak.fill(FEKETE, [100, 515, 400, 85])
        lepesszamlalo("Lépések száma: " + str(lepesszam))
        if nyeroallas(allas) == True:
            gratulacio(400, 400)
        pygame.display.update()


def uj():  # létrehoz egy kezdőállást
    tabla = generate_start_position().copy()
    tabla = tabla.reshape(16).tolist()
    return tabla


def kezdjük(kezdoallas):
    allas = []
    lepesszam = 0
    index = 0
    pygame.draw.rect(ablak, FEHER, (98, 98, 404, 404))
    for y in range(100, 500, 100):
        for x in range(100, 500, 100):
            if index < 16:
                if kezdoallas[index] > 0:
                    mezoszam = kezdoallas[index]
                    ujmezo = Mezo(mezoszam, x, y)
                    allas.append(ujmezo)
                    ujmezo.rajzol()
                    index += 1
                else:
                    üres_x = x
                    üres_y = y
                    index += 1
    # visszaállít gomb
    pygame.draw.rect(ablak, FEHER, (25, 20, 150, 60), 2)
    szoveg = font.render("Visszaállít", True, FEHER)
    szövegdoboz = szoveg.get_rect(center=(100, 50))
    ablak.blit(szoveg, szövegdoboz)

    # megold gomb
    pygame.draw.rect(ablak, FEHER, (250, 20, 100, 60), 2)
    szoveg = font.render("Megold", True, FEHER)
    szövegdoboz = szoveg.get_rect(center=(300, 50))
    ablak.blit(szoveg, szövegdoboz)

    # uj gomb
    pygame.draw.rect(ablak, FEHER, (450, 20, 100, 60), 2)
    szoveg = font.render("Új", True, FEHER)
    szövegdoboz = szoveg.get_rect(center=(500, 50))
    ablak.blit(szoveg, szövegdoboz)

    pygame.display.update()
    fut = True
    while fut:
        for event in pygame.event.get():
            felulir = True
            if event.type == QUIT:
                fut = False
                pygame.quit()
            elif event.type == MOUSEBUTTONDOWN:
                pozicio = pygame.mouse.get_pos()
                if 20 <= pozicio[1] <= 80:
                    if 25 <= pozicio[0] <= 175:
                        kezdjük(kezdoallas)
                    if 250 <= pozicio[0] <= 350:
                        jelen_allas = np.zeros((4, 4))
                        for mezo in allas:
                            jelen_allas[int((mezo.y) / 100 - 1)][int((mezo.x) / 100 - 1)] = mezo.szam
                        megold(jelen_allas, allas, üres_x, üres_y)
                        felulir = False
                    if 450 <= pozicio[0] < 550:
                        kezdjük(uj())

                x = int(math.floor(pozicio[0] / 100.0)) * 100
                y = int(math.floor(pozicio[1] / 100.0)) * 100

                xy_tavolsag = [(üres_x - x), (üres_y - y)]
                if 0 in xy_tavolsag and (
                        100 in xy_tavolsag or -100 in xy_tavolsag):  # megnézem, hogy az üres melletti mezőre kattintottak-e
                    for mezo in allas:
                        if mezo.x == x and mezo.y == y:
                            lepesszam += 1
                            üres_x = mezo.x
                            üres_y = mezo.y
                            mezo.mozgat(xy_tavolsag)
                            if nyeroallas(allas) == True:
                                gratulacio(400, 400)

            elif event.type == KEYDOWN:
                nyilak = [K_LEFT, K_RIGHT, K_UP, K_DOWN]
                if event.key == K_ESCAPE:
                    fut = False
                    pygame.quit()
                elif event.key in nyilak:
                    xy_tavolsag = [None, None]

                    if event.key == K_LEFT:
                        xy_tavolsag = [-100, 0]
                    if event.key == K_RIGHT:
                        xy_tavolsag = [100, 0]
                    if event.key == K_UP:
                        xy_tavolsag = [0, -100]
                    if event.key == K_DOWN:
                        xy_tavolsag = [0, 100]

                    for mezo in allas:
                        if mezo.x + xy_tavolsag[0] == üres_x and mezo.y + xy_tavolsag[1] == üres_y:
                            lepesszam += 1
                            üres_x = mezo.x
                            üres_y = mezo.y
                            mezo.mozgat(xy_tavolsag)
                            if nyeroallas(allas) == True:
                                gratulacio(400, 400)

                            break
            if fut != False:
                ablak.fill(FEKETE, [100, 520, 400, 60])
                if felulir:
                    lepesszamlalo("Lépéseid száma: " + str(lepesszam))
                pygame.display.update()
                clock.tick(60)


pygame.draw.rect(ablak, FEHER, (200, 250, 200, 100))
szoveg = font.render("Kezdjük", True, FEKETE)
szövegdoboz = szoveg.get_rect(center=(300, 300))
ablak.blit(szoveg, szövegdoboz)
pygame.display.update()

fut = True
while fut:
    for event in pygame.event.get():
        if event.type == QUIT:
            fut = False
            pygame.quit()

        elif event.type == MOUSEBUTTONDOWN:
            pozicio = pygame.mouse.get_pos()
            if ((200 <= pozicio[0] <= 400) & (250 <= pozicio[1] <= 350)):
                kezdjük(uj())

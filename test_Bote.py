import unittest
import pygame
from Bote import *


pygame.init()


ancho = 1280
altura = 650
ventana = pygame.display.set_mode((ancho, altura))
pacifico1Img = pygame.image.load('imagenes/pacifico1.png')
verdugo1Img = pygame.image.load('imagenes/verdugo1.png')


class TestBote(unittest.TestCase):

    print("--------tests valores de resultado conocido-----------")

    def test_BoteEnX_with_three_positives(self):
        self.assertEqual(Bote(157, 478, 2, pacifico1Img,
                              verdugo1Img, ventana).x, 157)
        self.assertEqual(Bote(1, 478, 2, pacifico1Img,
                              verdugo1Img, ventana).x, 1)
        self.assertEqual(Bote(123456987965465432132138464831381384313546384344648646, 478, 2, pacifico1Img,
                              verdugo1Img, ventana).x, 123456987965465432132138464831381384313546384344648646)

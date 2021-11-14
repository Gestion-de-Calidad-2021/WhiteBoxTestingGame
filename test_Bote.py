import unittest
import pygame
from Bote import *


pygame.init()


ancho = 1280
altura = 650
ventana = pygame.display.set_mode((ancho, altura))
pacifico1Img = pygame.image.load('imagenes/pacifico1.png')
verdugo1Img = pygame.image.load('imagenes/verdugo1.png')

bote=Bote(157, 478, 2, pacifico1Img,verdugo1Img, ventana)
class TestBoteCtr(unittest.TestCase):

    def test_BoteEnX_with_three_positives(self):
        self.assertEqual(Bote(157, 478, 2, pacifico1Img,
                              verdugo1Img, ventana).x, 157)
        self.assertEqual(Bote(1, 478, 2, pacifico1Img,
                              verdugo1Img, ventana).x, 1)
        self.assertEqual(Bote(123456987965465432132138464831381384313546384344648646, 478, 2, pacifico1Img,
                              verdugo1Img, ventana).x, 123456987965465432132138464831381384313546384344648646)
    def test_BoteEnY_with_three_positives(self):
        self.assertEqual(Bote(1, 1, 2, pacifico1Img,
                              verdugo1Img, ventana).y, 1)
        self.assertEqual(Bote(1, 478, 2, pacifico1Img,
                              verdugo1Img, ventana).y, 478)
        self.assertEqual(Bote(1, 123456987965465432132138464831381384313546384344648646, 2, pacifico1Img,
                              verdugo1Img, ventana).y, 123456987965465432132138464831381384313546384344648646)
    
    def test_BoteEnPos(self):
        self.assertEqual(Bote(1, 1, 4, pacifico1Img,
                            verdugo1Img, ventana).pos, 4)
    def test_Bote_imagen1(self):
        self.assertEqual(Bote(1, 1, 2, pacifico1Img,
                            verdugo1Img, ventana).imagen1, pacifico1Img)
       
    def test_Bote_imagen2(self):
        self.assertEqual(Bote(1, 1, 2, pacifico1Img,
                            verdugo1Img, ventana).imagen2, verdugo1Img)
    
    
class TestBoteMover(unittest.TestCase):
    def test_mover_1_if(self):
        self.assertEqual(Bote(157, 478, 2, pacifico1Img,verdugo1Img, ventana).mover(10,10,'M'),bote.mover(10,10,'M'))
    def test_mover_2_if(self):
        self.assertEqual(Bote(157, 478, 3, pacifico1Img,verdugo1Img, ventana).mover(10,10,'C'),bote.mover(10,10,'C'))
    def test_mover_3_if(self):
        self.assertEqual(Bote(157, 478, 4, pacifico1Img,verdugo1Img, ventana).mover(10,10,'M'),bote.mover(10,10,'M'))
    def test_mover_4_if(self):
        self.assertEqual(Bote(157, 478, 5, pacifico1Img,verdugo1Img, ventana).mover(10,10,'C'),bote.mover(10,10,'C'))
    def test_mover_5_if(self):
        self.assertEqual(Bote(157, 478, 2, pacifico1Img,verdugo1Img, ventana).mover(10,10,'H'),bote.mover(10,10,'H'))
    def test_mover_6_if(self):
        self.assertEqual(Bote(157, 478, 4, pacifico1Img,verdugo1Img, ventana).mover(10,10,'H'),bote.mover(10,10,'H'))
    bote.pos=10
    def test_mover_7_if(self):
        self.assertEqual(Bote(157, 478, 10, pacifico1Img,verdugo1Img, ventana).mover(10,10,'C'),bote.mover(10,10,'C'))

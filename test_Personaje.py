import unittest
import pygame
from Personaje import *

pygame.init()
ancho = 1280
altura = 650
ventana = pygame.display.set_mode((ancho, altura))
pacificoImg = pygame.image.load('imagenes/pacifico.png')
pacifico1Img = pygame.image.load('imagenes/pacifico1.png')
verdugo1Img = pygame.image.load('imagenes/verdugo1.png')

personaje_test = Personaje(135, 100, 0, 0, 'P', 'izquierda', pacificoImg, pacifico1Img, ventana)

class TestPersonaje(unittest.TestCase):
    def test_builder_positionX(self):
        self.assertEqual(Personaje(135, 100, 0, 0, 'P', 'izquierda', pacificoImg, pacifico1Img, ventana).x, 135)
        self.assertEqual(Personaje(0, 100, 0, 0, 'P', 'izquierda', pacificoImg, pacifico1Img, ventana).x, 0)
        self.assertEqual(Personaje(-10, 100, 0, 0, 'P', 'izquierda', pacificoImg, pacifico1Img, ventana).x, -10)

    def test_builder_positionY(self):
        self.assertEqual(Personaje(135, 100, 0, 0, 'P', 'izquierda', pacificoImg, pacifico1Img, ventana).y, 100)
        self.assertEqual(Personaje(135, 0, 0, 0, 'P', 'izquierda', pacificoImg, pacifico1Img, ventana).y, 0)
        self.assertEqual(Personaje(135, -100, 0, 0, 'P', 'izquierda', pacificoImg, pacifico1Img, ventana).y, -100)

    def test_mostrar_personaje(self):
        self.assertEqual(Personaje(135, 100, 0, 0, 'P', 'izquierda', pacificoImg, pacifico1Img, ventana).mostrar(), personaje_test.mostrar())

    def test_mover_personaje(self):
        self.assertEqual(Personaje(135, 100, 0, 0, 'P', 'izquierda', pacificoImg, pacifico1Img, ventana).mover(), personaje_test.mover())

#if __name__ == '__main__':
#    unittest.main()
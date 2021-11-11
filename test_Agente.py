import unittest
from Agente import Agente
import pytest

from copy import deepcopy
from time import time
import sys
"""
setTecnica
setEstadoInicial
setEstadoMeta
testObjetivo
generaHijos
busqueda_profundidad
 """
agente = Agente()
pafi, verdug, bt = 3, 3, 1  # Indica 3 verdugos, 3 pacificos en orilla izquierda
# indica estado en orilla izquierda (numero de pacificos y verdugos)
estado = [pafi, verdug, bt]

# agente.setEstadoMeta((0, 0, 0, 3, 3))
#print(agente.estadoMeta[0][0]) Bug NO SE PUEDE ITERAR UN OBJETO 'int' 

agente.setEstadoInicial(
            (estado[0], estado[1], estado[2], 3-estado[0], 3-estado[1]))
inicial=agente.estadoInicial
frontera = [[inicial]]
print(frontera)
print(type(frontera))
tam = 0
tam = max(sys.getsizeof(frontera), tam)
print('tamanio memoria:',tam)

camino = frontera.pop()
print(camino)
print(type(camino))

nodo = camino[-1]
print(nodo)

""" agente.generaHijos(nodo) """

print(agente.generaHijos(nodo))

class TestAgente(unittest.TestCase):
    def test_set_tecnica(self):
        agente.setTecnica("profundidad")
        self.assertEqual(agente.tecnica, "profundidad")

    def test_set_Estado_Inicial(self):
        agente.setEstadoInicial(
            (estado[0], estado[1], estado[2], 3-estado[0], 3-estado[1]))
        self.assertEqual(agente.estadoInicial, (3, 3, 1, 0, 0))

    def test_set_Estado_Meta(self):
        agente.setEstadoMeta((0, 0, 0, 3, 3))
        self.assertEqual(agente.estadoMeta, (0, 0, 0, 3, 3))

    """ def test_test_Objetivo(self):
        agente.testObjetivo() """
    
    def test_genera_Hijos(self):
        self.assertEqual(agente.generaHijos(nodo),
        [(2, 2, 0, 1, 1, 'Mover 1 Nativo (Mapuche) y 1 Verdugo a la derecha'), (3, 3, 1, 0, 0), (3, 1, 0, 0, 2, 'Mover 2 Verdugos a la derecha'), (3, 3, 1, 0, 0), (3, 2, 0, 0, 1, 'Mover 1 Verdugo a la derecha')])
        

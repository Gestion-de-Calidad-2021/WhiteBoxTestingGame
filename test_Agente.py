import unittest
from Agente import Agente

class TestAgente(unittest.TestCase):
    def test_costructor(self):
    
        pafi, verdug, bt = 3, 3, 1  # Indica 3 verdugos, 3 pacificos en orilla izquierda
        estado = [pafi, verdug, bt] # indica estado en orilla izquierda (numero de pacificos y verdugos)
 
        agenteTest=Agente()
        agenteTest.setEstadoInicial((estado[0], estado[1], estado[2], 3-estado[0], 3-estado[1]))
        self.assertEqual(agenteTest.estadoInicial, (3, 3, 1, 0, 0))

    def test_moverMV(self):
        agenteTest=Agente()
        self.assertEqual(agenteTest.moverMV((3,3,1,0,0)), (2, 2, 0, 1, 1, 'Mover 1 Nativo (Mapuche) y 1 Verdugo a la derecha'))
        self.assertEqual(agenteTest.moverMV((1,1,0,2,2)), (2, 2, 1, 1, 1, 'Mover 1 Nativo (Mapuche) y 1 Verdugo a la izquierda'))
        self.assertEqual(agenteTest.moverMV((3,1,0,0,2)), (3, 1, 0, 0, 2))
        self.assertEqual(agenteTest.moverMV((2,1,1,1,2)), (2, 1, 1, 1, 2))
    
    def test_moverMM(self):
        agenteTest=Agente()
        self.assertEqual(agenteTest.moverMM((2,2,1,1,1)), (0, 2, 0, 3, 1, 'Mover 2 Nativos (Mapuches) a la derecha'))
        self.assertEqual(agenteTest.moverMM((1,1,0,2,2)), (3, 1, 1, 0, 2, 'Mover 2 Nativos (Mapuches) a la izquierda'))
        self.assertEqual(agenteTest.moverMM((3,3,1,0,0)), (3, 3, 1, 0, 0))
        self.assertEqual(agenteTest.moverMM((3,3,0,0,0)), (3, 3, 0, 0, 0))

    def test_moverVV(self):
        agenteTest=Agente()
        self.assertEqual(agenteTest.moverVV((3,3,1,0,0)),(3, 1, 0, 0, 2, 'Mover 2 Verdugos a la derecha'))
        self.assertEqual(agenteTest.moverVV((3,1,0,0,2)),(3, 3, 1, 0, 0, 'Mover 2 Verdugos a la izquierda'))
        self.assertEqual(agenteTest.moverVV((1,1,1,2,2)),(1, 1, 1, 2, 2))
        self.assertEqual(agenteTest.moverVV((1,1,0,2,2)),(1, 1, 0, 2, 2))
    
    def test_moverM(self):
        agenteTest=Agente()
        self.assertEqual(agenteTest.moverM((1,1,1,2,2)), (0, 1, 0, 3, 2, 'Mover 1 Nativo (Mapuche) a la derecha'))
        self.assertEqual(agenteTest.moverM((2,2,0,1,1)), (3, 2, 1, 0, 1, 'Mover 1 Nativo (Mapuche) a la izquierda'))
        self.assertEqual(agenteTest.moverM((3,3,1,0,0)), (3, 3, 1, 0, 0))
        self.assertEqual(agenteTest.moverM((1,1,0,2,2)), (1, 1, 0, 2, 2))
    
    def test_moverV(self):
        agenteTest=Agente()
        self.assertEqual(agenteTest.moverV((3,3,1,0,0)), (3, 2, 0, 0, 1, 'Mover 1 Verdugo a la derecha'))
        self.assertEqual(agenteTest.moverV((2,1,0,1,2)), (2, 2, 1, 1, 1, 'Mover 1 Verdugo a la izquierda'))
        self.assertEqual(agenteTest.moverV((2,2,1,1,1)), (2, 2, 1, 1, 1))
        self.assertEqual(agenteTest.moverV((2,2,0,1,1)), (2, 2, 0, 1, 1))

    def test_esValido(self):
        agenteTest=Agente()
        self.assertEqual(agenteTest.esValido((4,4,1,-1,-1)), False)
        self.assertEqual(agenteTest.esValido((3,3,1,0,0)), True)
        self.assertEqual(agenteTest.esValido((2,1,1,1,2)), False)
        self.assertEqual(agenteTest.esValido((3,0,1,0,3)), True)
        self.assertEqual(agenteTest.esValido((1,2,1,2,1)), False)
        self.assertEqual(agenteTest.esValido((0,3,1,3,0)), True)

    def test_set_tecnica(self):
        agente = Agente()
        agente.setTecnica("profundidad")
        self.assertEqual(agente.tecnica, "profundidad")

    def test_set_Estado_Inicial(self):
        agente = Agente()
        pafi, verdug, bt = 3, 3, 1  # Indica 3 verdugos, 3 pacificos en orilla izquierda
        estado = [pafi, verdug, bt] # indica estado en orilla izquierda (numero de pacificos y verdugos)
        agente.setEstadoInicial(
            (estado[0], estado[1], estado[2], 3-estado[0], 3-estado[1]))
        self.assertEqual(agente.estadoInicial, (3, 3, 1, 0, 0))

    def test_set_Estado_Meta(self):
        agente = Agente()
        agente.setEstadoMeta((0, 0, 0, 3, 3))
        self.assertEqual(agente.estadoMeta, (0, 0, 0, 3, 3))

    def test_test_Objetivo(self):
        agente = Agente()
        pafi, verdug, bt = 3, 3, 1  # Indica 3 verdugos, 3 pacificos en orilla izquierda
        estado = [pafi, verdug, bt] # indica estado en orilla izquierda (numero de pacificos y verdugos)
        agente.setEstadoInicial(
        (estado[0], estado[1], estado[2], 3-estado[0], 3-estado[1]))
        inicial = agente.estadoInicial
        frontera = [[inicial]]
        camino = frontera.pop()
        nodo = camino[-1]
        self.assertEqual(agente.testObjetivo(nodo),(0, 0, 0, 3, 3))

    def test_genera_Hijos_Con_FuncionSucesor_Completo(self):
        agente = Agente()
        pafi, verdug, bt = 3, 3, 1  # Indica 3 verdugos, 3 pacificos en orilla izquierda
        estado = [pafi, verdug, bt] # indica estado en orilla izquierda (numero de pacificos y verdugos)
        agente.setEstadoInicial((estado[0], estado[1], estado[2], 3-estado[0], 3-estado[1]))
        inicial = agente.estadoInicial
        frontera = [[inicial]]
        camino = frontera.pop()
        nodo = camino[-1]
        self.assertEqual(agente.generaHijos(nodo),[(2, 2, 0, 1, 1, 'Mover 1 Nativo (Mapuche) y 1 Verdugo a la derecha'), (3, 3, 1, 0, 0), (3, 1, 0, 0, 2, 'Mover 2 Verdugos a la derecha'), (3, 3, 1, 0, 0), (3, 2, 0, 0, 1, 'Mover 1 Verdugo a la derecha')])

    def test_genera_Hijos_Con_FuncionSucesor_Vacio(self):
        agente = Agente()
        pafi, verdug, bt = 3, 3, 1  # Indica 3 verdugos, 3 pacificos en orilla izquierda
        estado = [pafi, verdug, bt] # indica estado en orilla izquierda (numero de pacificos y verdugos)
        agente.setEstadoInicial((estado[0], estado[1], estado[2], 3-estado[0], 3-estado[1]))
        inicial = agente.estadoInicial
        frontera = [[inicial]]
        camino = frontera.pop()
        nodo = camino[-1]
        agente.funcionSucesor=[]
        self.assertEqual(agente.generaHijos(nodo), [])

    def test_DFS_Nodo_Inicial_Vacio(self):
        agente = Agente()
        agente.setEstadoInicial(None)
        agente.setEstadoMeta((0, 0, 0, 3, 3))
        agente.setTecnica("profundidad")
        self.assertEqual(agente.busqueda_profundidad(
            agente.estadoInicial, agente.estadoMeta),None)

    def test_DFS_Nodo_Objetivo_Igual_A_Estado_Inicial(self):
        agente = Agente()
        pafi, verdug, bt = 3, 3, 1  # Indica 3 verdugos, 3 pacificos en orilla izquierda
        estado = [pafi, verdug, bt] # indica estado en orilla izquierda (numero de pacificos y verdugos)
        agente.setEstadoInicial((3-estado[0], 3-estado[1], 1-estado[2], estado[0], estado[1]))
        agente.setEstadoMeta((0, 0, 0, 3, 3))
        agente.setTecnica("profundidad")
        camino = agente.busqueda_profundidad(
            agente.estadoInicial, agente.estadoMeta)
        self.assertEqual(camino,[(0, 0, 0, 3, 3)])

    def test_DFS(self):
        agente = Agente()
        pafi, verdug, bt = 3, 3, 1  # Indica 3 verdugos, 3 pacificos en orilla izquierda
        estado = [pafi, verdug, bt] # indica estado en orilla izquierda (numero de pacificos y verdugos)
        agente.setEstadoInicial((estado[0], estado[1], estado[2], 3-estado[0], 3-estado[1]))
        print(agente.estadoInicial)
        agente.setEstadoMeta((0, 0, 0, 3, 3))
        print(agente.estadoMeta)
        print("TECNICA DE BÚSQUEDA:")
        agente.setTecnica("profundidad")
        print(agente.tecnica)
        camino = agente.busqueda_profundidad(
            agente.estadoInicial, agente.estadoMeta)
        self.assertEqual(camino, [(3, 3, 1, 0, 0), (3, 1, 0, 0, 2, 'Mover 2 Verdugos a la derecha'), (3, 2, 1, 0, 1, 'Mover 1 Verdugo a la izquierda'), (3, 0, 0, 0, 3, 'Mover 2 Verdugos a la derecha'), (3, 1, 1, 0, 2, 'Mover 1 Verdugo a la izquierda'), (1, 1, 0, 2, 2, 'Mover 2 Nativos (Mapuches) a la derecha'), (2, 2, 1, 1, 1,
                                                                                                                                                                                                                                                                                                                          'Mover 1 Nativo (Mapuche) y 1 Verdugo a la izquierda'), (0, 2, 0, 3, 1, 'Mover 2 Nativos (Mapuches) a la derecha'), (0, 3, 1, 3, 0, 'Mover 1 Verdugo a la izquierda'), (0, 1, 0, 3, 2, 'Mover 2 Verdugos a la derecha'), (0, 2, 1, 3, 1, 'Mover 1 Verdugo a la izquierda'), (0, 0, 0, 3, 3, 'Mover 2 Verdugos a la derecha'), (0, 0, 0, 3, 3)])

        
class TestAgente_Programa(unittest.TestCase):

    
    def test_programa_profundidad(self):    
        agente = Agente()
        pafi, verdug, bt = 3, 3, 1  # Indica 3 verdugos, 3 pacificos en orilla izquierda
        estado = [pafi, verdug, bt] # indica estado en orilla izquierda (numero de pacificos y verdugos)
        agente.setEstadoInicial((3-estado[0], 3-estado[1], 1-estado[2], estado[0], estado[1]))
        agente.setEstadoMeta((0, 0, 0, 3, 3))    
        agente.setTecnica("profundidad")
        self.assertEqual(agente.programa(),agente.busqueda_profundidad(agente.estadoInicial,agente.estadoMeta))
    def test_programa_amplitud(self):
        agente = Agente()
        pafi, verdug, bt = 3, 3, 1  # Indica 3 verdugos, 3 pacificos en orilla izquierda
        estado = [pafi, verdug, bt] # indica estado en orilla izquierda (numero de pacificos y verdugos)
        agente.setEstadoInicial((3-estado[0], 3-estado[1], 1-estado[2], estado[0], estado[1]))
        agente.setEstadoMeta((0, 0, 0, 3, 3))  
        agente.setTecnica("amplitud")
        self.assertEqual(agente.programa(),agente.busqueda_amplitud(agente.estadoInicial,agente.estadoMeta))
    def test_programa_sin_tecnica(self):
        agente = Agente()
        pafi, verdug, bt = 3, 3, 1  # Indica 3 verdugos, 3 pacificos en orilla izquierda
        estado = [pafi, verdug, bt] # indica estado en orilla izquierda (numero de pacificos y verdugos)
        agente.setEstadoInicial((3-estado[0], 3-estado[1], 1-estado[2], estado[0], estado[1]))
        agente.setEstadoMeta((0, 0, 0, 3, 3))  
        agente.setTecnica("xxx")
        self.assertEqual(agente.programa(),"Configure la tecnica de busqueda.")
        
class TestAgente_BFS(unittest.TestCase):
    
    def test_programa_profundidad2(self):
        agente = Agente()
        pafi, verdug, bt = 3, 3, 1  # Indica 3 verdugos, 3 pacificos en orilla izquierda
        estado = [pafi, verdug, bt] # indica estado en orilla izquierda (numero de pacificos y verdugos)
        agente.setEstadoInicial((3-estado[0], 3-estado[1], 1-estado[2], estado[0], estado[1]))
        agente.setEstadoMeta((0, 0, 0, 3, 3))  
        agente.setTecnica("amplitud")
        agente.estadoInicial=(3, 3, 1, 0, 0)
        agente.setEstadoMeta((0,0,0,3,3))
        self.assertEqual(agente.busqueda_amplitud(agente.estadoInicial,agente.estadoMeta),[(3, 3, 1, 0, 0),
                                                                                   (2, 2, 0, 1, 1, 'Mover 1 Nativo (Mapuche) y 1 Verdugo a la derecha'),
                                                                                   (3, 2, 1, 0, 1, 'Mover 1 Nativo (Mapuche) a la izquierda'),
                                                                                   (3, 0, 0, 0, 3, 'Mover 2 Verdugos a la derecha'),
                                                                                   (3, 1, 1, 0, 2, 'Mover 1 Verdugo a la izquierda'),
                                                                                   (1, 1, 0, 2, 2, 'Mover 2 Nativos (Mapuches) a la derecha'),
                                                                                   (2, 2, 1, 1, 1, 'Mover 1 Nativo (Mapuche) y 1 Verdugo a la izquierda'),
                                                                                   (0, 2, 0, 3, 1, 'Mover 2 Nativos (Mapuches) a la derecha'),
                                                                                   (0, 3, 1, 3, 0, 'Mover 1 Verdugo a la izquierda'),
                                                                                   (0, 1, 0, 3, 2, 'Mover 2 Verdugos a la derecha'),
                                                                                   (1, 1, 1, 2, 2, 'Mover 1 Nativo (Mapuche) a la izquierda'),
                                                                                   (0, 0, 0, 3, 3, 'Mover 1 Nativo (Mapuche) y 1 Verdugo a la derecha'),
                                                                                   (0, 0, 0, 3, 3)]) 
        
    def test_programa_profundidad(self):
        agente = Agente()
        pafi, verdug, bt = 3, 3, 1  # Indica 3 verdugos, 3 pacificos en orilla izquierda
        estado = [pafi, verdug, bt] # indica estado en orilla izquierda (numero de pacificos y verdugos)
        agente.setEstadoInicial((3-estado[0], 3-estado[1], 1-estado[2], estado[0], estado[1]))
        agente.setEstadoMeta((0, 0, 0, 3, 3))  
        agente.setTecnica("amplitud")
        agente.estadoInicial=(0, 0, 0, 3, 3)
        agente.setEstadoMeta((0,0,0,3,3))
        self.assertEqual(agente.busqueda_amplitud(agente.estadoInicial,agente.estadoMeta),[(0, 0, 0, 3, 3)])
   
                         
from copy import deepcopy
from time import time
import sys
class Agente:
    def __init__(self):
        self.funcionSucesor = [self.moverMV, self.moverMM, self.moverVV, self.moverM, self.moverV]
        
    def moverMV(self, estado):
        estadoAux=(estado[0],estado[1],estado[2],estado[3],estado[4])
        if(estado[2]==0):
            estado=(estado[0]+1,estado[1]+1,1,estado[3]-1,estado[4]-1,"Mover 1 Nativo (Mapuche) y 1 Verdugo a la izquierda")
        elif(estado[2]==1):
            estado=(estado[0]-1,estado[1]-1,0,estado[3]+1,estado[4]+1,"Mover 1 Nativo (Mapuche) y 1 Verdugo a la derecha")
        if(self.esValido(estado)):
            return estado
        else: 
            return estadoAux
            
        
    def moverMM(self,estado):
        estadoAux=(estado[0],estado[1],estado[2],estado[3],estado[4])
        if(estado[2]==0):
            estado=(estado[0]+2,estado[1],1,estado[3]-2,estado[4],"Mover 2 Nativos (Mapuches) a la izquierda")
        elif(estado[2]==1):
            estado=(estado[0]-2,estado[1],0,estado[3]+2,estado[4],"Mover 2 Nativos (Mapuches) a la derecha")
        if(self.esValido(estado)):
            return estado
        else: 
            return estadoAux
        
    def moverVV(self,estado):
        estadoAux=(estado[0],estado[1],estado[2],estado[3],estado[4])
        if(estado[2]==0):
            estado=(estado[0],estado[1]+2,1,estado[3],estado[4]-2,"Mover 2 Verdugos a la izquierda")
        elif(estado[2]==1):
            estado=(estado[0],estado[1]-2,0,estado[3],estado[4]+2,"Mover 2 Verdugos a la derecha")
        if(self.esValido(estado)):
            return estado
        else: 
            return estadoAux
        
    def moverM(self,estado):
        estadoAux=(estado[0],estado[1],estado[2],estado[3],estado[4])
        if(estado[2]==0):
            estado=(estado[0]+1,estado[1],1,estado[3]-1,estado[4],"Mover 1 Nativo (Mapuche) a la izquierda")
        elif(estado[2]==1):
            estado=(estado[0]-1,estado[1],0,estado[3]+1,estado[4],"Mover 1 Nativo (Mapuche) a la derecha")
        if(self.esValido(estado)):
            return estado
        else: 
            return estadoAux
        
    def moverV(self,estado):
        estadoAux=(estado[0],estado[1],estado[2],estado[3],estado[4])
        if(estado[2]==0):
            estado=(estado[0],estado[1]+1,1,estado[3],estado[4]-1,"Mover 1 Verdugo a la izquierda")
        elif(estado[2]==1):
            estado=(estado[0],estado[1]-1,0,estado[3],estado[4]+1,"Mover 1 Verdugo a la derecha")
        if(self.esValido(estado)):
            return estado
        else: 
            return estadoAux
        
    def esValido(self, estado):
        resp=False
        if((estado[0]<=3 and estado[0]>=0)and(estado[1]<=3 and estado[1]>=0)and(estado[3]<=3 and estado[3]>=0)and(estado[4]<=3 and estado[4]>=0)):
            if(estado[3] >= estado[4]):
                resp = True
            else:
                if estado[3] == 0:
                    resp = True
                else:
                    return False
            
            if(estado[0] >= estado[1]):
                resp = True
            else:
                if estado[0] == 0:
                    resp = True
                else: 
                    return False
        return resp

    def setTecnica(self,t):
        self.tecnica = t

    def setEstadoInicial(self, e0):
        self.estadoInicial = e0

    def setEstadoMeta(self, ef):
        self.estadoMeta = ef

    def testObjetivo(self, nodo):
        return nodo[0][0] == self.estadoMeta[0][0]


    def generaHijos(self, nodo):
        lista=[]
        for metodo in self.funcionSucesor:
            aux = metodo(nodo)
            lista.append(aux)
        return lista
        
    def busqueda_profundidad(self,inicial, objetivo):
        inicio_tiempo = time()
        frontera = [[inicial]]
        tam = 0
        cont = 0
        visitados = []
        while frontera:
            tam = max(sys.getsizeof(frontera), tam)
            cont += 1
            camino = frontera.pop()
            nodo = camino[-1]
            if nodo == objetivo:
                fin_tiempo = time() - inicio_tiempo
                print("Algoritmo tardo: %0.10f segundos." % fin_tiempo)
                print("Maximo tamaño de frontera: ", tam, " bytes")
                print("Se preciso de ", cont, " iteraciones para encontrar la solucion")
                print("la solución tiene ", len(camino), " pasos")
                return camino
            else:
                for h in self.generaHijos(nodo):
                    aux = deepcopy(camino)
                    aux.append(h) 
                    if h not in visitados:
                        frontera.append(aux)
                        visitados.append(h)
                        
    def busqueda_amplitud(self,inicial, objetivo):
        inicio_tiempo = time()
        frontera = [[inicial]]
        tam = 0
        cont = 0
        visitados = []
        while frontera:
            tam = max(sys.getsizeof(frontera), tam)
            cont += 1
            camino = frontera.pop(0)
            nodo = camino[-1]

            if nodo == objetivo:
                fin_tiempo = time() - inicio_tiempo
                print("Algoritmo tardo: %0.10f segundos." % fin_tiempo)
                print("Maximo tamaño de frontera: ", tam, " bytes")
                print("Se preciso de ", cont, " iteraciones para encontrar la solucion")
                print("la solución tiene ", len(camino), " pasos")
                return camino
            else:
                for h in self.generaHijos(nodo):
                    aux = deepcopy(camino)
                    aux.append(h)
                    if h not in visitados:
                        frontera.append(aux)
                        visitados.append(h)
    
    def programa(self):
        if(self.tecnica=="profundidad"):
            print("estado inicial:",self.estadoInicial, "estado meta:",self.estadoMeta)
            return self.busqueda_profundidad(self.estadoInicial, self.estadoMeta)
           
            

        elif(self.tecnica=="amplitud"):
            print("estado inicial:",self.estadoInicial, "estado meta:",self.estadoMeta)
            return self.busqueda_amplitud(self.estadoInicial, self.estadoMeta)
            
        else:
            return "Configure la tecnica de busqueda."
    
        
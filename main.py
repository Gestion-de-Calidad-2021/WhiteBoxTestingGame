import pygame
from Personaje import Personaje
from Bote import Bote
from Agente import Agente
import time

pygame.init()
ancho = 1280
altura = 650
ventana = pygame.display.set_mode((ancho, altura))

# definimos nuestros colores rgb
negro = (0, 0, 0)
blanco = (255, 255, 255)
rojo = (255, 0, 0)
rojo_claro = (226, 110, 110)

# cargamos imagenes
boteImg = pygame.image.load('imagenes/bote.png')
fondoImg = pygame.image.load('imagenes/fondo.png')
pacificoImg = pygame.image.load('imagenes/pacifico.png')
pacifico1Img = pygame.image.load('imagenes/pacifico1.png')
verdugoImg = pygame.image.load('imagenes/verdugo.png')
verdugo1Img = pygame.image.load('imagenes/verdugo1.png')
nuevoImg = pygame.image.load('imagenes/nuevo.png')
nuevo1Img = pygame.image.load('imagenes/nuevo1.png')
finImg = pygame.image.load('imagenes/fin.png')
victoriaImg = pygame.image.load('imagenes/victoria.png')
goImg = pygame.image.load('imagenes/go.png')
go1Img = pygame.image.load('imagenes/go1.png')
sonidoOnImg = pygame.image.load('imagenes/sonidoon.png')
sonidoOffImg = pygame.image.load('imagenes/sonidooff.png')
ayudaImg= pygame.image.load('imagenes/help.png')
ayudaImg2 = pygame.image.load('imagenes/help2.png')
# cargamos sonido
snd_fin = pygame.mixer.Sound('sonido/sonido_fin.wav')
snd_victoria = pygame.mixer.Sound('sonido/sonido_ganador.wav')


font = pygame.font.SysFont(None, 25)


def main():
    x = (ancho * 0.1)
    y = (altura * 0.8)
    x_nuevo, y_nuevo = 0, 0

    personajes = []
    personajes.insert(0, Personaje(x - 135, y - 100, 0, 0, 'P', 'izquierda', pacificoImg, pacifico1Img, ventana))
    personajes.insert(1, Personaje(x - 90, y - 100, 0, 0, 'P', 'izquierda', pacificoImg, pacifico1Img, ventana))
    personajes.insert(2, Personaje(x - 45, y - 100, 0, 0, 'P', 'izquierda', pacificoImg, pacifico1Img, ventana))
    personajes.insert(3, Personaje(x - 135, y - 250, 0, 0, 'V', 'izquierda', verdugoImg, verdugo1Img, ventana))
    personajes.insert(4, Personaje(x - 90, y - 250, 0, 0, 'V', 'izquierda', verdugoImg, verdugo1Img, ventana))
    personajes.insert(5, Personaje(x - 45, y - 250, 0, 0, 'V', 'izquierda', verdugoImg, verdugo1Img, ventana))

    en_bote = []
    en_bote.insert(0, Bote(157, 478, 2, pacifico1Img, verdugo1Img, ventana))
    en_bote.insert(1, Bote(656, 478, 3, pacifico1Img, verdugo1Img, ventana))
    en_bote.insert(2, Bote(318, 478, 4, pacifico1Img, verdugo1Img, ventana))
    en_bote.insert(3, Bote(817, 478, 5, pacifico1Img, verdugo1Img, ventana))

    pygame.display.set_caption('Sistemas Inteligentes 1')

    clock = pygame.time.Clock()
    finalizado = False
    pos_bote = 0
    a, b = 0, 0
    accion = [a, b]  # numero de verdugos y pacificos a mover
    pafi, verdug, bt = 3, 3, 1  # Indica 3 verdugos, 3 pacificos en orilla izquierda
    estado = [pafi, verdug, bt]  # indica estado en orilla izquierda (numero de pacificos y verdugos)
    


    fin_juego = False
    fin_jugador, victoria_jugador = False, False
    izquierda, derecha = False, False
    victoria = False
    num_movida = 0

    # cargar sonido de fondo
    pygame.mixer.music.load('sonido/sonido_fondo.mp3')
    pygame.mixer.music.play(-1)
    sonido = True

    while not finalizado:
        # cargar imagenes de inicio
        ventana.blit(fondoImg, (0, 0))
        ventana.blit(nuevoImg, (1000, 45))
        ventana.blit(ayudaImg, (900, 45))
        msg_pista = font.render("Mantener Presionado para obtener ayuda", True, negro)
        ventana.blit(msg_pista, [900,130])
        
        # boton para habilitar sonido
        if sonido:
            ventana.blit(sonidoOnImg, (1150, 40))
        else:
            ventana.blit(sonidoOffImg, (1150, 40))

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                finalizado = True

        # cargar imagenes para los personajes (el vector de personajes)
        for i in range(6):
            personajes[i].mostrar()

    
        msg_estado = font.render("Estado: " + str(estado), True, negro)
        ventana.blit(msg_estado, [20, 20])
        msg_accion = font.render("Accion: " + str(accion), True, negro)
        ventana.blit(msg_accion, [20, 50])
        msg_movidas = font.render("Movidas: " + str(num_movida), True, negro)
        ventana.blit(msg_movidas, [20, 80])
        cursor = pygame.mouse.get_pos()

        
        if 1150 + 50 > cursor[0] > 1150 and 40 + 50 > cursor[1] > 40:
            if sonido:
                ventana.blit(sonidoOffImg, (1150, 40))
            else:
                ventana.blit(sonidoOnImg, (1150, 40))
            if pygame.mouse.get_pressed() == (1, 0, 0):
                if sonido:
                    sonido = False
                    pygame.mixer.music.pause()
                else:
                    sonido = True
                    pygame.mixer.music.play()

        
        if 1000 + 119 > cursor[0] > 1000 and 45 + 36 > cursor[1] > 45:
            ventana.blit(nuevo1Img, (1000, 20))
            if pygame.mouse.get_pressed() == (1, 0, 0):
                main()
                


        if 900 + 80 > cursor[0] > 900 and 45 + 90 > cursor[1] > 45:
            ventana.blit(ayudaImg2, (900, 45))
            if pygame.mouse.get_pressed() == (1, 0, 0):
                agente = Agente()
                print("Estado Actual: ",estado)
                print("prueba fuera del if")
                if(estado[2]==1):
                    agente.setEstadoInicial((estado[0],estado[1],estado[2],3-estado[0],3-estado[1]))
                    print(agente.estadoInicial)
                    agente.setEstadoMeta((0,0,0,3,3))
                    print(agente.estadoMeta)
                    print("TECNICA DE BÚSQUEDA:")
                    agente.setTecnica("profundidad")
                    print(agente.tecnica)
                    print()
                    print("EJECUTAR BUSQUEDA:",agente.tecnica)
                    lista=agente.programa()
                    for i in lista:
                        print("paso: ",i)
                    #ayuda 
                    msg_estado = font.render("PISTA: " + str(lista[1][5]), True, negro)
                    ventana.blit(msg_estado, [400, 10])
                    
                        
                    
                elif(estado[2]==0):
                    agente.setEstadoInicial((estado[0],estado[1],estado[2],3-estado[0],3-estado[1]))
                    print(agente.estadoInicial)
                    agente.setEstadoMeta((0,0,0,3,3))
                    print(agente.estadoMeta)
                    print("TECNICA DE BÚSQUEDA:")
                    agente.setTecnica("profundidad")
                    print(agente.tecnica)
                    print()
                    print("EJECUTAR BUSQUEDA:",agente.tecnica)
                    lista=agente.programa()
                    for i in lista:
                        print("paso: ",i)
                    #ayuda 
                    msg_estado = font.render("PISTA: " + str(lista[1][5]), True, negro)
                    ventana.blit(msg_estado, [400, 10])
            
                
                
        
        ventana.blit(boteImg, (x, y))

        
        if (estado[1] > estado[0] > 0) or  (estado[1] < estado[0] < 3):
            ventana.blit(finImg, (400, 250))
            fin_juego = True

        
        if estado == [0, 0, 0] and accion == [0, 0]:
            ventana.blit(victoriaImg, (400, 250))
            victoria = True

        if not fin_juego and not victoria:
            
            if 590+88 > cursor[0] > 590 and 300 + 90 > cursor[1] > 300 and accion != [0, 0]:
                ventana.blit(go1Img, (590, 300))
                if pygame.mouse.get_pressed() == (1, 0, 0):
                    if pos_bote == 0:
                        x_nuevo = 10
                        for i in range(6):
                            if personajes[i].pos == 2 or personajes[i].pos == 4:
                                personajes[i].x_mas = 10
                    else:
                        x_nuevo = -10
                        for i in range(6):
                            if personajes[i].pos == 3 or personajes[i].pos == 5:
                                personajes[i].x_mas = -10
            else:
                ventana.blit(goImg, (590, 300))

            
            if x >= 620 and pos_bote == 0:
                x_nuevo = 0
                for i in range(6):
                    personajes[i].x_mas = 0
                pos_bote = 1
                num_movida += 1
                estado[0], estado[1], estado[2] = estado[0] - accion[0], estado[1] - accion[1], 0
                for i in range(6):
                    if personajes[i].pos == 2:
                        personajes[i].pos = 3
                        personajes[i].izq_der = 'derecha'
                        personajes[i].rect_x += 900
                    if personajes[i].pos == 4:
                        personajes[i].pos = 5
                        personajes[i].izq_der = 'derecha'
                        personajes[i].rect_x += 900
            if x <= 128 and pos_bote == 1:
                x_nuevo = 0
                for i in range(6):
                    personajes[i].x_mas = 0
                pos_bote = 0
                num_movida += 1
                estado[0], estado[1], estado[2] = estado[0] + accion[0], estado[1] + accion[1], 1
                for i in range(6):
                    if personajes[i].pos == 3:
                        personajes[i].pos = 2
                        personajes[i].rect_x -= 900
                        personajes[i].izq_der = 'izquierda'
                    if personajes[i].pos == 5:
                        personajes[i].pos = 4
                        personajes[i].izq_der = 'izquierda'
                        personajes[i].rect_x -= 900

            
            if accion != [1, 1] and accion != [0, 2] and accion != [2, 0]:
                for i in range(6):
                    
                    if personajes[i].rect_x+Personaje.ancho > cursor[0] > personajes[i].rect_x and personajes[i].rect_y + Personaje.altura > cursor[1] > personajes[i].rect_y:
                        if personajes[i].pos == 0 and personajes[i].izq_der == 'izquierda' and pos_bote == 0:
                            personajes[i].mover()
                            if pygame.mouse.get_pressed() == (1, 0, 0):
                                if personajes[i].personaje == 'P':
                                    a += 1
                                elif personajes[i].personaje == 'V':
                                    b += 1
                                if accion == [0, 1] or accion == [1, 0]:
                                    for k in range(6):
                                        if personajes[k].pos == 2:
                                            izquierda = True
                                        if personajes[k].pos == 4:
                                            derecha = True
                                    if izquierda:
                                        personajes[i].x, personajes[i].y = x + 180, y - 50
                                        personajes[i].pos = 4
                                    elif derecha:
                                        personajes[i].x, personajes[i].y = x + 20, y - 50
                                        personajes[i].pos = 2
                                else:
                                    personajes[i].x, personajes[i].y = x + 20, y - 50
                                    personajes[i].pos = 2

                        elif personajes[i].pos == 1 and personajes[i].izq_der == 'derecha' and pos_bote == 1:
                            personajes[i].mover()
                            if pygame.mouse.get_pressed() == (1, 0, 0):
                                if personajes[i].personaje == 'P':
                                    a += 1
                                elif personajes[i].personaje == 'V':
                                    b += 1
                                if accion == [0, 1] or accion == [1, 0]:
                                    for k in range(6):
                                        if personajes[k].pos == 3:
                                            izquierda = True
                                        if personajes[k].pos == 5:
                                            derecha = True
                                    if izquierda:
                                        personajes[i].x, personajes[i].y = x + 180, y - 50
                                        personajes[i].pos = 5
                                    elif derecha:
                                        personajes[i].x, personajes[i].y = x + 20, y - 50
                                        personajes[i].pos = 3
                                else:
                                    personajes[i].x, personajes[i].y = x + 20, y - 50
                                    personajes[i].pos = 3
                                print(i, personajes[i].x, personajes[i].y)

            
            if accion != [0, 0]:
                for j in range(4):
                    if en_bote[j].x + Bote.ancho > cursor[0] > en_bote[j].x and en_bote[j].y + Bote.altura > cursor[1] > en_bote[j].y:
                        k = 7
                        for i in range(6):
                            if personajes[i].pos == en_bote[j].pos:
                                k = i
                        if k != 7:
                            en_bote[j].mover(x, y, personajes[k].personaje)
                            if pygame.mouse.get_pressed() == (1, 0, 0):
                                if personajes[k].personaje == 'P':
                                    a -= 1
                                elif personajes[k].personaje == 'V':
                                    b -= 1
                                if personajes[k].izq_der == 'izquierda':
                                    personajes[k].x, personajes[k].y = personajes[k].rect_x - 12, personajes[k].rect_y
                                    personajes[k].pos = 0
                                elif personajes[k].izq_der == 'derecha':
                                    personajes[k].x, personajes[k].y = personajes[k].rect_x - 12, personajes[k].rect_y
                                    personajes[k].pos = 1
                                if en_bote[j].pos == 2 or en_bote[j].pos == 3:
                                    izquierda = False
                                elif en_bote[j].pos == 4 or en_bote[j].pos == 5:
                                    derecha = False

           
            x = x + x_nuevo

            
            for i in range(6):
                personajes[i].x += personajes[i].x_mas
            accion = [a, b]

        
        elif fin_juego and not fin_jugador:
            pygame.mixer.music.stop()
            snd_fin.play(0)
            fin_jugador = True

    
        elif victoria and not victoria_jugador:
            pygame.mixer.music.stop()
            snd_victoria.play(0)
            victoria_jugador = True

        pygame.display.update()
        clock.tick(25)

    pygame.quit()
    quit()


if __name__ == "__main__":
    main()

class Personaje:

    ancho = 40
    altura = 100
    # pos indicate position of M and C;
    #  0 and 1 indicates left and right shore respectively
    # 2 and 4 indicates left an right of boat at left shore
    # 3 and 5 indicates left an right of boat at right shore

    def __init__(self, x, y, x_mas, pos, personaje, izq_der, imagen1, imagen2, superficie):
        self.izq_der = izq_der
        self.x = x
        self.y = y
        self.x_mas = x_mas
        self.pos = pos
        self.personaje = personaje
        self.rect_x = self.x + 12
        self.rect_y = self.y
        self.imagen1 = imagen1
        self.imagen2 = imagen2
        self.superficie = superficie

    def mostrar(self):
        self.superficie.blit(self.imagen1, (self.x, self.y))

    def mover(self):
        self.superficie.blit(self.imagen2, (self.x, self.y))

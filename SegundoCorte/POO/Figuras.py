
class Circulo2:
    pi=3.14
    def __init__(self,diametro):
        print('Nuevo circulo del tipo 2 con un diametro de: {d}' .format(d=diametro))
        self.radius = diametro/2
    def circunferencia(self):
        return 2*self.pi*self.radius
    def area(self):
        return Circulo2.pi *self.radius ** 2


circulo_prueba = Circulo2(5)
print('El perímetro del círculo es: ', circulo_prueba.circunferencia())
print('El área del círculo es: ', circulo_prueba.area())


class Cuadrado:
    def __init__(self,lado):
        print('\n Nuevo cuadrado con un lado de: {}' .format(lado))
        self.lado = lado
    def perimetro(self):
        return self.lado + self.lado + self.lado + self.lado
    def area(self):
        return self.lado**2 


cuadrado_prueba = Cuadrado(3)
print('El perímetro del cuadrado es: ', cuadrado_prueba.perimetro())
print('El área del cuadrado es: ', cuadrado_prueba.area())

class Rectangulo:
    def __init__(self,alto,ancho):
        print('\n Nuevo rectángulo con un alto de: {}' .format(alto), 'y un ancho de: ' .format(ancho))
        self.alto = alto
        self.ancho = ancho
    def perimetro(self):
        return 2*self.alto + 2*self.ancho
    def area(self):
        return self.ancho*self.alto
        
rectangulo_prueba = Rectangulo(5,4)
print('El perímetro del rectángulo es: ', rectangulo_prueba.perimetro())
print('El área del rectángulo es: ', rectangulo_prueba.area())


class Triangulo:
    def __init__(self,lado1,lado2,):
        print('\n Nuevo triángulo rectángulo de base: {}, y de altura: {}' .format(lado1,lado2))
        self.lado1 = lado1
        self.lado2 = lado2
        self.lado3 = ((lado2**2)+(lado1**2))**(1/2)
    def perimetro(self):
        return self.lado1 + self.lado2 + self.lado3
    def area(self):
        return (self.lado1*self.lado2)/2

triangulo_prueba = Triangulo(5,6)
print('El perímetro del triángulo es: ', triangulo_prueba.perimetro())
print('El área del triángulo es: ', triangulo_prueba.area())

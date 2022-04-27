import zooAnimales.animal as animal
class Reptil(animal):
    iguanas = 0
    serpientes = 0
    listado = []
    totalAnimales = 0
    def __init__(self, nombre, edad, habitat, genero, zona, listado, colorEscamas, largoCola):
        super().__init__(nombre, edad, habitat, genero, zona)
        self._listado = listado
        self._colorEscamas = colorEscamas
        self._largoCola = largoCola
        Reptil.listado.append(self)
        Reptil.totalAnimales += 1
    def cantidadReptiles(self):
        return Reptil.totalAnimales
    def movimiento(self):
        return "reptar"
    @classmethod
    def crearIguana(cls, nombre, edad, genero,zona, listado):
        cls.iguanas += 1
        return Reptil(nombre, edad, "humedal", genero, zona, listado, "verde", 3)
    @classmethod 
    def crearSerpiente(cls,nombre, edad, genero,zona, listado):
        cls.serpientes +=1 
        return Reptil(nombre, edad, "jungla", genero, zona, listado, "blanco", 1)

    @classmethod
    def setListado(cls, listado):
        cls._listado = listado
    @classmethod
    def getListado(cls):
        return cls._listado

    def setColorEscamas(self, colorEscamas):
        self._colorEscamas = colorEscamas
    def getColorEscamas(self):
        return self._colorEscamas

    def setLargoCola(self, largoCola):
        self._largoCola = largoCola
    def getColorPlumas(self):
        return self._largoCola


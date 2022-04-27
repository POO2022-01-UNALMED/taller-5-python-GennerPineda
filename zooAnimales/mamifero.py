import zooAnimales.animal as animal
class Mamifero(animal):
    _listado = []
    leones = 0
    caballos = 0
    totalAnimales = 0
    def __init__(self, nombre, edad, habitat, genero, zona, pelaje, patas):
        super().__init__(nombre, edad, habitat, genero, zona)
        self._pelaje = pelaje
        self._patas = patas
        Mamifero.totalAnimales += 1
        Mamifero._listado.append(self)
    def cantidadMamiferos(self):
        return Mamifero.totalAnimales
    @classmethod
    def crearCaballo(cls, nombre, edad, genero, zona):
        cls.caballos += 1
        return Mamifero(nombre, edad,"pradera", genero, zona, True, 4)
    @classmethod
    def crearLeon(cls, nombre, edad, genero, zona):
        cls.leones
        return Mamifero(nombre, edad,"selva", genero, zona, True, 4)
    
    @classmethod
    def setListado(cls, listado):
        cls._listado = listado
    @classmethod
    def getListado(cls):
        return cls._listado

    def setPelaje(self, pelaje):
        self._pelaje = pelaje
    def getPelaje(self):
        return self._pelaje

    def setPatas(self, patas):
        self._patas = patas
    def getPatas(self):
        return self._patas

    def isPelaje(self):
        return self._pelaje
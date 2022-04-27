import zooAnimales.animal as animal
class Pez(animal):
    salmones = 0
    bacalaos = 0
    _listado = []
    totalAnimales = 0
    def __init__(self, nombre, edad, habitat, genero, zona, colorEscamas, cantidadAletas):
        super().__init__(nombre, edad, habitat, genero, zona)
        self._colorEscamas = colorEscamas
        self._cantidadAletas = cantidadAletas
        Pez._listado.append(self)
        Pez.totalAnimales += 1
    def cantidadPeces(self):
        Pez.totalAnimales
    def movimiento(self):
        return "nadar"
    @classmethod
    def crearSalmon(cls,nombre, edad, genero, zona):
        cls.salmones += 1
        return Pez(nombre, edad, "oceano", genero, zona, "rojo", 6)
    @classmethod
    def crearBacalao(cls,nombre, edad, genero, zona):
        cls.bacalaos += 1
        return Pez(nombre, edad, "oceano", genero, zona, "gris", 6)
    
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

    def setCantidadAletas(self, cantidadAletas):
        self._cantidadAletas = cantidadAletas
    def getCantidadAletas(self):
        return self._cantidadAletas


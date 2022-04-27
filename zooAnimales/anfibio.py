import zooAnimales.animal as animal
class Anfibio(animal):
    ranas = 0
    salamandras = 0
    _listado = []
    totalAnimales = 0
    def __init__(self, nombre, edad, habitat, genero, zona, colorPiel, venenoso):
        super().__init__(nombre, edad, habitat, genero, zona)
        self._colorPiel = colorPiel
        self._venenoso = venenoso
        Anfibio._listado.append(self)
        Anfibio.totalAnimales+=1
        
    def cantidadAnfibios(self):
        return Anfibio.totalAnimales
    def movimiento(self):
        return "saltar"
    @classmethod
    def crearRana(cls, nombre, edad, genero, zona):
        cls.ranas += 1
        return Anfibio(nombre, edad, "selva", genero, zona, "rojo", True)
    @classmethod
    def crearSalamandra(cls,nombre, edad, genero, zona):
        cls.salamandras +=1
        return Anfibio(nombre, edad, "selva", genero, zona, "negro y amarillo", False)
    @classmethod
    def setListado(cls, listado):
        cls._listado = listado
    @classmethod
    def getListado(cls):
        return cls._listado
    
    def setColorPiel(self, colorPiel):
        self._colorPiel = colorPiel
    def getColorPiel(self):
        return self._colorPiel

    def setVenenoso(self, venenoso):
        self._venenoso = venenoso
    def getColorPiel(self):
        return self._venenoso

    def isVenenoso(self):
        return self._venenoso
        
    
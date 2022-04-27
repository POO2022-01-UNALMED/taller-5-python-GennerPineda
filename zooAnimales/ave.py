import zooAnimales.animal as animal
class Ave(animal):
    halcones = 0
    aguilas = 0
    _listado = []
    totalAnimales = 0
    def __init__(self, nombre, edad, habitat, genero, zona, colorPlumas):
        super().__init__(nombre, edad, habitat, genero, zona)
        self._colorPlumas = colorPlumas
        Ave.totalAnimales += 1
        Ave._listado.append(self)
        
    def cantidadAves(self):
        return Ave.totalAnimales
    def movimiento(self):
        return "volar"
    @classmethod
    def crearHalcon(cls, nombre, edad, genero, zona):
        cls.halcones += 1
        return Ave(nombre, edad, "montanas", genero, zona, "cafe glorioso")
    @classmethod
    def crearAguila(cls, nombre, edad, genero, zona):
        cls.aguilas += 1
        return Ave(nombre, edad, "montanas", genero, zona, "blanco y amarillo")
    @classmethod
    def setListado(cls, listado):
        cls._listado = listado
    @classmethod
    def getListado(cls):
        return cls._listado

    def setColorPlumas(self, colorPlumas):
        self._colorPlumas = colorPlumas
    def getColorPlumas(self):
        return self._colorPlumas

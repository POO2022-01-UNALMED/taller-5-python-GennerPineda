class Zoologico():
    def __init__(self, nombre, ubicacion, zonas):
        self._nombre = nombre
        self._ubicacion = ubicacion
        self._zonas = zonas
    def agregarzonas(self, zona):
        self.zonas.append(zona)
    def cantidadTotalAnimales(self):
        k = 0
        for i in range(len(self.zonas)):
            k += self.zonas[i].cantidadAnimales()
        return k
    def setNombre(self, nombre):
        self._nombre = nombre
    def getNombre(self):
        return self._nombre

    def setUbicacion(self, ubicacion):
        self._ubicacion = ubicacion
    def getUbicacion(self):
        return self._ubicacion
    
    def setZona(self, zonas):
        self._zonas = zonas
    def getZona(self):
        return self._zonas
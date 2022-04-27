class Zoologico:
    def __init__(self, nombre, ubicacion, zonas = None):
        self._nombre = nombre
        self._ubicacion = ubicacion
        self._zonas = zonas
    def agregarZonas(self, zona):
        if self._zonas == None:
            self._zonas = []
        self._zonas.append(zona)
    def cantidadTotalAnimales(self):
        k = 0
        for i in range(len(self._zonas)):
            k += self._zonas[i].cantidadAnimales()
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
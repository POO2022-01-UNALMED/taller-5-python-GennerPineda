
class Animal:
    _totalAnimales = 0
    def __init__(self, nombre, edad, habitat, genero, zona = None):
        self._nombre = nombre
        self._edad = edad
        self._habitat = habitat
        self._genero = genero
        self._zona = zona
        Animal._totalAnimales+=1
    def movimiento(self):
        return "desplazarse"
    def totalPorTipo(self):
        from zooAnimales.mamifero import Mamifero
        from zooAnimales.anfibio import Anfibio
        from zooAnimales.ave import Ave
        from zooAnimales.pez import Pez
        from zooAnimales.reptil import Reptil
        return("Mamiferos: "+Mamifero.totalAnimales+"\nAves: "+Ave.totalAnimales+
        "\nReptiles: "+Reptil.totalAnimales+"\nPeces: "+Pez.totalAnimales+"\nAnfibio: "+Anfibio.totalAnimales)
    def __str__(self):
        if self._zona == None:
            return("Mi nombre es "+self._nombre+", tengo una edad de "+self._edad+", habito en "+self._habitat+" y mi genero es "+self._genero)
        else:
            return("Mi nombre es "+self._nombre+", tengo una edad de "+self._edad+", habito en "+self._habitat+" y mi genero es "+self._genero+" la zona en la que me ubico es "+self._zona+" en el "+self)
    @classmethod
    def setTotalAnimales(cls, num):
        Animal._totalAnimales = num 
    def getTotalAnimales(self):
        return Animal._totalAnimales
    
    def setNombre(self, nombre):
        self._nombre = nombre
    def getNombre(self):
        return self._nombre

    def setGenero(self, genero):
        self._genero = genero
    def getGenero(self):
        return self._genero


    def setEdad(self, edad):
        self._edad = edad
    def getEdad(self):
        return self._edad
    def setHabitat(self, habitat):
        self._habitat = habitat
    def getHabitat(self):
        return self._habitat 
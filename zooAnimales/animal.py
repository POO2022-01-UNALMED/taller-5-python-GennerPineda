import zooAnimales.mamifero as mamifero
import zooAnimales.anfibio as anfibio
import zooAnimales.ave as ave
import zooAnimales.mamifero as mamifero
import zooAnimales.pez as pez
import zooAnimales.reptil as reptil

class Animal():
    _totalAnimales = 0
    def __init__(self, nombre, edad, habitat, genero, zona):
        self._nombre = nombre
        self._edad = edad
        self._habitat = habitat
        self._genero = genero
        self._zona = zona
        Animal._totalAnimales+=1
    def movimiento(self):
        return "desplazarse"
    def totalPorTipo(self):
        return("Mamiferos: "+mamifero.totalAnimales+"\nAves: "+ave.totalAnimales+
        "\nReptiles: "+reptil.totalAnimales+"\nPeces: "+pez.totalAnimales+"\nAnfibio: "+anfibio.totalAnimales)
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

    def setEdad(self, edad):
        self._edad = edad
    def getEdad(self):
        return self._edad
    def setHabitat(self, habitat):
        self._habitat = habitat
    def getHabitat(self):
        return self._habitat 